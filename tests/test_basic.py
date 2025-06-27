"""Basic functionality tests for A2A CLI application."""

import asyncio
import pytest
import httpx
from pathlib import Path

from shared.core.config import ServerConfig, ClientConfig
from shared.core.utils import create_text_message, get_mime_type, format_agent_info
from shared.core.agent import CLIAgentExecutor


class TestConfig:
    """Test configuration classes."""
    
    def test_server_config_defaults(self):
        """Test server configuration defaults."""
        config = ServerConfig()
        assert config.host == "localhost"
        assert config.port == 8000
        assert config.log_level == "info"
    
    def test_client_config_creation(self):
        """Test client configuration creation."""
        config = ClientConfig.from_url("http://localhost:8000")
        assert config.agent_url == "http://localhost:8000"
        assert config.timeout == 30
        assert config.max_retries == 3


class TestUtils:
    """Test utility functions."""
    
    def test_create_text_message(self):
        """Test text message creation."""
        message = create_text_message("Hello, world!")
        assert message.role == "user"
        assert len(message.parts) == 1
        assert message.parts[0].root.text == "Hello, world!"
        assert message.messageId is not None
    
    def test_get_mime_type(self):
        """Test MIME type detection."""
        assert get_mime_type('.txt') == 'text/plain'
        assert get_mime_type('.json') == 'application/json'
        assert get_mime_type('.pdf') == 'application/pdf'
        assert get_mime_type('.unknown') == 'application/octet-stream'
    
    def test_format_agent_info(self):
        """Test agent info formatting."""
        from a2a.types import AgentCard, AgentCapabilities
        
        agent_card = AgentCard(
            name="Test Agent",
            description="A test agent",
            url="http://localhost:8000",
            version="1.0.0",
            defaultInputModes=["text"],
            defaultOutputModes=["text"],
            capabilities=AgentCapabilities(streaming=True),
            skills=[]
        )
        
        info = format_agent_info(agent_card)
        assert "Test Agent" in info
        assert "A test agent" in info
        assert "1.0.0" in info


class TestAgentExecutor:
    """Test agent executor functionality."""
    
    @pytest.fixture
    def executor(self):
        """Create agent executor for testing."""
        return CLIAgentExecutor()
    
    def test_executor_initialization(self, executor):
        """Test executor initialization."""
        assert executor.name == "CLI Agent"
    
    @pytest.mark.asyncio
    async def test_greeting_processing(self, executor):
        """Test greeting message processing."""
        response = await executor._process_message("Hello", None)
        assert "Hello" in response
        assert "help" in response.lower()
    
    @pytest.mark.asyncio
    async def test_help_processing(self, executor):
        """Test help message processing."""
        response = await executor._process_message("help", None)
        assert "help" in response.lower()
        assert "greeting" in response.lower()
    
    @pytest.mark.asyncio
    async def test_echo_processing(self, executor):
        """Test echo message processing."""
        response = await executor._process_message("echo test message", None)
        assert "Echo: test message" in response
    
    @pytest.mark.asyncio
    async def test_time_processing(self, executor):
        """Test time request processing."""
        response = await executor._process_message("what time is it", None)
        assert "time" in response.lower()
    
    @pytest.mark.asyncio
    async def test_info_processing(self, executor):
        """Test info request processing."""
        response = await executor._process_message("tell me about yourself", None)
        assert "CLI Demo Agent" in response or "Agent Information" in response


@pytest.mark.asyncio
async def test_server_creation():
    """Test server application creation."""
    from server.main import create_server_app
    
    config = ServerConfig(host="localhost", port=8000)
    server_app = create_server_app(config)
    
    assert server_app is not None
    # The server app should be buildable
    app = server_app.build()
    assert app is not None


@pytest.mark.asyncio 
async def test_client_connection_failure():
    """Test client behavior with invalid agent URL."""
    from client.main import A2ACLIClient
    
    config = ClientConfig.from_url("http://invalid-url:9999")
    
    # This should fail to connect
    try:
        async with A2ACLIClient(config) as client:
            assert False, "Should have failed to connect"
    except Exception:
        # Expected to fail
        pass


if __name__ == "__main__":
    pytest.main([__file__])