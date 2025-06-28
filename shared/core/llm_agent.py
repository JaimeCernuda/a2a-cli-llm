"""LLM-powered agent executor for A2A CLI server."""

import asyncio
import logging
import uuid
import json
from datetime import datetime
from typing import Any, Dict, List, Optional

from a2a.server.agent_execution import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.utils import new_agent_text_message

from shared.llm import LLMProviderFactory, LLMProvider, LLMError, LLMResponse
from shared.mcp import MCPManager
from .config_loader import A2AConfig, ConfigLoader
from .prompt_loader import PromptLoader
from .tool_context import ToolContextManager, ToolResult
from .utils import extract_text_from_message, should_log_everything
from .logging_utils import StructuredLogger


logger = logging.getLogger(__name__)


class LLMAgentExecutor(AgentExecutor):
    """LLM-powered agent executor that uses configurable providers."""
    
    def __init__(self, config: Optional[A2AConfig] = None, config_path: Optional[str] = None) -> None:
        """Initialize the LLM agent executor."""
        # Load configuration
        self.config = config or ConfigLoader.load_config(config_path)
        
        # Validate configuration
        config_errors = ConfigLoader.validate_config(self.config)
        if config_errors:
            logger.warning(f"Configuration issues: {config_errors}")
        
        # Initialize LLM provider
        self.provider: Optional[LLMProvider] = None
        self.provider_name = self.config.default_provider
        
        # Initialize MCP manager
        self.mcp_manager = MCPManager()
        
        # Initialize tool context manager for agentic behavior
        self.tool_context_manager = ToolContextManager()
        
        # Agent info
        self.name = self.config.agent.name
        
        # Load persona if specified
        self.system_prompt = self._load_system_prompt()
        
        # Load external prompts if configured
        self.prompts = self._load_prompts()
        
        # Store log_everything setting directly in the instance
        self.log_everything = should_log_everything()
        logger.info(f"LLM Agent log_everything setting: {self.log_everything}")
        
        # Initialize structured logger
        self.structured_logger = StructuredLogger(__name__)
        
        logger.info(f"Initialized {self.name} with {self.provider_name} provider")
        
        # Initialize MCP servers asynchronously
        asyncio.create_task(self._initialize_mcp_servers())
    
    async def _ensure_provider(self) -> LLMProvider:
        """Ensure LLM provider is initialized and healthy."""
        if self.provider is None:
            await self._initialize_provider()
        
        # Check provider health periodically
        if not await self.provider.health_check():
            logger.warning(f"Provider {self.provider_name} health check failed, reinitializing...")
            await self._initialize_provider()
        
        return self.provider
    
    async def _initialize_provider(self) -> None:
        """Initialize the LLM provider."""
        try:
            provider_config = ConfigLoader.get_provider_config(self.config, self.provider_name)
            self.provider = LLMProviderFactory.create_provider(self.provider_name, provider_config)
            
            # Test the provider
            if not await self.provider.health_check():
                raise LLMError(f"Provider {self.provider_name} failed health check", self.provider_name)
            
            logger.info(f"Successfully initialized {self.provider_name} provider")
            
        except Exception as e:
            logger.error(f"Failed to initialize {self.provider_name} provider: {e}")
            
            # Try fallback providers
            await self._try_fallback_providers()
    
    async def _try_fallback_providers(self) -> None:
        """Try fallback providers if the primary one fails."""
        available_providers = [name for name in self.config.providers.keys() if name != self.provider_name]
        
        for fallback_provider in available_providers:
            try:
                logger.info(f"Trying fallback provider: {fallback_provider}")
                provider_config = ConfigLoader.get_provider_config(self.config, fallback_provider)
                fallback = LLMProviderFactory.create_provider(fallback_provider, provider_config)
                
                if await fallback.health_check():
                    self.provider = fallback
                    self.provider_name = fallback_provider
                    logger.info(f"Successfully switched to fallback provider: {fallback_provider}")
                    return
                    
            except Exception as e:
                logger.warning(f"Fallback provider {fallback_provider} also failed: {e}")
        
        # If all providers fail, raise an error
        raise LLMError("All configured LLM providers failed", "all")
    
    def _load_system_prompt(self) -> str:
        """Load system prompt from config."""
        # Use system_prompt from config if available
        if self.config.agent.system_prompt:
            return self.config.agent.system_prompt
        
        # Ultimate fallback
        return "You are a helpful AI assistant specialized in ADIOS2 data analysis."
    
    def _load_prompts(self) -> Dict[str, str]:
        """Load external prompt files if configured."""
        if not self.config.agent.prompts:
            logger.info("No external prompts configured")
            return {}
        
        try:
            prompts = PromptLoader.load_prompts(self.config.agent.prompts)
            logger.info(f"Loaded {len(prompts)} external prompts: {list(prompts.keys())}")
            return prompts
        except Exception as e:
            logger.warning(f"Failed to load external prompts: {e}")
            return {}
    
    async def _initialize_mcp_servers(self) -> None:
        """Initialize MCP servers from configuration."""
        if not self.config.mcp_servers:
            logger.info("No MCP servers configured")
            return
        
        logger.info(f"Initializing {len(self.config.mcp_servers)} MCP servers...")
        
        for server_name, server_config in self.config.mcp_servers.items():
            if not server_config.enabled:
                logger.info(f"Skipping disabled MCP server: {server_name}")
                continue
            
            try:
                success = await self.mcp_manager.add_server(
                    server_name, 
                    server_config.command, 
                    server_config.cwd
                )
                
                if success:
                    tools = self.mcp_manager.get_server_tools(server_name)
                    logger.info(f"✅ MCP server '{server_name}' connected with {len(tools)} tools")
                else:
                    logger.error(f"❌ Failed to connect to MCP server '{server_name}'")
                    
            except Exception as e:
                logger.error(f"Error initializing MCP server '{server_name}': {e}")
    
    def _get_ollama_tools_schema(self) -> List[Dict[str, Any]]:
        """Convert MCP tools to Ollama tools schema."""
        ollama_tools = []
        
        for tool_name, client in self.mcp_manager.clients.items():
            for mcp_tool_name, tool_schema in client.tools.items():
                # Convert MCP tool schema to Ollama format
                ollama_tool = {
                    "type": "function",
                    "function": {
                        "name": mcp_tool_name,
                        "description": tool_schema.get("description", ""),
                        "parameters": {
                            "type": "object",
                            "properties": {},
                            "required": []
                        }
                    }
                }
                
                # Use actual MCP tool input schema if available
                if "inputSchema" in tool_schema:
                    input_schema = tool_schema["inputSchema"]
                    if "properties" in input_schema:
                        ollama_tool["function"]["parameters"]["properties"] = input_schema["properties"]
                    if "required" in input_schema:
                        ollama_tool["function"]["parameters"]["required"] = input_schema["required"]
                else:
                    # Fallback: infer parameters from tool name and description
                    if mcp_tool_name == "list_bp5":
                        ollama_tool["function"]["parameters"]["properties"]["directory"] = {
                            "type": "string",
                            "description": "Directory path to search for BP5 files",
                            "default": "data/"
                        }
                    elif mcp_tool_name == "inspect_variables":
                        ollama_tool["function"]["parameters"]["properties"]["filename"] = {
                            "type": "string", 
                            "description": "Path to the BP5 file"
                        }
                        ollama_tool["function"]["parameters"]["required"] = ["filename"]
                    elif mcp_tool_name == "inspect_attributes":
                        ollama_tool["function"]["parameters"]["properties"]["filename"] = {
                            "type": "string",
                            "description": "Path to the BP5 file"
                        }
                        ollama_tool["function"]["parameters"]["properties"]["variable_name"] = {
                            "type": "string",
                            "description": "Optional variable name for variable-specific attributes"
                        }
                        ollama_tool["function"]["parameters"]["required"] = ["filename"]
                    elif mcp_tool_name == "read_variable_at_step":
                        ollama_tool["function"]["parameters"]["properties"]["filename"] = {
                            "type": "string",
                            "description": "Path to the BP5 file"
                        }
                        ollama_tool["function"]["parameters"]["properties"]["variable_name"] = {
                            "type": "string",
                            "description": "Name of the variable to read"
                        }
                        ollama_tool["function"]["parameters"]["properties"]["target_step"] = {
                            "type": "integer",
                            "description": "Step number to read from"
                        }
                        ollama_tool["function"]["parameters"]["required"] = ["filename", "variable_name", "target_step"]
                    elif mcp_tool_name == "read_bp5":
                        ollama_tool["function"]["parameters"]["properties"]["filename"] = {
                            "type": "string",
                            "description": "Path to the BP5 file"
                        }
                        ollama_tool["function"]["parameters"]["required"] = ["filename"]
                    elif mcp_tool_name == "get_min_max":
                        ollama_tool["function"]["parameters"]["properties"]["filename"] = {
                            "type": "string",
                            "description": "Path to the BP5 file"
                        }
                        ollama_tool["function"]["parameters"]["properties"]["variable_name"] = {
                            "type": "string",
                            "description": "Name of the variable"
                        }
                        ollama_tool["function"]["parameters"]["properties"]["step"] = {
                            "type": "integer",
                            "description": "Optional step number"
                        }
                        ollama_tool["function"]["parameters"]["required"] = ["filename", "variable_name"]
                    elif mcp_tool_name == "add_variables":
                        ollama_tool["function"]["parameters"]["properties"]["filename"] = {
                            "type": "string",
                            "description": "Path to the BP5 file"
                        }
                        ollama_tool["function"]["parameters"]["properties"]["var1"] = {
                            "type": "string",
                            "description": "First variable name"
                        }
                        ollama_tool["function"]["parameters"]["properties"]["var2"] = {
                            "type": "string",
                            "description": "Second variable name"
                        }
                        ollama_tool["function"]["parameters"]["properties"]["step1"] = {
                            "type": "integer",
                            "description": "Optional step for first variable"
                        }
                        ollama_tool["function"]["parameters"]["properties"]["step2"] = {
                            "type": "integer",
                            "description": "Optional step for second variable"
                        }
                        ollama_tool["function"]["parameters"]["required"] = ["filename", "var1", "var2"]
                
                ollama_tools.append(ollama_tool)
        
        return ollama_tools
    
    async def _handle_ollama_tool_calls(self, llm_response: LLMResponse) -> str:
        """Handle native Ollama tool calls."""
        response_text = llm_response.text
        tool_calls = llm_response.metadata.get("tool_calls", [])
        
        if not tool_calls:
            return response_text
        
        logger.info(f"Processing {len(tool_calls)} tool calls from Ollama")
        
        # Execute each tool call
        tool_results = []
        for tool_call in tool_calls:
            try:
                function = tool_call.get("function", {})
                tool_name = function.get("name")
                arguments = function.get("arguments", {})
                
                if tool_name:
                    logger.info(f"Executing tool: {tool_name} with args: {arguments}")
                    result = await self.mcp_manager.call_tool(tool_name, arguments)
                    
                    # Format the result
                    if 'content' in result:
                        for content_item in result['content']:
                            if 'text' in content_item:
                                tool_results.append(f"\n**{tool_name} result:**\n{content_item['text']}")
                    else:
                        tool_results.append(f"\n**{tool_name} result:**\n{result}")
                        
            except Exception as e:
                logger.error(f"Error executing tool call: {e}")
                tool_results.append(f"\n**Error with {tool_name}:**\n{str(e)}")
        
        # Combine response with tool results
        if tool_results:
            return response_text + "\n" + "\n".join(tool_results)
        else:
            return response_text
    
    async def _handle_tool_calls(self, response_text: str) -> str:
        """Parse and execute tool calls from LLM response."""
        if "TOOL_CALL:" not in response_text:
            return response_text
        
        lines = response_text.split('\n')
        result_lines = []
        
        for line in lines:
            if line.strip().startswith("TOOL_CALL:"):
                try:
                    # Parse tool call
                    tool_call = line.strip()[10:].strip()  # Remove "TOOL_CALL:"
                    
                    # Simple parsing: tool_name(arg1=value1, arg2=value2)
                    if '(' in tool_call and ')' in tool_call:
                        tool_name = tool_call.split('(')[0].strip()
                        args_str = tool_call.split('(', 1)[1].rsplit(')', 1)[0]
                        
                        # Parse arguments
                        arguments = {}
                        if args_str.strip():
                            for arg in args_str.split(','):
                                if '=' in arg:
                                    key, value = arg.split('=', 1)
                                    key = key.strip()
                                    value = value.strip().strip('"\'')
                                    
                                    # Try to convert to appropriate type
                                    if value.isdigit():
                                        value = int(value)
                                    elif value.replace('.', '').isdigit():
                                        value = float(value)
                                    elif value.lower() in ('true', 'false'):
                                        value = value.lower() == 'true'
                                    
                                    arguments[key] = value
                        
                        # Execute tool
                        logger.info(f"Executing tool: {tool_name} with args: {arguments}")
                        result = await self.mcp_manager.call_tool(tool_name, arguments)
                        
                        # Format result
                        result_lines.append(f"Tool result for {tool_name}:")
                        if 'content' in result:
                            for content_item in result['content']:
                                if 'text' in content_item:
                                    result_lines.append(content_item['text'])
                        else:
                            result_lines.append(str(result))
                        
                    else:
                        result_lines.append(f"Error: Invalid tool call format: {tool_call}")
                        
                except Exception as e:
                    logger.error(f"Error executing tool call '{line}': {e}")
                    result_lines.append(f"Tool execution error: {str(e)}")
            else:
                result_lines.append(line)
        
        return '\n'.join(result_lines)
    
    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        """
        Execute the agent logic with enhanced cognitive processing and multi-turn reasoning.
        
        Args:
            context: Request context containing message and metadata
            event_queue: Queue for sending events back to the client
        """
        try:
            # Get user input
            user_input = context.get_user_input()
            logger.info(f"Processing cognitive LLM request: {user_input[:100]}...")
            
            # Create or get conversation context
            conversation_id = context.context_id or str(uuid.uuid4())
            
            # Log user query with structured logging if enabled
            if self.log_everything:
                self.structured_logger.log_user_query(user_input, conversation_id)
            
            # Multi-turn cognitive processing loop
            final_response = await self._cognitive_processing_loop(user_input, conversation_id)
            
            # Send final synthesized response
            await event_queue.enqueue_event(new_agent_text_message(final_response))
            
        except LLMError as e:
            logger.error(f"LLM error: {e}")
            error_message = f"I encountered an issue with the {e.provider} provider: {str(e)}"
            
            # Try to provide helpful guidance
            if "api_key" in str(e).lower():
                error_message += "\n\nPlease check your API key configuration."
            elif "connection" in str(e).lower():
                error_message += "\n\nPlease check your network connection and provider settings."
            
            await event_queue.enqueue_event(new_agent_text_message(error_message))
            
        except Exception as e:
            logger.error(f"Unexpected error in LLM agent: {e}")
            error_message = f"I encountered an unexpected error: {str(e)}"
            await event_queue.enqueue_event(new_agent_text_message(error_message))
    
    async def _cognitive_processing_loop(self, user_input: str, conversation_id: str) -> str:
        """
        Multi-turn cognitive processing loop with parser prompt for final synthesis.
        Uses small model for tool execution, then parser prompt for natural language response.
        """
        max_iterations = 3  # Reduced iterations since we're using parser approach
        iteration = 0
        current_prompt = user_input
        all_tool_results = []
        
        logger.info(f"Starting cognitive processing with parser approach for: {user_input[:50]}...")
        
        # Phase 1: Tool execution with focused prompts
        while iteration < max_iterations:
            iteration += 1
            logger.info(f"Tool execution iteration {iteration}")
            
            # Ensure provider is ready
            provider = await self._ensure_provider()
            
            # Get available tools
            ollama_tools = self._get_ollama_tools_schema()
            
            # Build tool-focused system prompt
            tool_focused_prompt = self._build_tool_focused_prompt(conversation_id)
            
            # Log orchestrator to model communication if enabled
            if self.log_everything:
                self.structured_logger.log_orchestrator_to_model(
                    phase="PHASE 1 - TOOL EXECUTION",
                    iteration=iteration,
                    prompt=current_prompt,
                    system_prompt=tool_focused_prompt,
                    tools=ollama_tools
                )
            
            # Generate response with tools (focused on execution, not explanation)
            llm_response = await provider.generate(
                prompt=current_prompt,
                system_prompt=tool_focused_prompt,
                tools=ollama_tools if ollama_tools else None,
                max_tokens=provider.config.get("max_tokens", 1024),  # Reduced for tool calls
                temperature=0.01  # Very low for reliable tool execution
            )
            
            # Log model response if enabled
            if self.log_everything:
                tool_calls = llm_response.metadata.get("tool_calls", [])
                self.structured_logger.log_model_to_orchestrator(
                    phase="PHASE 1 - TOOL EXECUTION",
                    response_length=len(llm_response.text),
                    tool_calls=tool_calls
                )
            
            # Handle tool calls and collect results
            response_text = await self._handle_agentic_tool_calls(llm_response, conversation_id)
            
            # Extract and store tool results
            iteration_results = self._extract_tool_results(response_text)
            all_tool_results.extend(iteration_results)
            
            logger.info(f"Iteration {iteration}: executed {len(iteration_results)} tools")
            
            # Check if we have sufficient data to answer the question
            if self._has_sufficient_data(user_input, all_tool_results):
                logger.info("Sufficient data collected - proceeding to synthesis")
                break
            
            # Prepare next iteration if more tools needed
            if iteration < max_iterations:
                current_prompt = self._prepare_tool_continuation(response_text, user_input)
        
        # Phase 2: Parser prompt for natural language synthesis
        logger.info("Starting parser prompt synthesis")
        final_response = await self._synthesize_natural_language_response(
            user_input, all_tool_results, conversation_id
        )
        
        return final_response
    
    def _is_analysis_complete(self, response_text: str) -> bool:
        """Check if the response contains the ANALYSIS_COMPLETE token."""
        return "ANALYSIS_COMPLETE:" in response_text
    
    def _extract_final_answer(self, response_text: str) -> str:
        """Extract the final natural language answer after ANALYSIS_COMPLETE."""
        if "ANALYSIS_COMPLETE:" in response_text:
            parts = response_text.split("ANALYSIS_COMPLETE:")
            if len(parts) > 1:
                # Return the content after ANALYSIS_COMPLETE:
                final_answer = parts[-1].strip()
                logger.info(f"Extracted final answer: {final_answer[:100]}...")
                return final_answer
        
        # Fallback: return full response if extraction fails
        return response_text
    
    def _needs_continued_processing(self, response_text: str) -> bool:
        """Check if the response indicates more processing is needed."""
        continuation_indicators = [
            "TASK_DECOMPOSITION:",
            "EXECUTING_TASK:",
            "COMPLETION_CHECK:",
            "❌"  # Failed completion check
        ]
        return any(indicator in response_text for indicator in continuation_indicators)
    
    def _prepare_continuation_prompt(self, response_text: str, original_question: str) -> str:
        """Prepare the prompt for the next iteration of cognitive processing."""
        # Create a prompt that includes the previous work and asks for continuation
        continuation_prompt = f"""Previous analysis progress:
{response_text}

Original question: {original_question}

Continue your cognitive processing. If you have completed all necessary tasks, provide your ANALYSIS_COMPLETE: response with the final natural language answer."""
        
        return continuation_prompt
    
    def _build_enhanced_system_prompt(self, conversation_id: str, user_input: str) -> str:
        """Build enhanced system prompt with conversation context and tool guidance."""
        # Base system prompt (persona)
        base_prompt = self.system_prompt
        
        # Get conversation context
        context_summary = self.tool_context_manager.get_context_for_llm(conversation_id)
        tool_guidance = self.tool_context_manager.generate_tool_guidance(conversation_id)
        
        # Build enhanced prompt
        enhanced_prompt = base_prompt
        
        if context_summary and context_summary.strip():
            enhanced_prompt += f"\n\n## Current Conversation Context:\n{context_summary}"
        
        if tool_guidance and tool_guidance.strip():
            enhanced_prompt += f"\n\n## Tool Usage Guidance:\n{tool_guidance}"
        
        # Add specific guidance for tool result reuse
        enhanced_prompt += """

## Critical Tool Chaining Instructions:
- ALWAYS use the exact file paths returned by list_bp5 in subsequent tool calls
- When inspect_variables or other tools need a filename, use the full absolute path from previous tool results
- For ADIOS2 analysis, ALWAYS start with list_bp5 to discover available files
- Use the discovered file paths exactly as returned - do not modify or truncate them
- If a tool call fails due to file not found, check the exact paths from list_bp5 results
"""
        
        return enhanced_prompt
    
    def _build_tool_focused_prompt(self, conversation_id: str) -> str:
        """Build a tool-focused system prompt for reliable tool execution."""
        # Get conversation context
        context_summary = self.tool_context_manager.get_context_for_llm(conversation_id)
        
        # Use external prompt if available, otherwise fallback to hardcoded
        if "tool_execution" in self.prompts:
            base_prompt = self.prompts["tool_execution"]
            # Add conversation context if available
            if context_summary:
                tool_focused_prompt = f"{base_prompt}\n\n## CONVERSATION CONTEXT:\n{context_summary}"
            else:
                tool_focused_prompt = base_prompt
        else:
            # Fallback to hardcoded prompt
            tool_focused_prompt = f"""You are the Data1.bp File Agent specialized in analyzing /home/jcernuda/micro_agent/adios/data/data1.bp.

## PRIMARY DIRECTIVE:
Execute tools efficiently to gather data. Do NOT provide explanations or natural language responses.
Your only job is to call the appropriate tools with correct parameters.

## FILE PATH:
Always use: /home/jcernuda/micro_agent/adios/data/data1.bp

## TOOL EXECUTION RULES:
1. Call tools with minimal response text
2. Use exact file paths from previous tool results
3. Don't explain what you're doing - just execute tools
4. Don't provide analysis or conclusions - just gather data

{f"## CONVERSATION CONTEXT:\\n{context_summary}" if context_summary else ""}

## AVAILABLE TOOLS:
- inspect_variables: Get variable metadata
- read_bp5: Read all data from file
- get_min_max: Get min/max values for specific variables
- inspect_attributes: Get file attributes
- read_variable_at_step: Read specific variable at specific step
- add_variables: Add two variables together

Execute the necessary tools to answer the user's question, then stop."""
        
        return tool_focused_prompt
    
    def _extract_tool_results(self, response_text: str) -> List[Dict[str, Any]]:
        """Extract tool results from the response text."""
        tool_results = []
        lines = response_text.split('\n')
        
        current_tool = None
        current_result = []
        
        for line in lines:
            if line.startswith('**') and ' result:**' in line:
                # Save previous tool result if any
                if current_tool and current_result:
                    tool_results.append({
                        'tool_name': current_tool,
                        'result': '\n'.join(current_result).strip()
                    })
                
                # Start new tool result
                current_tool = line.replace('**', '').replace(' result:', '').strip()
                current_result = []
            elif current_tool:
                # Accumulate result lines
                current_result.append(line)
        
        # Save last tool result
        if current_tool and current_result:
            tool_results.append({
                'tool_name': current_tool,
                'result': '\n'.join(current_result).strip()
            })
        
        return tool_results
    
    def _has_sufficient_data(self, user_input: str, tool_results: List[Dict[str, Any]]) -> bool:
        """Check if we have sufficient data to answer the user's question."""
        if not tool_results:
            return False
        
        # Basic heuristics for common question patterns
        user_lower = user_input.lower()
        
        # For variable listing questions
        if 'variables' in user_lower and 'what' in user_lower:
            return any('inspect_variables' in result['tool_name'] for result in tool_results)
        
        # For min/max questions
        if any(word in user_lower for word in ['min', 'max', 'minimum', 'maximum']):
            return any('get_min_max' in result['tool_name'] or 'inspect_variables' in result['tool_name'] 
                      for result in tool_results)
        
        # For comparison questions
        if any(word in user_lower for word in ['compare', 'comparison', 'vs', 'versus']):
            return len(tool_results) >= 2  # Need multiple data points
        
        # For temporal/time analysis
        if any(word in user_lower for word in ['time', 'temporal', 'dynamics', 'changes']):
            return any('read_bp5' in result['tool_name'] or 'physical_time' in result['result'] 
                      for result in tool_results)
        
        # For general analysis questions
        if any(word in user_lower for word in ['simulation', 'analysis', 'represents', 'findings']):
            return len(tool_results) >= 1 and any(len(result['result']) > 100 for result in tool_results)
        
        # Default: if we have any substantial data
        return len(tool_results) >= 1
    
    def _prepare_tool_continuation(self, response_text: str, original_question: str) -> str:
        """Prepare prompt for next tool execution iteration."""
        return f"""Continue gathering data for: {original_question}

Previous tools executed, now execute additional tools if needed to fully answer the question.
Focus only on tool execution, not explanations."""
    
    async def _synthesize_natural_language_response(self, user_input: str, tool_results: List[Dict[str, Any]], conversation_id: str) -> str:
        """Use parser prompt to synthesize natural language response from tool results."""
        if not tool_results:
            return "I wasn't able to gather the necessary data to answer your question."
        
        # Build comprehensive data summary
        data_summary = self._build_data_summary(tool_results)
        
        # Create parser prompt for natural language synthesis
        if "parser_synthesis" in self.prompts:
            # Use external prompt with variable substitution
            parser_prompt = PromptLoader.format_prompt(
                self.prompts["parser_synthesis"],
                user_input=user_input,
                data_summary=data_summary
            )
        else:
            # Fallback to hardcoded prompt
            parser_prompt = f"""Based on the scientific data analysis results below, provide a direct, factual answer to the user's question.

## USER QUESTION:
{user_input}

## ANALYSIS RESULTS:
{data_summary}

## RESPONSE REQUIREMENTS:
1. Answer ONLY what the user asked - do not speculate or add interpretations
2. Use the exact data from the analysis results
3. Be factual and precise with numbers and measurements
4. Do NOT make assumptions about what kind of simulation this might be
5. Do NOT suggest causes, mechanisms, or scientific explanations not present in the data
6. If the data shows errors or missing values, acknowledge them honestly
7. Keep responses concise and directly relevant to the question

Provide a direct, factual response using only the information present in the analysis results."""
        
        # Use provider for synthesis with higher temperature for natural language
        provider = await self._ensure_provider()
        
        # Get system prompt for synthesis
        synthesis_system_prompt = self.prompts.get(
            "synthesis_system", 
            "You are a precise data reporter who provides factual answers based strictly on the provided analysis results. Do not speculate or add interpretations beyond what is explicitly shown in the data."
        )
        
        # Log Phase 2 with structured logging if enabled
        if self.log_everything:
            self.structured_logger.log_orchestrator_to_model(
                phase="PHASE 2 - RESPONSE SYNTHESIS",
                iteration=1,
                prompt=parser_prompt,
                system_prompt=synthesis_system_prompt
            )
        
        synthesis_response = await provider.generate(
            prompt=parser_prompt,
            system_prompt=synthesis_system_prompt,
            max_tokens=provider.config.get("max_tokens", 1024),  # Reduced to encourage conciseness
            temperature=0.1  # Lower temperature for factual, precise responses
        )
        
        # Log synthesis completion if enabled
        if self.log_everything:
            self.structured_logger.log_synthesis_complete(
                user_input=user_input,
                final_response=synthesis_response.text,
                tool_count=len(tool_results)
            )
        
        logger.info(f"Generated synthesis response: {len(synthesis_response.text)} characters")
        return synthesis_response.text
    
    def _build_data_summary(self, tool_results: List[Dict[str, Any]]) -> str:
        """Build a comprehensive summary of all tool results."""
        summary_parts = []
        
        for i, result in enumerate(tool_results, 1):
            tool_name = result['tool_name']
            result_data = result['result']
            
            summary_parts.append(f"### Tool {i}: {tool_name}")
            summary_parts.append(result_data)
            summary_parts.append("")  # Add spacing
        
        return "\n".join(summary_parts)
    
    def _log_tool_execution_start(self, tool_name: str, arguments: Dict[str, Any]) -> None:
        """Log tool execution start with pretty formatting."""
        args_str = json.dumps(arguments, indent=2) if arguments else "{}"
        logger.info(f"🔨 Executing tool: {tool_name}")
        logger.info(f"📋 Arguments:\n{args_str}")
    
    def _log_tool_execution_result(self, tool_name: str, result: Any, execution_time_ms: float) -> None:
        """Log tool execution result with pretty formatting."""
        # Determine success/failure
        success = not (isinstance(result, dict) and result.get('isError', False))
        status_emoji = "✅" if success else "❌"
        
        # Format result for logging
        if isinstance(result, dict):
            if 'content' in result:
                # MCP format result
                content_text = ""
                for content_item in result['content']:
                    if 'text' in content_item:
                        content_text += content_item['text'][:200] + ("..." if len(content_item['text']) > 200 else "")
                result_preview = content_text
            elif result.get('isError', False):
                # Error result
                error_msg = result.get('error', 'Unknown error')
                result_preview = f"ERROR: {error_msg}"
            else:
                # Clean result (like from list_bp5)
                result_str = json.dumps(result, indent=2)
                result_preview = result_str[:200] + ("..." if len(result_str) > 200 else "")
        else:
            result_preview = str(result)[:200] + ("..." if len(str(result)) > 200 else "")
        
        logger.info(f"{status_emoji} Tool {tool_name} completed in {execution_time_ms:.1f}ms")
        logger.info(f"📤 Result preview: {result_preview}")
        
        # Log get_min_max failures specifically since they're problematic
        if tool_name == "get_min_max" and not success:
            logger.warning(f"🚨 get_min_max tool failed - this is a known issue. Arguments were: {json.dumps(result.get('_meta', {}), indent=2) if isinstance(result, dict) else 'N/A'}")
    
    def _clean_tool_arguments(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Clean and type-convert tool arguments to handle LLM string conversions."""
        cleaned = {}
        
        for key, value in arguments.items():
            if isinstance(value, str):
                # Handle common string-to-type conversions
                if value == "None" or value == "null":
                    # Convert string "None" to actual None
                    cleaned[key] = None
                elif value.isdigit():
                    # Convert numeric strings to integers
                    cleaned[key] = int(value)
                elif self._is_float_string(value):
                    # Convert float strings to floats
                    cleaned[key] = float(value)
                elif value.lower() in ('true', 'false'):
                    # Convert boolean strings to booleans
                    cleaned[key] = value.lower() == 'true'
                else:
                    # Keep as string
                    cleaned[key] = value
            else:
                # Keep non-string values as-is
                cleaned[key] = value
        
        return cleaned
    
    def _is_float_string(self, value: str) -> bool:
        """Check if a string represents a valid float."""
        try:
            float(value)
            return '.' in value  # Only consider it float if it has a decimal point
        except ValueError:
            return False
    
    async def _handle_agentic_tool_calls(self, llm_response: LLMResponse, conversation_id: str) -> str:
        """Handle tool calls with agentic intelligence and conversation context."""
        response_text = llm_response.text
        tool_calls = llm_response.metadata.get("tool_calls", [])
        
        if not tool_calls:
            return response_text
        
        logger.info(f"Processing {len(tool_calls)} agentic tool calls")
        
        # Execute each tool call with context-aware parameter enhancement
        tool_results = []
        for tool_call in tool_calls:
            try:
                function = tool_call.get("function", {})
                tool_name = function.get("name")
                raw_arguments = function.get("arguments", {})
                
                if tool_name:
                    # Clean and type-convert arguments first
                    cleaned_arguments = self._clean_tool_arguments(raw_arguments)
                    
                    # Log argument cleaning
                    if cleaned_arguments != raw_arguments:
                        logger.info(f"🧹 Cleaned arguments for {tool_name}: {raw_arguments} -> {cleaned_arguments}")
                    
                    # Enhance arguments using conversation context
                    enhanced_arguments = self.tool_context_manager.suggest_parameters(
                        tool_name, conversation_id, cleaned_arguments
                    )
                    
                    # Log parameter enhancement
                    if enhanced_arguments != cleaned_arguments:
                        logger.info(f"🔧 Enhanced parameters for {tool_name}: {cleaned_arguments} -> {enhanced_arguments}")
                    
                    # Pretty log tool execution start
                    self._log_tool_execution_start(tool_name, enhanced_arguments)
                    
                    # Check for missing prerequisites
                    missing_prereqs = self.tool_context_manager.should_suggest_prerequisites(tool_name, conversation_id)
                    if missing_prereqs:
                        logger.info(f"⚠️  Tool {tool_name} has missing prerequisites: {missing_prereqs}")
                        # For now, continue with the call - the LLM should handle prerequisites
                    
                    # Execute the tool call
                    start_time = datetime.now()
                    result = await self.mcp_manager.call_tool(tool_name, enhanced_arguments)
                    execution_time = (datetime.now() - start_time).total_seconds() * 1000
                    
                    # Log tool execution with structured logging if enabled
                    if self.log_everything:
                        success = not (isinstance(result, dict) and result.get('isError', False))
                        error_msg = None
                        if not success and isinstance(result, dict):
                            error_msg = result.get('error', 'Unknown error')
                        
                        # Format result preview
                        if isinstance(result, dict) and 'content' in result:
                            result_preview = ""
                            for content_item in result['content']:
                                if 'text' in content_item:
                                    result_preview += content_item['text']
                        else:
                            result_preview = str(result)
                        
                        self.structured_logger.log_tool_call(
                            tool_name=tool_name,
                            arguments=enhanced_arguments,
                            execution_time_ms=execution_time,
                            success=success,
                            result_preview=result_preview,
                            error_msg=error_msg
                        )
                    else:
                        # Fallback to old logging for console mode
                        self._log_tool_execution_result(tool_name, result, execution_time)
                    
                    # Create tool result object
                    tool_result = ToolResult(
                        tool_name=tool_name,
                        arguments=enhanced_arguments,
                        result=result,
                        timestamp=datetime.now(),
                        success='error' not in result or not result.get('isError', False),
                        error_message=None if 'error' not in result else str(result.get('error', 'Unknown error')),
                        execution_time_ms=execution_time
                    )
                    
                    # Add to conversation context
                    self.tool_context_manager.add_tool_result(conversation_id, tool_result)
                    
                    # Format the result for display
                    if 'content' in result:
                        for content_item in result['content']:
                            if 'text' in content_item:
                                tool_results.append(f"\n**{tool_name} result:**\n{content_item['text']}")
                    else:
                        # Handle clean results (like from list_bp5)
                        if isinstance(result, list):
                            formatted_result = json.dumps(result, indent=2)
                        elif isinstance(result, dict):
                            formatted_result = json.dumps(result, indent=2)
                        else:
                            formatted_result = str(result)
                        tool_results.append(f"\n**{tool_name} result:**\n{formatted_result}")
                        
            except Exception as e:
                logger.error(f"Error executing agentic tool call {tool_name}: {e}")
                # Create failed tool result
                failed_result = ToolResult(
                    tool_name=tool_name,
                    arguments=raw_arguments,
                    result={"error": str(e)},
                    timestamp=datetime.now(),
                    success=False,
                    error_message=str(e)
                )
                self.tool_context_manager.add_tool_result(conversation_id, failed_result)
                tool_results.append(f"\n**Error with {tool_name}:**\n{str(e)}")
        
        # Combine response with tool results
        if tool_results:
            return response_text + "\n" + "\n".join(tool_results)
        else:
            return response_text
    
    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        """
        Handle task cancellation.
        
        Args:
            context: Request context
            event_queue: Event queue for sending cancellation acknowledgment
        """
        logger.info("LLM task cancellation requested")
        
        # Cleanup MCP connections
        try:
            await self.mcp_manager.disconnect_all()
        except Exception as e:
            logger.error(f"Error disconnecting MCP servers during cancellation: {e}")
        
        await event_queue.enqueue_event(
            new_agent_text_message("Task has been cancelled.")
        )
    
    def _extract_message_context(self, context: RequestContext) -> Dict[str, Any]:
        """Extract additional context from the message."""
        message = context.message
        message_context = {
            "has_files": False,
            "file_count": 0,
            "file_types": [],
            "context_id": message.contextId if message else None,
            "task_id": message.taskId if message else None
        }
        
        # Check for file attachments
        if message and message.parts:
            for part in message.parts:
                if hasattr(part.root, 'file'):
                    message_context["has_files"] = True
                    message_context["file_count"] += 1
                    if hasattr(part.root.file, 'name'):
                        file_ext = part.root.file.name.split('.')[-1] if '.' in part.root.file.name else 'unknown'
                        message_context["file_types"].append(file_ext)
        
        return message_context
    
    async def get_provider_status(self) -> Dict[str, Any]:
        """Get current provider status for debugging."""
        status = {
            "current_provider": self.provider_name,
            "provider_healthy": False,
            "available_providers": list(self.config.providers.keys()),
            "config_errors": ConfigLoader.validate_config(self.config)
        }
        
        if self.provider:
            try:
                status["provider_healthy"] = await self.provider.health_check()
                status["model_info"] = self.provider.get_model_info()
            except Exception as e:
                status["provider_error"] = str(e)
        
        return status