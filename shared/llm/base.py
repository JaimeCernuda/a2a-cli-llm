"""Base classes for LLM providers."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Dict, Any, List
import logging


logger = logging.getLogger(__name__)


@dataclass
class LLMResponse:
    """Response from an LLM provider."""
    
    text: str
    model: str
    provider: str
    usage: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None


class LLMError(Exception):
    """Base exception for LLM provider errors."""
    
    def __init__(self, message: str, provider: str, original_error: Optional[Exception] = None):
        super().__init__(message)
        self.provider = provider
        self.original_error = original_error


class LLMProvider(ABC):
    """Abstract base class for LLM providers."""
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize the provider with configuration."""
        self.config = config
        self.name = self.__class__.__name__.replace("Provider", "").lower()
        logger.info(f"Initializing {self.name} provider")
    
    @abstractmethod
    async def generate(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        **kwargs
    ) -> LLMResponse:
        """
        Generate text using the LLM.
        
        Args:
            prompt: The user prompt
            system_prompt: Optional system prompt
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Additional provider-specific parameters
            
        Returns:
            LLMResponse with generated text and metadata
            
        Raises:
            LLMError: If generation fails
        """
        pass
    
    @abstractmethod
    async def health_check(self) -> bool:
        """
        Check if the provider is healthy and accessible.
        
        Returns:
            True if healthy, False otherwise
        """
        pass
    
    def get_default_system_prompt(self) -> str:
        """Get the default system prompt for this agent."""
        return """You are a helpful AI assistant integrated into an A2A (Agent-to-Agent) CLI system. 

Your role:
- Provide helpful, accurate, and concise responses
- Be conversational but professional
- Help users with questions, tasks, and information
- When users ask about your capabilities, mention you're part of an A2A system

Guidelines:
- Keep responses focused and relevant
- If you're unsure about something, say so
- Be friendly and helpful
- Avoid overly technical jargon unless requested"""
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get information about the current model."""
        return {
            "provider": self.name,
            "model": self.config.get("model", "unknown"),
            "config": {k: v for k, v in self.config.items() if k not in ["api_key", "token"]}
        }