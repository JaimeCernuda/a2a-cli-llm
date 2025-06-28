"""LLM-powered agent executor for A2A CLI server."""

import asyncio
import logging
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional

from a2a.server.agent_execution import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.utils import new_agent_text_message

from shared.llm import LLMProviderFactory, LLMProvider, LLMError, LLMResponse
from shared.mcp import MCPManager
from .config_loader import A2AConfig, ConfigLoader
from .persona_loader import PersonaLoader
from .tool_context import ToolContextManager, ToolResult
from .utils import extract_text_from_message


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
        """Load system prompt from persona or config."""
        # If a persona is specified, load it
        if self.config.agent.persona:
            try:
                persona_prompt = PersonaLoader.load_persona(self.config.agent.persona)
                logger.info(f"Loaded persona: {self.config.agent.persona}")
                return persona_prompt
            except (FileNotFoundError, IOError) as e:
                logger.warning(f"Failed to load persona '{self.config.agent.persona}': {e}")
                logger.info("Falling back to system_prompt from config")
        
        # Fall back to system_prompt from config
        if self.config.agent.system_prompt:
            return self.config.agent.system_prompt
        
        # Ultimate fallback
        return "You are a helpful AI assistant."
    
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
        Execute the agent logic using LLM providers with agentic tool chaining.
        
        Args:
            context: Request context containing message and metadata
            event_queue: Queue for sending events back to the client
        """
        try:
            # Get user input
            user_input = context.get_user_input()
            logger.info(f"Processing agentic LLM request: {user_input[:100]}...")
            
            # Create or get conversation context
            conversation_id = context.context_id or str(uuid.uuid4())
            
            # Prepare context from the full message
            message_context = self._extract_message_context(context)
            
            # Ensure provider is ready
            provider = await self._ensure_provider()
            
            # Get available tools in Ollama format
            ollama_tools = self._get_ollama_tools_schema()
            
            # Enhanced system prompt with conversation context
            enhanced_system_prompt = self._build_enhanced_system_prompt(conversation_id, user_input)
            
            # Generate response using LLM with tools and conversation context
            llm_response = await provider.generate(
                prompt=user_input,
                system_prompt=enhanced_system_prompt,
                tools=ollama_tools if ollama_tools else None,
                max_tokens=provider.config.get("max_tokens", 2048),
                temperature=provider.config.get("temperature", 0.7)
            )
            
            # Handle native tool calls with agentic behavior
            response_text = await self._handle_agentic_tool_calls(llm_response, conversation_id)
            
            # Add provider info to response if requested
            if "model" in user_input.lower() or "provider" in user_input.lower():
                model_info = provider.get_model_info()
                response_text += f"\n\n_Using {model_info['provider']} ({model_info['model']})_"
            
            # Send response
            await event_queue.enqueue_event(new_agent_text_message(response_text))
            
            # Log usage info if available
            if llm_response.usage:
                logger.info(f"LLM usage: {llm_response.usage}")
            
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
                    # Enhance arguments using conversation context
                    enhanced_arguments = self.tool_context_manager.suggest_parameters(
                        tool_name, conversation_id, raw_arguments
                    )
                    
                    # Log parameter enhancement
                    if enhanced_arguments != raw_arguments:
                        logger.info(f"Enhanced parameters for {tool_name}: {raw_arguments} -> {enhanced_arguments}")
                    
                    # Check for missing prerequisites
                    missing_prereqs = self.tool_context_manager.should_suggest_prerequisites(tool_name, conversation_id)
                    if missing_prereqs:
                        logger.info(f"Tool {tool_name} has missing prerequisites: {missing_prereqs}")
                        # For now, continue with the call - the LLM should handle prerequisites
                    
                    # Execute the tool call
                    start_time = datetime.now()
                    result = await self.mcp_manager.call_tool(tool_name, enhanced_arguments)
                    execution_time = (datetime.now() - start_time).total_seconds() * 1000
                    
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