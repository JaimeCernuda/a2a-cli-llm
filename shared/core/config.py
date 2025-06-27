"""Configuration management for A2A CLI application."""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class ServerConfig:
    """Server configuration settings."""
    
    host: str = "localhost"
    port: int = 8000
    log_level: str = "info"
    
    @classmethod
    def from_env(cls) -> "ServerConfig":
        """Create configuration from environment variables."""
        return cls(
            host=os.getenv("A2A_HOST", "localhost"),
            port=int(os.getenv("A2A_PORT", "8000")),
            log_level=os.getenv("A2A_LOG_LEVEL", "info"),
        )


@dataclass
class ClientConfig:
    """Client configuration settings."""
    
    agent_url: str
    timeout: int = 30
    max_retries: int = 3
    
    @classmethod
    def from_url(cls, agent_url: str) -> "ClientConfig":
        """Create configuration for a specific agent URL."""
        return cls(
            agent_url=agent_url,
            timeout=int(os.getenv("A2A_TIMEOUT", "30")),
            max_retries=int(os.getenv("A2A_MAX_RETRIES", "3")),
        )