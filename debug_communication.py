#!/usr/bin/env python3
"""Debug client-server communication."""

import asyncio
import httpx
import json
from uuid import uuid4
from a2a.client import A2AClient, A2ACardResolver
from a2a.types import Message, SendMessageRequest, MessageSendParams
from a2a_cli.core.utils import create_text_message


async def debug_communication():
    """Debug the actual communication."""
    print("Debugging A2A communication...")
    
    async with httpx.AsyncClient() as httpx_client:
        # First, get the agent card
        resolver = A2ACardResolver(httpx_client, "http://localhost:8889")
        try:
            agent_card = await resolver.get_agent_card()
            print(f"✓ Got agent card: {agent_card.name}")
        except Exception as e:
            print(f"✗ Failed to get agent card: {e}")
            return
        
        # Create A2A client
        client = A2AClient(httpx_client, agent_card=agent_card)
        
        # Create a simple message
        message = create_text_message("Hello, agent!")
        
        # Create request
        request = SendMessageRequest(
            id=str(uuid4()),
            params=MessageSendParams(message=message)
        )
        
        print(f"Sending message: {message.parts[0].root.text}")
        
        try:
            # Send message and get response
            response = await client.send_message(request)
            
            print(f"Response type: {type(response)}")
            print(f"Response: {response}")
            
            # Debug the response structure
            if hasattr(response, 'root'):
                print(f"Response root type: {type(response.root)}")
                print(f"Response root: {response.root}")
                
                if hasattr(response.root, 'result'):
                    print(f"Root result type: {type(response.root.result)}")
                    print(f"Root result: {response.root.result}")
                    
                    # Check if it's a message
                    if hasattr(response.root.result, 'parts'):
                        print("Found message with parts:")
                        for i, part in enumerate(response.root.result.parts):
                            print(f"Part {i}: {part}")
                            if hasattr(part, 'root') and hasattr(part.root, 'text'):
                                print(f"Text content: '{part.root.text}'")
            
        except Exception as e:
            print(f"✗ Failed to send message: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(debug_communication())