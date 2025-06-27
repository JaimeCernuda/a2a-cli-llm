"""Utility functions for A2A CLI application."""

import base64
import logging
from pathlib import Path
from typing import Optional, Union
from uuid import uuid4

from a2a.types import Message, Part, TextPart, FilePart, FileWithBytes


def setup_logging(level: str = "info") -> None:
    """Set up logging configuration."""
    log_level = getattr(logging, level.upper(), logging.INFO)
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


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