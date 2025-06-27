#!/usr/bin/env python3
"""Quick test of LLM-powered A2A system."""

import asyncio
import httpx
from shared.core.config import ClientConfig
from client.main import A2ACLIClient


async def test_llm_communication():
    """Test communication with LLM-powered server."""
    print("🤖 Testing LLM-powered A2A communication...")
    
    config = ClientConfig.from_url("http://localhost:8001")
    
    try:
        async with A2ACLIClient(config) as client:
            # Test 1: Get agent info
            print("\n📋 Getting agent info...")
            await client.get_agent_info()  # This prints the info
            agent_info = client.agent_card
            print(f"Agent: {agent_info.name}")
            print(f"Description: {agent_info.description}")
            print(f"Version: {agent_info.version}")
            
            # Test 2: Send a greeting
            print("\n💬 Sending greeting...")
            await client.send_message("Hello! Can you tell me about yourself?", streaming=False)
            
            # Test 3: Ask about A2A protocol
            print("\n🔗 Asking about A2A protocol...")
            await client.send_message("What is the A2A protocol?", streaming=False)
            
            # Test 4: Simple math question
            print("\n🧮 Testing reasoning...")
            await client.send_message("What is 2 + 2?", streaming=False)
            
            print("\n✅ All tests completed successfully!")
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    
    return True


if __name__ == "__main__":
    success = asyncio.run(test_llm_communication())
    if success:
        print("\n🎉 LLM-powered A2A system is working!")
    else:
        print("\n💥 Tests failed!")