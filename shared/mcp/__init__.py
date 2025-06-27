"""MCP (Model Context Protocol) integration for A2A CLI."""

from .client import MCPClient
from .manager import MCPManager

__all__ = ["MCPClient", "MCPManager"]