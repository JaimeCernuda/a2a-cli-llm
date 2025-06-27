"""LLM-powered agent executor for A2A CLI server."""

import asyncio
import logging
from typing import Any, Dict, Optional

from a2a.server.agent_execution import AgentExecutor
from a2a.server.agent_execution.context import RequestContext
from a2a.server.events.event_queue import EventQueue
from a2a.utils import new_agent_text_message

from shared.llm import LLMProviderFactory, LLMProvider, LLMError
from .config_loader import A2AConfig, ConfigLoader
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
        
        # Agent info
        self.name = self.config.agent.name
        logger.info(f"Initialized {self.name} with {self.provider_name} provider")
    
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
    
    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        """
        Execute the agent logic using LLM providers.
        
        Args:
            context: Request context containing message and metadata
            event_queue: Queue for sending events back to the client
        """
        try:
            # Get user input
            user_input = context.get_user_input()
            logger.info(f"Processing LLM request: {user_input[:100]}...")
            
            # Prepare context from the full message
            message_context = self._extract_message_context(context)
            
            # Ensure provider is ready
            provider = await self._ensure_provider()
            
            # Generate response using LLM
            llm_response = await provider.generate(
                prompt=user_input,
                system_prompt=self.config.agent.system_prompt,
                max_tokens=provider.config.get("max_tokens", 2048),
                temperature=provider.config.get("temperature", 0.7)
            )
            
            # Add provider info to response if requested
            response_text = llm_response.text
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
    
    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        """
        Handle task cancellation.
        
        Args:
            context: Request context
            event_queue: Event queue for sending cancellation acknowledgment
        """
        logger.info("LLM task cancellation requested")
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