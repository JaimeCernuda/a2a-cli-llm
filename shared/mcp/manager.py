"""MCP manager for handling multiple MCP servers."""

import asyncio
import logging
from typing import Any, Dict, List, Optional
from pathlib import Path

from .client import MCPClient

logger = logging.getLogger(__name__)


class MCPManager:
    """Manager for multiple MCP servers."""
    
    def __init__(self):
        """Initialize MCP manager."""
        self.clients: Dict[str, MCPClient] = {}
        self.is_initialized = False
    
    async def add_server(self, name: str, command: List[str], cwd: Optional[str] = None) -> bool:
        """
        Add and connect to an MCP server.
        
        Args:
            name: Unique name for the server
            command: Command to start the server
            cwd: Working directory for the command
            
        Returns:
            True if successfully connected
        """
        try:
            if name in self.clients:
                logger.warning(f"MCP server '{name}' already exists, disconnecting old one")
                await self.remove_server(name)
            
            client = MCPClient(command, cwd)
            success = await client.connect()
            
            if success:
                self.clients[name] = client
                logger.info(f"Added MCP server '{name}' with {len(client.tools)} tools")
                return True
            else:
                logger.error(f"Failed to connect to MCP server '{name}'")
                return False
                
        except Exception as e:
            logger.error(f"Error adding MCP server '{name}': {e}")
            return False
    
    async def remove_server(self, name: str):
        """Remove and disconnect from an MCP server."""
        if name in self.clients:
            await self.clients[name].disconnect()
            del self.clients[name]
            logger.info(f"Removed MCP server '{name}'")
    
    async def call_tool(self, tool_name: str, arguments: Dict[str, Any], server_name: Optional[str] = None) -> Dict[str, Any]:
        """
        Call a tool on any connected MCP server.
        
        Args:
            tool_name: Name of the tool to call
            arguments: Arguments for the tool
            server_name: Specific server to use (if None, searches all servers)
            
        Returns:
            Tool response
        """
        if server_name:
            # Call tool on specific server
            if server_name not in self.clients:
                raise ValueError(f"MCP server '{server_name}' not found")
            
            return await self.clients[server_name].call_tool(tool_name, arguments)
        
        else:
            # Find server that has this tool
            for name, client in self.clients.items():
                if tool_name in client.tools:
                    logger.debug(f"Found tool '{tool_name}' on server '{name}'")
                    return await client.call_tool(tool_name, arguments)
            
            # Tool not found on any server
            available_tools = self.get_all_tools()
            raise ValueError(f"Tool '{tool_name}' not found on any MCP server. Available tools: {list(available_tools.keys())}")
    
    def get_all_tools(self) -> Dict[str, str]:
        """Get all available tools from all connected servers."""
        all_tools = {}
        for server_name, client in self.clients.items():
            for tool_name, description in client.get_available_tools().items():
                # Add server prefix to avoid conflicts
                prefixed_name = f"{server_name}.{tool_name}" if len(self.clients) > 1 else tool_name
                all_tools[prefixed_name] = f"[{server_name}] {description}"
        
        return all_tools
    
    def get_server_tools(self, server_name: str) -> Dict[str, str]:
        """Get tools for a specific server."""
        if server_name not in self.clients:
            return {}
        
        return self.clients[server_name].get_available_tools()
    
    def get_tool_info(self, tool_name: str) -> Optional[Dict[str, Any]]:
        """Get detailed information about a tool."""
        # Strip server prefix if present
        if "." in tool_name:
            server_name, actual_tool_name = tool_name.split(".", 1)
            if server_name in self.clients:
                return self.clients[server_name].get_tool_schema(actual_tool_name)
        
        # Search all servers
        for client in self.clients.values():
            schema = client.get_tool_schema(tool_name)
            if schema:
                return schema
        
        return None
    
    async def disconnect_all(self):
        """Disconnect from all MCP servers."""
        for name in list(self.clients.keys()):
            await self.remove_server(name)
        
        logger.info("Disconnected from all MCP servers")
    
    def is_connected(self, server_name: Optional[str] = None) -> bool:
        """Check if servers are connected."""
        if server_name:
            return server_name in self.clients and self.clients[server_name].is_connected
        
        return any(client.is_connected for client in self.clients.values())
    
    def get_connected_servers(self) -> List[str]:
        """Get list of connected server names."""
        return [name for name, client in self.clients.items() if client.is_connected]
    
    async def __aenter__(self):
        """Async context manager entry."""
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.disconnect_all()