#!/usr/bin/env python3
"""Test script for LLM providers and enhanced A2A system."""

import asyncio
import os
import logging
from pathlib import Path

from a2a_cli.llm import LLMProviderFactory
from a2a_cli.core.config_loader import ConfigLoader
from a2a_cli.core.llm_agent import LLMAgentExecutor


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_ollama_health():
    """Test if Ollama is running and accessible."""
    print("🔍 Testing Ollama availability...")
    
    try:
        import httpx
        async with httpx.AsyncClient(timeout=5) as client:
            response = await client.get("http://localhost:11434/api/tags")
            if response.status_code == 200:
                models = response.json().get("models", [])
                print(f"✅ Ollama is running with {len(models)} models")
                for model in models[:3]:  # Show first 3 models
                    print(f"   - {model['name']}")
                return True
            else:
                print(f"❌ Ollama responded with status {response.status_code}")
                return False
    except Exception as e:
        print(f"❌ Ollama not accessible: {e}")
        print("   💡 Start Ollama with: ollama serve")
        print("   💡 Pull a model with: ollama pull llama3.2:3b")
        return False


async def test_provider_creation():
    """Test creating LLM providers."""
    print("\n🧪 Testing LLM provider creation...")
    
    config = ConfigLoader.load_config("test_config.yaml")
    
    # Test each configured provider
    for provider_name in config.providers.keys():
        print(f"\n   Testing {provider_name} provider...")
        
        try:
            provider_config = ConfigLoader.get_provider_config(config, provider_name)
            
            # Skip providers that need API keys if they're not set
            if provider_name in ["gemini", "claude"] and not provider_config.get("api_key"):
                print(f"   ⏭️  Skipping {provider_name} (no API key)")
                continue
            
            provider = LLMProviderFactory.create_provider(provider_name, provider_config)
            print(f"   ✅ {provider_name} provider created successfully")
            
            # Test health check
            is_healthy = await provider.health_check()
            if is_healthy:
                print(f"   ✅ {provider_name} health check passed")
                
                # Test simple generation
                try:
                    response = await provider.generate(
                        "Say 'Hello from A2A!' and nothing else.",
                        max_tokens=50
                    )
                    print(f"   ✅ {provider_name} generation test: {response.text[:50]}...")
                except Exception as e:
                    print(f"   ⚠️  {provider_name} generation failed: {e}")
            else:
                print(f"   ❌ {provider_name} health check failed")
                
        except Exception as e:
            print(f"   ❌ {provider_name} provider failed: {e}")


async def test_llm_agent():
    """Test the LLM agent executor."""
    print("\n🤖 Testing LLM Agent Executor...")
    
    try:
        # Create LLM agent with test config
        agent = LLMAgentExecutor(config_path="test_config.yaml")
        
        # Get provider status
        status = await agent.get_provider_status()
        print(f"   Current provider: {status['current_provider']}")
        print(f"   Provider healthy: {status['provider_healthy']}")
        
        if status['config_errors']:
            print(f"   Config warnings: {status['config_errors']}")
        
        if status['provider_healthy']:
            print("   ✅ LLM agent is ready")
        else:
            print("   ❌ LLM agent is not ready")
            
    except Exception as e:
        print(f"   ❌ LLM agent initialization failed: {e}")


async def test_provider_fallback():
    """Test provider fallback mechanism."""
    print("\n🔄 Testing provider fallback...")
    
    # Load config and modify it to test fallback
    config = ConfigLoader.load_config("test_config.yaml")
    
    # Set a non-existent provider as default to test fallback
    config.default_provider = "non_existent"
    
    try:
        agent = LLMAgentExecutor(config)
        status = await agent.get_provider_status()
        
        if status['provider_healthy']:
            print(f"   ✅ Fallback worked, using: {status['current_provider']}")
        else:
            print("   ❌ Fallback failed, no working providers")
            
    except Exception as e:
        print(f"   ❌ Fallback test failed: {e}")


def print_setup_instructions():
    """Print setup instructions for different providers."""
    print("\n📋 LLM Provider Setup Instructions:")
    
    print("\n🦙 Ollama (Local, Free):")
    print("   1. Install: curl -fsSL https://ollama.ai/install.sh | sh")
    print("   2. Start: ollama serve")
    print("   3. Pull model: ollama pull llama3.2:3b")
    print("   4. No API key needed!")
    
    print("\n🤖 Google Gemini (Free tier available):")
    print("   1. Get API key: https://makersuite.google.com/app/apikey")
    print("   2. Set environment: export GEMINI_API_KEY=your_key_here")
    print("   3. Free tier includes generous usage limits")
    
    print("\n🧠 Anthropic Claude (Paid):")
    print("   1. Get API key: https://console.anthropic.com/")
    print("   2. Set environment: export CLAUDE_API_KEY=your_key_here")
    print("   3. Requires paid subscription or credits")


async def main():
    """Main test function."""
    print("🚀 A2A CLI LLM Provider Test Suite")
    print("=" * 50)
    
    # Test Ollama availability first
    ollama_available = await test_ollama_health()
    
    # Test provider creation
    await test_provider_creation()
    
    # Test LLM agent
    await test_llm_agent()
    
    # Test fallback mechanism
    await test_provider_fallback()
    
    # Print setup instructions
    print_setup_instructions()
    
    print("\n✨ Test Summary:")
    print(f"   Ollama available: {'✅' if ollama_available else '❌'}")
    print(f"   Gemini API key: {'✅' if os.getenv('GEMINI_API_KEY') else '❌'}")
    print(f"   Claude API key: {'✅' if os.getenv('CLAUDE_API_KEY') else '❌'}")
    
    if ollama_available or os.getenv('GEMINI_API_KEY') or os.getenv('CLAUDE_API_KEY'):
        print("\n🎉 Ready to test LLM-powered A2A agent!")
        print("   Start server: uv run server --llm --config test_config.yaml")
    else:
        print("\n💡 Set up at least one provider to test LLM functionality")


if __name__ == "__main__":
    asyncio.run(main())