"""Utility functions for A2A CLI application."""

import base64
import logging
import sys
from pathlib import Path
from typing import Optional, Union
from uuid import uuid4

from a2a.types import Message, Part, TextPart, FilePart, FileWithBytes


def setup_logging(level: str = "info") -> None:
    """Set up console logging configuration."""
    log_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stdout
    )


def setup_session_logging(session_id: str, level: str = "info", log_everything: bool = True) -> None:
    """Set up session-based file logging with optional detailed content logging."""
    log_level = getattr(logging, level.upper(), logging.INFO)
    
    # Create logs directory if it doesn't exist
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    # Create session log file
    log_file = logs_dir / f"session_{session_id}.log"
    
    # Clear any existing handlers
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Create file handler
    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    file_handler.setLevel(log_level)
    
    # Create detailed formatter for file logging
    if log_everything:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
    else:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
    
    file_handler.setFormatter(formatter)
    
    # Configure root logger to catch ALL loggers
    root_logger.setLevel(log_level)
    root_logger.addHandler(file_handler)
    
    # Ensure we capture all loggers by setting propagation
    for logger_name in ['shared', 'httpx', 'uvicorn', 'a2a']:
        specific_logger = logging.getLogger(logger_name)
        specific_logger.setLevel(log_level)
        specific_logger.propagate = True
    
    # Also add console handler for important messages only
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.WARNING)  # Only warnings and errors to console
    console_formatter = logging.Formatter("%(levelname)s: %(message)s")
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)
    
    # Store log_everything setting globally for other modules to access
    import os
    os.environ['LOG_EVERYTHING'] = str(log_everything)
    
    print(f"Session logging initialized: {log_file}")
    print(f"Log everything setting: {log_everything}")
    if log_everything:
        print("Detailed logging enabled: prompts, tools, and full content will be logged")
    else:
        print("Standard logging enabled: basic operations only")


def should_log_everything() -> bool:
    """Check if detailed logging is enabled."""
    import os
    return os.environ.get('LOG_EVERYTHING', 'false').lower() == 'true'


def create_text_message(
    content: str, 
    role: str = "user", 
    context_id: Optional[str] = None,
    task_id: Optional[str] = None
) -> Message:
    """Create a text message for A2A communication."""
    return Message(
        messageId=str(uuid4()),
        role=role,
        parts=[Part(root=TextPart(text=content))],
        contextId=context_id,
        taskId=task_id,
    )


def create_message_with_file(
    text_content: str,
    file_path: Union[str, Path],
    role: str = "user",
    context_id: Optional[str] = None,
    task_id: Optional[str] = None
) -> Message:
    """Create a message with both text and file content."""
    file_path = Path(file_path)
    
    # Read and encode file
    with open(file_path, 'rb') as f:
        file_content = base64.b64encode(f.read()).decode('utf-8')
    
    # Create message parts
    parts = [Part(root=TextPart(text=text_content))]
    
    # Add file part
    file_part = Part(root=FilePart(
        file=FileWithBytes(
            name=file_path.name,
            bytes=file_content,
            mimeType=get_mime_type(file_path.suffix)
        )
    ))
    parts.append(file_part)
    
    return Message(
        messageId=str(uuid4()),
        role=role,
        parts=parts,
        contextId=context_id,
        taskId=task_id,
    )


def get_mime_type(file_extension: str) -> str:
    """Get MIME type for file extension."""
    mime_types = {
        '.txt': 'text/plain',
        '.json': 'application/json',
        '.csv': 'text/csv',
        '.pdf': 'application/pdf',
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.html': 'text/html',
        '.xml': 'application/xml',
    }
    return mime_types.get(file_extension.lower(), 'application/octet-stream')


def extract_text_from_message(message: Message) -> str:
    """Extract text content from a message."""
    text_parts = []
    for part in message.parts:
        if hasattr(part.root, 'text'):
            text_parts.append(part.root.text)
    return ''.join(text_parts)


def format_agent_info(agent_card) -> str:
    """Format agent card information for display."""
    info = [
        f"Agent Name: {agent_card.name}",
        f"Description: {agent_card.description}",
        f"Version: {agent_card.version}",
        f"URL: {agent_card.url}",
    ]
    
    if agent_card.capabilities:
        info.append(f"Streaming: {agent_card.capabilities.streaming}")
        info.append(f"Push Notifications: {agent_card.capabilities.pushNotifications}")
    
    if agent_card.skills:
        info.append(f"Skills ({len(agent_card.skills)}):")
        for skill in agent_card.skills:
            info.append(f"  - {skill.name}: {skill.description}")
    
    return '\n'.join(info)