"""Factory for creating LLM providers."""

import logging
from typing import Dict, Any, Optional

from .base import LLMProvider, LLMError
from .gemini import GeminiProvider
from .claude import ClaudeProvider  
from .ollama import OllamaProvider


logger = logging.getLogger(__name__)


class LLMProviderFactory:
    """Factory for creating LLM providers."""
    
    _providers = {
        "gemini": GeminiProvider,
        "claude": ClaudeProvider,
        "ollama": OllamaProvider
    }
    
    @classmethod
    def create_provider(cls, provider_type: str, config: Dict[str, Any]) -> LLMProvider:
        """
        Create an LLM provider instance.
        
        Args:
            provider_type: Type of provider (gemini, claude, ollama)
            config: Provider configuration
            
        Returns:
            Configured LLM provider instance
            
        Raises:
            LLMError: If provider type is unsupported or initialization fails
        """
        provider_type = provider_type.lower()
        
        if provider_type not in cls._providers:
            available = ", ".join(cls._providers.keys())
            raise LLMError(
                f"Unsupported provider type: {provider_type}. Available: {available}",
                provider_type
            )
        
        provider_class = cls._providers[provider_type]
        
        try:
            return provider_class(config)
        except Exception as e:
            if isinstance(e, LLMError):
                raise
            raise LLMError(
                f"Failed to initialize {provider_type} provider: {str(e)}",
                provider_type,
                e
            )
    
    @classmethod
    def get_available_providers(cls) -> list[str]:
        """Get list of available provider types."""
        return list(cls._providers.keys())
    
    @classmethod
    async def test_provider(cls, provider_type: str, config: Dict[str, Any]) -> bool:
        """
        Test if a provider can be created and is healthy.
        
        Args:
            provider_type: Type of provider to test
            config: Provider configuration
            
        Returns:
            True if provider is working, False otherwise
        """
        try:
            provider = cls.create_provider(provider_type, config)
            return await provider.health_check()
        except Exception as e:
            logger.warning(f"Provider {provider_type} test failed: {e}")
            return False