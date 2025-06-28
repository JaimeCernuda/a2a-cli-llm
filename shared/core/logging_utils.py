"""Enhanced logging utilities for structured session logging."""

import logging
from typing import Any, Dict, List, Optional
from datetime import datetime


class StructuredLogger:
    """Enhanced logger for categorized, consolidated logging."""
    
    def __init__(self, logger_name: str):
        self.logger = logging.getLogger(logger_name)
    
    def log_user_query(self, query: str, conversation_id: str) -> None:
        """Log incoming user query."""
        message = f"""
╔══════════════════════════════════════════════════════════════════════════════════
║ 👤 USER QUERY SUBMISSION
║ Conversation ID: {conversation_id}
║ Query: {query}
╚══════════════════════════════════════════════════════════════════════════════════"""
        self.logger.info(message)
    
    def log_orchestrator_to_model(self, phase: str, iteration: int, prompt: str, 
                                  system_prompt: str, tools: Optional[List[Dict]] = None) -> None:
        """Log orchestrator sending request to model."""
        tools_info = f"\n║ Available Tools: {len(tools)} tools" if tools else ""
        if tools:
            for i, tool in enumerate(tools, 1):
                tool_name = tool.get('function', {}).get('name', 'unknown')
                tools_info += f"\n║   {i}. {tool_name}"
        
        message = f"""
╔══════════════════════════════════════════════════════════════════════════════════
║ 🤖 ORCHESTRATOR → MODEL
║ Phase: {phase} (Iteration {iteration})
║ 
║ 📝 User Prompt:
║ {prompt}
║ 
║ 🎯 System Prompt:
║ {system_prompt[:200]}{'...' if len(system_prompt) > 200 else ''}{tools_info}
╚══════════════════════════════════════════════════════════════════════════════════"""
        self.logger.info(message)
    
    def log_model_to_orchestrator(self, phase: str, response_length: int, 
                                 tool_calls: Optional[List[Dict]] = None) -> None:
        """Log model response back to orchestrator."""
        tool_info = ""
        if tool_calls:
            tool_info = f"\n║ Tool Calls Requested: {len(tool_calls)}"
            for tool_call in tool_calls:
                tool_name = tool_call.get('function', {}).get('name', 'unknown')
                tool_info += f"\n║   → {tool_name}"
        
        message = f"""
╔══════════════════════════════════════════════════════════════════════════════════
║ 🔄 MODEL → ORCHESTRATOR  
║ Phase: {phase}
║ Response Length: {response_length} characters{tool_info}
╚══════════════════════════════════════════════════════════════════════════════════"""
        self.logger.info(message)
    
    def log_tool_call(self, tool_name: str, arguments: Dict[str, Any], 
                     execution_time_ms: float, success: bool, 
                     result_preview: str, error_msg: Optional[str] = None) -> None:
        """Log tool execution with consolidated information."""
        status = "✅ SUCCESS" if success else "❌ FAILED"
        error_info = f"\n║ Error: {error_msg}" if error_msg else ""
        
        # Format arguments nicely
        args_str = ""
        for key, value in arguments.items():
            args_str += f"\n║   {key}: {value}"
        
        message = f"""
╔══════════════════════════════════════════════════════════════════════════════════
║ 🔧 TOOL EXECUTION
║ Tool: {tool_name}
║ Status: {status} ({execution_time_ms:.1f}ms)
║ 
║ 📋 Arguments:{args_str}
║ 
║ 📤 Result Preview:
║ {result_preview[:300]}{'...' if len(result_preview) > 300 else ''}{error_info}
╚══════════════════════════════════════════════════════════════════════════════════"""
        self.logger.info(message)
    
    def log_synthesis_complete(self, user_input: str, final_response: str, 
                              tool_count: int) -> None:
        """Log final synthesis completion."""
        message = f"""
╔══════════════════════════════════════════════════════════════════════════════════
║ ✨ SYNTHESIS COMPLETE
║ Original Query: {user_input}
║ Tools Executed: {tool_count}
║ Response Length: {len(final_response)} characters
║ 
║ 📤 Final Response:
║ {final_response}
╚══════════════════════════════════════════════════════════════════════════════════"""
        self.logger.info(message)
    
    def log_phase_transition(self, from_phase: str, to_phase: str, 
                           context: Optional[str] = None) -> None:
        """Log transition between processing phases."""
        context_info = f"\n║ Context: {context}" if context else ""
        
        message = f"""
╔══════════════════════════════════════════════════════════════════════════════════
║ 🔄 PHASE TRANSITION
║ From: {from_phase}
║ To: {to_phase}{context_info}
╚══════════════════════════════════════════════════════════════════════════════════"""
        self.logger.info(message)