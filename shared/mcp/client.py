"""MCP client for connecting to external MCP servers."""

import asyncio
import json
import logging
import subprocess
from typing import Any, Dict, List, Optional
from pathlib import Path

logger = logging.getLogger(__name__)


class MCPClient:
    """Client for communicating with MCP servers via subprocess."""
    
    def __init__(self, command: List[str], cwd: Optional[str] = None):
        """
        Initialize MCP client.
        
        Args:
            command: Command to start MCP server (e.g., ["uv", "run", "adios-mcp"])
            cwd: Working directory for the command
        """
        self.command = command
        self.cwd = Path(cwd) if cwd else None
        self.process: Optional[subprocess.Popen] = None
        self.tools: Dict[str, Dict[str, Any]] = {}
        self.is_connected = False
    
    async def connect(self) -> bool:
        """Connect to the MCP server."""
        try:
            logger.info(f"Starting MCP server: {' '.join(self.command)}")
            
            # Start the MCP server process
            self.process = subprocess.Popen(
                self.command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                cwd=self.cwd
            )
            
            # Initialize connection with correct MCP protocol
            init_response = await self._send_request({
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {}
                    },
                    "clientInfo": {
                        "name": "A2A-CLI",
                        "version": "0.1.0"
                    }
                }
            })
            
            # Send initialized notification
            await self._send_notification({
                "jsonrpc": "2.0",
                "method": "notifications/initialized"
            })
            
            # List available tools
            await self._list_tools()
            
            self.is_connected = True
            logger.info(f"Connected to MCP server with {len(self.tools)} tools")
            return True
            
        except Exception as e:
            logger.error(f"Failed to connect to MCP server: {e}")
            await self.disconnect()
            return False
    
    async def disconnect(self):
        """Disconnect from the MCP server."""
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait()
            except Exception as e:
                logger.error(f"Error disconnecting from MCP server: {e}")
            finally:
                self.process = None
        
        self.is_connected = False
        logger.info("Disconnected from MCP server")
    
    async def _send_notification(self, notification: Dict[str, Any]) -> None:
        """Send a notification to the MCP server (no response expected)."""
        if not self.process:
            raise RuntimeError("MCP server not connected")
        
        try:
            # Send notification
            notification_json = json.dumps(notification) + "\n"
            self.process.stdin.write(notification_json)
            self.process.stdin.flush()
            
        except Exception as e:
            logger.error(f"Error sending notification to MCP server: {e}")
            raise
    
    async def _send_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Send a request to the MCP server and get response."""
        if not self.process:
            raise RuntimeError("MCP server not connected")
        
        try:
            # Send request
            request_json = json.dumps(request) + "\n"
            self.process.stdin.write(request_json)
            self.process.stdin.flush()
            
            # Read response
            response_line = self.process.stdout.readline()
            if not response_line:
                raise RuntimeError("No response from MCP server")
            
            response = json.loads(response_line.strip())
            
            if "error" in response:
                raise RuntimeError(f"MCP server error: {response['error']}")
            
            return response
            
        except Exception as e:
            logger.error(f"Error communicating with MCP server: {e}")
            raise
    
    async def _list_tools(self):
        """List available tools from the MCP server."""
        try:
            response = await self._send_request({
                "jsonrpc": "2.0",
                "id": 2,
                "method": "tools/list",
                "params": {}
            })
            
            if "result" in response and "tools" in response["result"]:
                for tool in response["result"]["tools"]:
                    self.tools[tool["name"]] = tool
                    logger.debug(f"Available tool: {tool['name']} - {tool.get('description', 'No description')}")
            
        except Exception as e:
            logger.error(f"Failed to list tools: {e}")
    
    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        Call a tool on the MCP server.
        
        Args:
            tool_name: Name of the tool to call
            arguments: Arguments to pass to the tool
            
        Returns:
            Tool response
        """
        if not self.is_connected:
            raise RuntimeError("MCP server not connected")
        
        if tool_name not in self.tools:
            available_tools = list(self.tools.keys())
            raise ValueError(f"Tool '{tool_name}' not available. Available tools: {available_tools}")
        
        try:
            logger.info(f"Calling MCP tool: {tool_name} with args: {arguments}")
            
            response = await self._send_request({
                "jsonrpc": "2.0",
                "id": 3,
                "method": "tools/call",
                "params": {
                    "name": tool_name,
                    "arguments": arguments
                }
            })
            
            if "result" in response:
                return response["result"]
            else:
                raise RuntimeError(f"Unexpected response format: {response}")
                
        except Exception as e:
            logger.error(f"Error calling tool {tool_name}: {e}")
            raise
    
    def get_available_tools(self) -> Dict[str, str]:
        """Get a dictionary of available tools and their descriptions."""
        return {
            name: tool.get("description", "No description")
            for name, tool in self.tools.items()
        }
    
    def get_tool_schema(self, tool_name: str) -> Optional[Dict[str, Any]]:
        """Get the schema for a specific tool."""
        return self.tools.get(tool_name)
    
    async def __aenter__(self):
        """Async context manager entry."""
        await self.connect()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.disconnect()