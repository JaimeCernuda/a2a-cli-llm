#!/usr/bin/env python3
"""
Comprehensive test script for agentic ADIOS2 workflow.

This script tests the complete agentic tool chaining system:
1. Tool result memory and conversation context
2. Intelligent parameter inference 
3. Path reuse from previous tool results
4. Multi-step scientific analysis workflows
"""

import asyncio
import json
import requests
import time
from typing import Dict, Any


class AgenticWorkflowTester:
    """Test the agentic ADIOS2 workflow capabilities."""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.test_results = []
        
    def make_request(self, message: str, test_name: str) -> Dict[str, Any]:
        """Make a request to the A2A server."""
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
            start_time = time.time()
            response = requests.post(
                self.base_url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=60
            )
            end_time = time.time()
            
            if response.status_code == 200:
                result = response.json()
                response_text = ""
                if "result" in result and "parts" in result["result"]:
                    for part in result["result"]["parts"]:
                        if "text" in part:
                            response_text += part["text"]
                
                print(f"📥 Response ({end_time - start_time:.2f}s):")
                print(response_text)
                
                # Analyze the response
                analysis = self.analyze_response(response_text, test_name)
                
                test_result = {
                    "test_name": test_name,
                    "request": message,
                    "response": response_text,
                    "response_time": end_time - start_time,
                    "success": response.status_code == 200,
                    "analysis": analysis
                }
                
                self.test_results.append(test_result)
                return test_result
                
            else:
                print(f"❌ Error: Status {response.status_code}")
                print(response.text)
                return {"success": False, "error": response.text}
                
        except Exception as e:
            print(f"❌ Exception: {e}")
            return {"success": False, "error": str(e)}
    
    def analyze_response(self, response_text: str, test_name: str) -> Dict[str, Any]:
        """Analyze the response for agentic behavior."""
        analysis = {
            "tools_called": [],
            "file_paths_used": [],
            "variable_names_found": [],
            "error_indicators": [],
            "agentic_behavior": {
                "tool_chaining": False,
                "path_reuse": False,
                "context_awareness": False,
                "intelligent_inference": False
            }
        }
        
        # Check for tool calls
        if "result:" in response_text.lower():
            lines = response_text.split('\n')
            for line in lines:
                if "result:" in line.lower():
                    tool_name = line.split("result:")[0].strip("*").strip()
                    analysis["tools_called"].append(tool_name)
        
        # Check for file paths
        if "/home/jcernuda/micro_agent/adios/data/" in response_text:
            # Extract file paths
            import re
            paths = re.findall(r'/home/jcernuda/micro_agent/adios/data/[^\s",]+\.bp', response_text)
            analysis["file_paths_used"].extend(paths)
        
        # Check for variable names in scientific context
        scientific_vars = ["temperature", "pressure", "physical_time", "nproc"]
        for var in scientific_vars:
            if var in response_text:
                analysis["variable_names_found"].append(var)
        
        # Check for error indicators
        error_keywords = ["error", "not found", "exception", "failed"]
        for keyword in error_keywords:
            if keyword.lower() in response_text.lower():
                analysis["error_indicators"].append(keyword)
        
        # Analyze agentic behavior
        if len(analysis["tools_called"]) > 1:
            analysis["agentic_behavior"]["tool_chaining"] = True
        
        if len(analysis["file_paths_used"]) > 0 and len(analysis["tools_called"]) > 1:
            analysis["agentic_behavior"]["path_reuse"] = True
        
        if "context" in response_text.lower() or "previous" in response_text.lower():
            analysis["agentic_behavior"]["context_awareness"] = True
        
        if not analysis["error_indicators"] and analysis["tools_called"]:
            analysis["agentic_behavior"]["intelligent_inference"] = True
        
        return analysis
    
    def run_comprehensive_test_suite(self):
        """Run the complete agentic workflow test suite."""
        print("🚀 Starting Agentic ADIOS2 Workflow Test Suite")
        print("=" * 60)
        
        # Test 1: Basic tool discovery
        self.make_request(
            "Discover all ADIOS2 BP5 files in the dataset at /home/jcernuda/micro_agent/adios/data",
            "Test 1: Basic File Discovery"
        )
        
        time.sleep(2)  # Allow conversation context to settle
        
        # Test 2: Agentic analysis workflow  
        self.make_request(
            "Perform a complete scientific analysis of the ADIOS2 dataset. Start by listing files, then analyze variables in the first file, and calculate statistics for the pressure variable.",
            "Test 2: Agentic Multi-Step Analysis"
        )
        
        time.sleep(2)
        
        # Test 3: Context-aware follow-up
        self.make_request(
            "Based on the previous analysis, now examine the temperature variable and compare it with pressure using mathematical operations.",
            "Test 3: Context-Aware Follow-up"
        )
        
        time.sleep(2)
        
        # Test 4: Error recovery and path intelligence
        self.make_request(
            "Analyze variables in the second BP5 file you discovered earlier.",
            "Test 4: Intelligent Path Inference"
        )
        
        time.sleep(2)
        
        # Test 5: Complex multi-tool workflow
        self.make_request(
            "Perform a comprehensive temporal analysis: list all files, examine variables in each file, get min/max statistics for all numerical variables, and provide scientific insights.",
            "Test 5: Complex Multi-Tool Workflow"
        )
        
        # Generate test report
        self.generate_test_report()
    
    def generate_test_report(self):
        """Generate a comprehensive test report."""
        print("\n" + "=" * 60)
        print("📊 AGENTIC WORKFLOW TEST REPORT")
        print("=" * 60)
        
        total_tests = len(self.test_results)
        successful_tests = sum(1 for t in self.test_results if t.get("success", False))
        
        print(f"Total Tests: {total_tests}")
        print(f"Successful: {successful_tests}")
        print(f"Failed: {total_tests - successful_tests}")
        print(f"Success Rate: {(successful_tests/total_tests)*100:.1f}%")
        
        print("\n🔧 AGENTIC BEHAVIOR ANALYSIS:")
        
        for test in self.test_results:
            if "analysis" in test:
                behavior = test["analysis"]["agentic_behavior"]
                print(f"\n{test['test_name']}:")
                print(f"  ✅ Tool Chaining: {behavior['tool_chaining']}")
                print(f"  ✅ Path Reuse: {behavior['path_reuse']}")
                print(f"  ✅ Context Awareness: {behavior['context_awareness']}")
                print(f"  ✅ Intelligent Inference: {behavior['intelligent_inference']}")
                print(f"  🔨 Tools Called: {test['analysis']['tools_called']}")
                print(f"  📁 File Paths: {len(test['analysis']['file_paths_used'])}")
                print(f"  🧪 Variables Found: {test['analysis']['variable_names_found']}")
                if test['analysis']['error_indicators']:
                    print(f"  ⚠️  Errors: {test['analysis']['error_indicators']}")
        
        # Overall agentic behavior assessment
        print("\n🎯 OVERALL AGENTIC ASSESSMENT:")
        
        all_behaviors = [t["analysis"]["agentic_behavior"] for t in self.test_results if "analysis" in t]
        if all_behaviors:
            tool_chaining_success = sum(1 for b in all_behaviors if b["tool_chaining"]) / len(all_behaviors)
            path_reuse_success = sum(1 for b in all_behaviors if b["path_reuse"]) / len(all_behaviors)
            context_awareness_success = sum(1 for b in all_behaviors if b["context_awareness"]) / len(all_behaviors)
            inference_success = sum(1 for b in all_behaviors if b["intelligent_inference"]) / len(all_behaviors)
            
            print(f"Tool Chaining Success: {tool_chaining_success*100:.1f}%")
            print(f"Path Reuse Success: {path_reuse_success*100:.1f}%")
            print(f"Context Awareness Success: {context_awareness_success*100:.1f}%")
            print(f"Intelligent Inference Success: {inference_success*100:.1f}%")
            
            overall_agentic_score = (tool_chaining_success + path_reuse_success + context_awareness_success + inference_success) / 4
            print(f"\n🏆 OVERALL AGENTIC SCORE: {overall_agentic_score*100:.1f}%")
            
            if overall_agentic_score >= 0.8:
                print("🎉 EXCELLENT: Highly agentic behavior achieved!")
            elif overall_agentic_score >= 0.6:
                print("👍 GOOD: Strong agentic capabilities with room for improvement")
            elif overall_agentic_score >= 0.4:
                print("⚠️  MODERATE: Basic agentic behavior, needs enhancement")
            else:
                print("❌ POOR: Limited agentic capabilities, significant work needed")


def main():
    """Main test execution."""
    print("🧪 Agentic ADIOS2 Workflow Tester")
    print("Ensure the server is running with: uv run python -m server.main --config test_config_adios2.yaml --llm")
    print("\nStarting tests in 3 seconds...")
    time.sleep(3)
    
    tester = AgenticWorkflowTester()
    tester.run_comprehensive_test_suite()


if __name__ == "__main__":
    main()