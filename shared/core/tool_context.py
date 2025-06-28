"""
Tool Context Management System for Agentic Tool Chaining

This module provides context-aware tool execution that enables the LLM to:
1. Remember results from previous tool calls
2. Intelligently infer parameters based on past results
3. Chain tools together to achieve complex goals
4. Maintain conversation continuity across multiple tool invocations
"""

import json
import logging
from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass, field
from datetime import datetime

logger = logging.getLogger(__name__)


@dataclass
class ToolResult:
    """Represents the result of a tool execution."""
    tool_name: str
    arguments: Dict[str, Any]
    result: Any
    timestamp: datetime
    success: bool
    error_message: Optional[str] = None
    execution_time_ms: float = 0.0
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "tool_name": self.tool_name,
            "arguments": self.arguments,
            "result": self.result,
            "timestamp": self.timestamp.isoformat(),
            "success": self.success,
            "error_message": self.error_message,
            "execution_time_ms": self.execution_time_ms
        }


@dataclass 
class ConversationContext:
    """Maintains context for a conversation including tool results."""
    conversation_id: str
    tool_results: List[ToolResult] = field(default_factory=list)
    discovered_files: Set[str] = field(default_factory=set)
    analyzed_variables: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    current_working_directory: Optional[str] = None
    
    def add_tool_result(self, result: ToolResult) -> None:
        """Add a tool result to the conversation context."""
        self.tool_results.append(result)
        self._extract_context_from_result(result)
        
        logger.info(f"Added tool result for {result.tool_name} to conversation {self.conversation_id}")
    
    def _extract_context_from_result(self, result: ToolResult) -> None:
        """Extract useful context information from tool results."""
        # Extract discovered files from file listing tools (generic approach)
        if result.tool_name.startswith(("list_", "discover_", "find_")) and result.success:
            if isinstance(result.result, list):
                for file_path in result.result:
                    if isinstance(file_path, str):
                        self.discovered_files.add(file_path)
            elif isinstance(result.result, str):
                try:
                    # Try to parse as JSON array
                    files = json.loads(result.result)
                    if isinstance(files, list):
                        self.discovered_files.update(str(f) for f in files)
                except json.JSONDecodeError:
                    pass
                    
        elif result.tool_name.startswith(("inspect_", "analyze_")) and result.success:
            # Extract variable information from inspect_variables results
            filename = result.arguments.get("filename", "unknown")
            if isinstance(result.result, dict):
                self.analyzed_variables[filename] = result.result
            elif isinstance(result.result, str):
                try:
                    # Try to parse as JSON
                    variables = json.loads(result.result)
                    if isinstance(variables, dict):
                        self.analyzed_variables[filename] = variables
                except json.JSONDecodeError:
                    pass
    
    def get_discovered_files(self) -> List[str]:
        """Get list of discovered files from previous tool calls."""
        return sorted(list(self.discovered_files))
    
    def get_analyzed_variables(self, filename: str) -> Optional[Dict[str, Any]]:
        """Get variable analysis for a specific file."""
        return self.analyzed_variables.get(filename)
    
    def get_recent_tool_results(self, count: int = 5) -> List[ToolResult]:
        """Get the most recent tool results."""
        return self.tool_results[-count:] if self.tool_results else []
    
    def get_tool_results_by_name(self, tool_name: str) -> List[ToolResult]:
        """Get all results for a specific tool."""
        return [r for r in self.tool_results if r.tool_name == tool_name]
    
    def has_successful_tool_result(self, tool_name: str) -> bool:
        """Check if there's a successful result for a given tool."""
        return any(r.success for r in self.tool_results if r.tool_name == tool_name)
    
    def to_context_summary(self) -> str:
        """Generate a summary of the conversation context for the LLM."""
        summary = []
        
        if self.discovered_files:
            summary.append(f"Discovered files: {', '.join(list(self.discovered_files)[:10])}")
            if len(self.discovered_files) > 10:
                summary.append(f"... and {len(self.discovered_files) - 10} more files")
        
        if self.analyzed_variables:
            summary.append(f"Analyzed variables in {len(self.analyzed_variables)} files")
            for filename, variables in list(self.analyzed_variables.items())[:3]:
                var_names = list(variables.keys())[:5]
                summary.append(f"  {filename}: {', '.join(var_names)}")
        
        if self.tool_results:
            recent_tools = [r.tool_name for r in self.get_recent_tool_results(3)]
            summary.append(f"Recent tools used: {', '.join(recent_tools)}")
        
        return "\n".join(summary) if summary else "No previous context available."


class ToolContextManager:
    """Manages tool execution context and provides intelligent parameter inference."""
    
    def __init__(self):
        self.conversations: Dict[str, ConversationContext] = {}
        # Generic tool dependencies - tools that need files should depend on file discovery tools
        self.tool_dependencies = {}
        
    def get_or_create_conversation(self, conversation_id: str) -> ConversationContext:
        """Get or create a conversation context."""
        if conversation_id not in self.conversations:
            self.conversations[conversation_id] = ConversationContext(conversation_id)
            logger.info(f"Created new conversation context: {conversation_id}")
        return self.conversations[conversation_id]
    
    def suggest_parameters(self, tool_name: str, conversation_id: str, 
                          user_provided_args: Dict[str, Any]) -> Dict[str, Any]:
        """Suggest intelligent parameters based on conversation context."""
        context = self.get_or_create_conversation(conversation_id)
        suggested_args = user_provided_args.copy()
        
        # Generic approach: use discovered files when filename is needed but not provided
        if "filename" in suggested_args and not suggested_args["filename"]:
            discovered_files = context.get_discovered_files()
            if discovered_files:
                # Use the first discovered file as default
                suggested_args["filename"] = discovered_files[0]
                logger.info(f"Suggested filename {discovered_files[0]} for {tool_name} from discovered files")
        
        # For tools requiring variable names, suggest from analyzed variables if available
        if "variable_name" in suggested_args and not suggested_args["variable_name"]:
            # Try to find variables from any analyzed file
            for filename, variables in context.analyzed_variables.items():
                if variables:
                    var_names = list(variables.keys())
                    if var_names:
                        suggested_args["variable_name"] = var_names[0]
                        logger.info(f"Suggested variable {var_names[0]} for {tool_name} from {filename}")
                        break
        
        return suggested_args
    
    def add_tool_result(self, conversation_id: str, result: ToolResult) -> None:
        """Add a tool result to the conversation context."""
        context = self.get_or_create_conversation(conversation_id)
        context.add_tool_result(result)
    
    def get_context_for_llm(self, conversation_id: str) -> str:
        """Get context summary for LLM prompting."""
        context = self.get_or_create_conversation(conversation_id)
        return context.to_context_summary()
    
    def should_suggest_prerequisites(self, tool_name: str, conversation_id: str) -> List[str]:
        """Check if prerequisite tools should be run first."""
        context = self.get_or_create_conversation(conversation_id)
        prerequisites = self.tool_dependencies.get(tool_name, [])
        
        missing_prerequisites = []
        for prereq in prerequisites:
            if not context.has_successful_tool_result(prereq):
                missing_prerequisites.append(prereq)
        
        return missing_prerequisites
    
    def generate_tool_guidance(self, conversation_id: str) -> str:
        """Generate guidance for the LLM about available context and next steps."""
        context = self.get_or_create_conversation(conversation_id)
        guidance = []
        
        if not context.tool_results:
            guidance.append("Start by discovering available files using file discovery tools.")
        
        if context.discovered_files and not context.analyzed_variables:
            files = context.get_discovered_files()
            guidance.append(f"Files discovered: {files[:3]}. Next, analyze variables or metadata using inspection tools.")
        
        if context.analyzed_variables:
            guidance.append("Variables analyzed. You can now perform detailed analysis, get statistics, or read specific data.")
        
        return " ".join(guidance) if guidance else ""