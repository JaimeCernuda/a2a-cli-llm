#!/usr/bin/env python3
"""
Test script for the parser prompt approach.
Tests the two-phase system: tool execution + natural language synthesis.
"""

import requests
import json
import time

def ask_parser_agent(question, test_name="", timeout=90):
    """Ask the parser prompt agent a question."""
    if test_name:
        print(f"\n🧠 {test_name}")
    print(f"❓ Question: {question}")
    
    payload = {
        "jsonrpc": "2.0",
        "id": f"parser-{int(time.time())}",
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
            timeout=timeout
        )
        end_time = time.time()
        
        if response.status_code == 200:
            result = response.json()
            response_text = ""
            if "result" in result and "parts" in result["result"]:
                for part in result["result"]["parts"]:
                    if "text" in part:
                        response_text += part["text"]
            
            print(f"🤖 Parser Response ({end_time - start_time:.2f}s):")
            print(response_text)
            print("\n" + "="*70)
            
            # Analyze parser behavior
            analysis = analyze_parser_response(response_text)
            print("🔍 Parser Analysis:")
            for key, value in analysis.items():
                print(f"  {key}: {value}")
            
            return response_text
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"❌ Exception: {e}")

def analyze_parser_response(response_text):
    """Analyze the response for parser prompt effectiveness."""
    analysis = {
        "🔧 Tool Execution Present": "**" in response_text and "result:**" in response_text,
        "📊 Natural Language Present": not response_text.strip().startswith("{") and len([line for line in response_text.split('\n') if line.strip() and not line.startswith('**')]) > 2,
        "🎯 Directly Answers Question": not response_text.startswith("**") and any(word in response_text.lower() for word in ["the", "this", "these", "analysis", "shows", "indicates"]),
        "🔬 Scientific Context": any(word in response_text.lower() for word in ["simulation", "data", "variables", "pressure", "temperature", "time", "step"]),
        "📈 Specific Numbers": any(char.isdigit() for char in response_text) and ("." in response_text or "values" in response_text.lower()),
        "🧮 Structured Response": len(response_text.split('\n')) > 3 and len(response_text) > 200,
        "⚡ No Raw JSON Output": not response_text.strip().startswith('{"') and "TASK_DECOMPOSITION" not in response_text
    }
    
    # Calculate parser effectiveness score
    parser_score = sum(1 for value in analysis.values() if value) / len(analysis)
    analysis["🏆 Parser Score"] = f"{parser_score*100:.0f}%"
    
    return analysis

def main():
    print("🧠 Parser Prompt Agent Test Suite")
    print("=" * 70)
    print("Testing two-phase approach: tool execution + natural language synthesis")
    print("Server should be running with: uv run python -m server.main --config test_config_data1_agent.yaml --llm")
    print("\nStarting parser tests...\n")
    
    # Test 1: Simple variable inquiry
    ask_parser_agent(
        "What variables are in your file?",
        "Test 1: Variable Discovery",
        timeout=60
    )
    
    time.sleep(3)
    
    # Test 2: Statistical analysis
    ask_parser_agent(
        "What are the min and max values for temperature?",
        "Test 2: Statistical Analysis",
        timeout=90
    )
    
    time.sleep(3)
    
    # Test 3: Comparative analysis
    ask_parser_agent(
        "Compare pressure and temperature variables and explain what this tells us about the simulation",
        "Test 3: Comparative Analysis",
        timeout=120
    )
    
    time.sleep(3)
    
    # Test 4: Temporal dynamics
    ask_parser_agent(
        "Analyze how the physical_time variable changes and what this means for the simulation dynamics",
        "Test 4: Temporal Analysis",
        timeout=90
    )
    
    time.sleep(3)
    
    # Test 5: Scientific interpretation
    ask_parser_agent(
        "Based on all the data in your file, what kind of scientific simulation do you think this represents and what are the key findings?",
        "Test 5: Scientific Interpretation",
        timeout=150
    )
    
    print("\n🏁 Parser Prompt Testing Complete!")
    print("\nExpected improvements over cognitive approach:")
    print("✅ Reliable tool execution (maintained)")
    print("✅ Natural language responses (new)")
    print("✅ Scientific interpretation (enhanced)")
    print("✅ Direct question answering (new)")
    print("✅ No raw JSON output (fixed)")

if __name__ == "__main__":
    main()