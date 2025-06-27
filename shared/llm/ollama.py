"""Ollama provider with native tool calling support."""

import logging
import httpx
import json
from typing import Optional, Dict, Any, List

from .base import LLMProvider, LLMResponse, LLMError


logger = logging.getLogger(__name__)


class OllamaProvider(LLMProvider):
    """Ollama local LLM provider with tool calling support."""
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize Ollama provider."""
        super().__init__(config)
        
        # Set up Ollama configuration
        self.base_url = config.get("base_url", "http://localhost:11434")
        self.model_name = config.get("model", "llama3.2:3b")
        self.default_max_tokens = config.get("max_tokens", 2048)
        self.default_temperature = config.get("temperature", 0.7)
        self.timeout = config.get("timeout", 60)
        
        logger.info(f"Initialized Ollama provider with model: {self.model_name}")
        logger.info(f"Ollama base URL: {self.base_url}")
    
    async def generate(
        self, 
        prompt: str, 
        system_prompt: Optional[str] = None,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        tools: Optional[List[Dict[str, Any]]] = None,
        **kwargs
    ) -> LLMResponse:
        """Generate text using Ollama with optional tool calling."""
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                # Use chat API if tools are provided, otherwise use generate API
                if tools:
                    return await self._generate_with_tools(
                        client, prompt, system_prompt, tools, max_tokens, temperature
                    )
                else:
                    return await self._generate_simple(
                        client, prompt, system_prompt, max_tokens, temperature
                    )
                    
        except httpx.TimeoutException:
            raise LLMError(f"Ollama request timed out after {self.timeout} seconds", "ollama")
        except httpx.RequestError as e:
            raise LLMError(f"Ollama request failed: {str(e)}", "ollama")
        except Exception as e:
            raise LLMError(f"Ollama generation failed: {str(e)}", "ollama")
    
    async def _generate_with_tools(
        self,
        client: httpx.AsyncClient,
        prompt: str,
        system_prompt: Optional[str],
        tools: List[Dict[str, Any]],
        max_tokens: Optional[int],
        temperature: Optional[float]
    ) -> LLMResponse:
        """Generate using Ollama's chat API with tools."""
        # Prepare messages
        messages = []
        
        if system_prompt:
            messages.append({
                "role": "system",
                "content": system_prompt
            })
        
        messages.append({
            "role": "user", 
            "content": prompt
        })
        
        # Prepare chat request with tools
        data = {
            "model": self.model_name,
            "messages": messages,
            "tools": tools,
            "stream": False,
            "options": {
                "temperature": temperature or self.default_temperature,
                "num_predict": max_tokens or self.default_max_tokens,
            }
        }
        
        logger.info(f"Calling Ollama chat API with {len(tools)} tools")
        
        # Make request to Ollama chat API
        response = await client.post(
            f"{self.base_url}/api/chat",
            json=data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code != 200:
            raise LLMError(
                f"Ollama chat API returned status {response.status_code}: {response.text}",
                "ollama"
            )
        
        result = response.json()
        
        if "error" in result:
            raise LLMError(f"Ollama error: {result['error']}", "ollama")
        
        message = result.get("message", {})
        content = message.get("content", "")
        tool_calls = message.get("tool_calls", [])
        
        # Extract usage info if available
        usage = {}
        if "prompt_eval_count" in result:
            usage["prompt_tokens"] = result.get("prompt_eval_count", 0)
            usage["completion_tokens"] = result.get("eval_count", 0)
            usage["total_tokens"] = usage["prompt_tokens"] + usage["completion_tokens"]
        
        return LLMResponse(
            text=content,
            model=self.model_name,
            provider="ollama",
            usage=usage,
            metadata={
                "tool_calls": tool_calls,
                "eval_duration": result.get("eval_duration"),
                "prompt_eval_duration": result.get("prompt_eval_duration"),
            }
        )
    
    async def _generate_simple(
        self,
        client: httpx.AsyncClient,
        prompt: str,
        system_prompt: Optional[str],
        max_tokens: Optional[int],
        temperature: Optional[float]
    ) -> LLMResponse:
        """Generate using Ollama's simple generate API."""
        # Prepare the request
        data = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": temperature or self.default_temperature,
                "num_predict": max_tokens or self.default_max_tokens,
            }
        }
        
        # Add system prompt if provided
        if system_prompt:
            data["system"] = system_prompt
        
        # Make request to Ollama
        response = await client.post(
            f"{self.base_url}/api/generate",
            json=data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code != 200:
            raise LLMError(
                f"Ollama API returned status {response.status_code}: {response.text}",
                "ollama"
            )
        
        result = response.json()
        
        if "error" in result:
            raise LLMError(f"Ollama error: {result['error']}", "ollama")
        
        if not result.get("response"):
            raise LLMError("No text generated by Ollama", "ollama")
        
        # Extract usage info if available
        usage = {}
        if "prompt_eval_count" in result:
            usage["prompt_tokens"] = result.get("prompt_eval_count", 0)
            usage["completion_tokens"] = result.get("eval_count", 0)
            usage["total_tokens"] = usage["prompt_tokens"] + usage["completion_tokens"]
        
        return LLMResponse(
            text=result["response"],
            model=self.model_name,
            provider="ollama",
            usage=usage,
            metadata={
                "eval_duration": result.get("eval_duration"),
                "prompt_eval_duration": result.get("prompt_eval_duration"),
            }
        )
    
    async def health_check(self) -> bool:
        """Check if Ollama is running and model is available."""
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                # Check if Ollama is running
                response = await client.get(f"{self.base_url}/api/tags")
                
                if response.status_code != 200:
                    return False
                
                # Check if our model is available
                tags = response.json()
                models = tags.get("models", [])
                model_names = [model.get("name", "") for model in models]
                
                return any(self.model_name in name for name in model_names)
                
        except Exception as e:
            logger.error(f"Ollama health check failed: {e}")
            return False
    
    def get_model_info(self) -> Dict[str, str]:
        """Get model information."""
        return {
            "provider": "ollama",
            "model": self.model_name,
            "base_url": self.base_url
        }
    
    def get_default_system_prompt(self) -> str:
        """Get default system prompt."""
        return "You are a helpful AI assistant."