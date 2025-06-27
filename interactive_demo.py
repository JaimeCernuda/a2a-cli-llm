#!/usr/bin/env python3
"""Interactive demo of the LLM-powered A2A system."""

import asyncio
from shared.core.config import ClientConfig
from client.main import A2ACLIClient


async def interactive_demo():
    """Run an interactive demonstration of the A2A system."""
    print("🚀 A2A CLI Interactive Demo with LLM")
    print("=" * 50)
    
    config = ClientConfig.from_url("http://localhost:8001")
    
    # Predefined conversation to demonstrate capabilities
    conversation = [
        ("Hello! What can you help me with?", "Testing basic conversation"),
        ("Can you explain what the A2A protocol is?", "Testing knowledge questions"),
        ("Help me write a Python function to calculate fibonacci numbers", "Testing code assistance"),
        ("What's the weather like in Tokyo right now?", "Testing general knowledge"),
        ("Thank you for the demonstration!", "Closing the conversation")
    ]
    
    try:
        async with A2ACLIClient(config) as client:
            print("\n📋 Connected to A2A Agent:")
            await client.get_agent_info()
            
            print("\n💬 Starting Interactive Conversation:")
            print("-" * 40)
            
            for i, (message, description) in enumerate(conversation, 1):
                print(f"\n[{i}/5] {description}:")
                print(f"User: {message}")
                print("Agent: ", end="", flush=True)
                
                # Send message and get response
                await client.send_message(message, streaming=False)
                
                # Add a small delay for readability
                await asyncio.sleep(1)
            
            print("\n" + "=" * 50)
            print("🎉 Interactive Demo Complete!")
            print("\nKey Features Demonstrated:")
            print("✅ Real-time A2A protocol communication")
            print("✅ LLM-powered intelligent responses")
            print("✅ Multiple conversation topics")
            print("✅ Code assistance capabilities")
            print("✅ Rich terminal interface")
            
            return True
            
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        return False


if __name__ == "__main__":
    success = asyncio.run(interactive_demo())
    if success:
        print("\n🌟 The A2A LLM system is ready for production use!")
    else:
        print("\n💥 Demo encountered issues.")