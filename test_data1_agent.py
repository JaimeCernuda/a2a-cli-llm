#!/usr/bin/env python3
"""
Test script for the focused data1.bp agent.
This tests the hyper-focused agent that specializes only in data1.bp analysis.
"""

import requests
import json
import time

def ask_data1_agent(question, test_name=""):
    """Ask the data1.bp focused agent a question."""
    if test_name:
        print(f"\n🎯 {test_name}")
    print(f"❓ Question: {question}")
    
    payload = {
        "jsonrpc": "2.0",
        "id": f"data1-{int(time.time())}",
        "method": "message/send",
        "params": {
            "message": {
                "messageId": f"msg-{int(time.time())}",
                "parts": [{"type": "text", "text": question}],
                "role": "user"
            }
        }
    }
    
    try:
        start_time = time.time()
        response = requests.post(
            "http://localhost:8000",
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=45
        )
        end_time = time.time()
        
        if response.status_code == 200:
            result = response.json()
            response_text = ""
            if "result" in result and "parts" in result["result"]:
                for part in result["result"]["parts"]:
                    if "text" in part:
                        response_text += part["text"]
            
            print(f"🤖 Agent Response ({end_time - start_time:.2f}s):")
            print(response_text)
            print("\n" + "="*60)
            
            # Analyze if the agent used the correct file path
            if "/home/jcernuda/micro_agent/adios/data/data1.bp" in response_text:
                print("✅ CORRECT: Used proper data1.bp file path")
            elif "error" in response_text.lower():
                print("❌ ERROR: Tool execution failed")
            else:
                print("⚠️  UNCLEAR: Path usage not visible in response")
            
            return response_text
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"❌ Exception: {e}")

def main():
    print("🎯 Data1.bp Focused Agent Test Suite")
    print("=" * 60)
    print("Testing hyper-focused agent specialized in data1.bp analysis")
    print("Server should be running with: uv run python -m server.main --config test_config_data1_agent.yaml --llm")
    print("\nStarting tests...\n")
    
    # Test 1: Basic file awareness
    ask_data1_agent(
        "What variables are in your file?",
        "Test 1: File Introspection"
    )
    
    time.sleep(2)
    
    # Test 2: Specific variable analysis
    ask_data1_agent(
        "Tell me about the pressure variable",
        "Test 2: Variable Analysis"
    )
    
    time.sleep(2)
    
    # Test 3: Statistical analysis
    ask_data1_agent(
        "What are the min and max values for temperature?",
        "Test 3: Statistical Query"
    )
    
    time.sleep(2)
    
    # Test 4: Temporal analysis
    ask_data1_agent(
        "How does physical_time change across timesteps?",
        "Test 4: Temporal Analysis"
    )
    
    time.sleep(2)
    
    # Test 5: Complex analysis
    ask_data1_agent(
        "Compare pressure and temperature and tell me what this simulation represents",
        "Test 5: Scientific Interpretation"
    )
    
    print("\n🏁 Data1.bp Agent Testing Complete!")
    print("The focused agent should consistently use the correct file path and provide expert analysis.")

if __name__ == "__main__":
    main()