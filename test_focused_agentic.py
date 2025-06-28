#!/usr/bin/env python3
"""
Focused test for agentic behavior with explicit path usage.
"""

import requests
import json
import time

def make_request(message: str, test_name: str):
    """Make a focused test request."""
    print(f"\n🧪 {test_name}")
    print(f"📤 Request: {message}")
    
    payload = {
        "jsonrpc": "2.0",
        "id": f"test-{int(time.time())}",
        "method": "message/send",
        "params": {
            "message": {
                "messageId": f"msg-{int(time.time())}",
                "parts": [
                    {
                        "type": "text",
                        "text": message
                    }
                ],
                "role": "user"
            }
        }
    }
    
    try:
        response = requests.post(
            "http://localhost:8000",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            response_text = ""
            if "result" in result and "parts" in result["result"]:
                for part in result["result"]["parts"]:
                    if "text" in part:
                        response_text += part["text"]
            
            print(f"📥 Response:")
            print(response_text)
            return response_text
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
            
    except Exception as e:
        print(f"❌ Exception: {e}")

def main():
    print("🔍 Focused Agentic Test - Testing Path Intelligence")
    print("=" * 60)
    
    # Test 1: Explicit path discovery (this should work)
    make_request(
        "Use list_bp5 tool with directory '/home/jcernuda/micro_agent/adios/data' to find all BP5 files",
        "Test 1: Explicit Path Discovery"
    )
    
    time.sleep(3)
    
    # Test 2: Use discovered paths in follow-up
    make_request(
        "Now use inspect_variables tool with filename '/home/jcernuda/micro_agent/adios/data/data1.bp' to analyze the first file",
        "Test 2: Explicit Path Usage"
    )
    
    time.sleep(3)
    
    # Test 3: Test conversation memory
    make_request(
        "Based on the variables you just discovered, use get_min_max tool to get statistics for the pressure variable in the same file",
        "Test 3: Context-Based Variable Usage"
    )

if __name__ == "__main__":
    main()