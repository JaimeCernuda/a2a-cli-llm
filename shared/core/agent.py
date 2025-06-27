"""Agent executor implementation for A2A CLI server."""

import asyncio
import logging
from typing import Any, Dict

from a2a.server.agent_execution import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.utils import new_agent_text_message

from .utils import extract_text_from_message


logger = logging.getLogger(__name__)


class CLIAgentExecutor(AgentExecutor):
    """Simple agent executor that demonstrates basic A2A functionality."""
    
    def __init__(self) -> None:
        """Initialize the CLI agent executor."""
        self.name = "CLI Agent"
        logger.info(f"Initialized {self.name}")
    
    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        """
        Execute the agent logic for processing incoming messages.
        
        Args:
            context: Request context containing message and metadata
            event_queue: Queue for sending events back to the client
        """
        try:
            # Extract user input from context
            user_input = context.get_user_input()
            logger.info(f"Processing user input: {user_input}")
            
            # Simulate some processing time
            await asyncio.sleep(0.5)
            
            # Process the input and generate response
            response = await self._process_message(user_input, context)
            
            # Send response back to client
            await event_queue.enqueue_event(new_agent_text_message(response))
            logger.info("Response sent successfully")
            
        except Exception as e:
            logger.error(f"Error processing request: {e}")
            error_message = f"Sorry, I encountered an error: {str(e)}"
            await event_queue.enqueue_event(new_agent_text_message(error_message))
    
    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        """
        Handle task cancellation.
        
        Args:
            context: Request context
            event_queue: Event queue for sending cancellation acknowledgment
        """
        logger.info("Task cancellation requested")
        await event_queue.enqueue_event(
            new_agent_text_message("Task has been cancelled.")
        )
    
    async def _process_message(self, user_input: str, context: RequestContext) -> str:
        """
        Process the user message and generate an appropriate response.
        
        Args:
            user_input: The text input from the user
            context: Request context for additional metadata
        
        Returns:
            Response message text
        """
        user_input_lower = user_input.lower()
        
        # Handle different types of messages
        if any(greeting in user_input_lower for greeting in ["hello", "hi", "hey"]):
            return self._handle_greeting(user_input)
        
        elif "help" in user_input_lower:
            return self._handle_help()
        
        elif any(word in user_input_lower for word in ["time", "date"]):
            return self._handle_time_request()
        
        elif "echo" in user_input_lower:
            return self._handle_echo(user_input)
        
        elif "info" in user_input_lower or "about" in user_input_lower:
            return self._handle_info_request()
        
        elif "file" in user_input_lower:
            return self._handle_file_analysis(context)
        
        else:
            return self._handle_general_message(user_input)
    
    def _handle_greeting(self, user_input: str) -> str:
        """Handle greeting messages."""
        return f"Hello! I received your greeting: '{user_input}'. How can I help you today?"
    
    def _handle_help(self) -> str:
        """Handle help requests."""
        return """I'm a simple CLI agent that can help with:
        
• Greetings (hello, hi, hey)
• Help information (help)
• Time/date requests (time, date)
• Echo messages (echo <message>)
• Agent information (info, about)
• File analysis (when you send files)
• General conversation

Try sending me a message or ask for help with any of these topics!"""
    
    def _handle_time_request(self) -> str:
        """Handle time/date requests."""
        from datetime import datetime
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"The current date and time is: {current_time}"
    
    def _handle_echo(self, user_input: str) -> str:
        """Handle echo requests."""
        echo_text = user_input.replace("echo", "", 1).strip()
        if echo_text:
            return f"Echo: {echo_text}"
        else:
            return "Echo: (no text provided)"
    
    def _handle_info_request(self) -> str:
        """Handle information requests about the agent."""
        return f"""Agent Information:
        
Name: {self.name}
Type: CLI Demo Agent
Capabilities: 
  • Text message processing
  • File handling
  • Basic conversation
  • Help and information
  
I'm a simple demonstration agent built with the A2A protocol. 
I can process text messages and provide basic responses."""
    
    def _handle_file_analysis(self, context: RequestContext) -> str:
        """Handle requests involving file analysis."""
        # Check if there are file attachments in the message
        message = context.message
        file_count = 0
        file_info = []
        
        for part in message.parts:
            if hasattr(part.root, 'file'):
                file_count += 1
                file_name = getattr(part.root.file, 'name', 'unknown')
                file_info.append(f"  • {file_name}")
        
        if file_count > 0:
            files_list = '\n'.join(file_info)
            return f"""File Analysis:

I received {file_count} file(s):
{files_list}

Note: This is a basic demo agent. I can acknowledge file uploads 
but don't perform detailed file analysis. In a full implementation, 
this is where I would process the file contents."""
        else:
            return "I can analyze files when you send them along with your message!"
    
    def _handle_general_message(self, user_input: str) -> str:
        """Handle general messages."""
        return f"""Thank you for your message: "{user_input}"

I'm a simple CLI demo agent. I can respond to:
• Greetings • Help requests • Time/date • Echo commands • File uploads

Try asking for 'help' to see all my capabilities!"""