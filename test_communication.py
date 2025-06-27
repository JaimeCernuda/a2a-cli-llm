#!/usr/bin/env python3
"""Test actual client-server communication."""

import asyncio
import httpx
import time
from a2a_cli.client import A2ACLIClient
from a2a_cli.core.config import ClientConfig


async def test_real_communication():
    """Test communication with a real server."""
    print("Testing communication with A2A server...")
    
    # Test with the server (assuming it's running on port 8889)
    config = ClientConfig.from_url("http://localhost:8889")
    
    try:
        async with A2ACLIClient(config) as client:
            print("\n1. Testing greeting message...")
            await client.send_message("Hello, agent!", streaming=False)
            
            print("\n2. Testing help request...")
            await client.send_message("help", streaming=False)
            
            print("\n3. Testing echo...")
            await client.send_message("echo this is a test", streaming=False)
            
            print("\n4. Testing time request...")
            await client.send_message("what time is it", streaming=False)
            
            print("\n5. Testing general message...")
            await client.send_message("How are you doing today?", streaming=False)
            
            print("\nAll tests completed!")
            
    except Exception as e:
        print(f"Error during communication test: {e}")


if __name__ == "__main__":
    asyncio.run(test_real_communication())