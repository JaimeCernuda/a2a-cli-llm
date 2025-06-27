"""A2A CLI Server implementation."""

import asyncio
import logging
from typing import Optional

import asyncclick as click
import uvicorn
from a2a.server.apps.jsonrpc.starlette_app import A2AStarletteApplication
from a2a.server.request_handlers.default_request_handler import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCard, AgentCapabilities, AgentSkill

from shared.core.agent import CLIAgentExecutor
from shared.core.llm_agent import LLMAgentExecutor
from shared.core.config import ServerConfig
from shared.core.config_loader import ConfigLoader
from shared.core.utils import setup_logging


logger = logging.getLogger(__name__)


def create_agent_card(host: str, port: int) -> AgentCard:
    """Create the agent card that describes this server's capabilities."""
    return AgentCard(
        name="A2A CLI Demo Agent",
        description="A simple demonstration agent for the A2A CLI application",
        url=f"http://{host}:{port}/",
        version="0.1.0",
        defaultInputModes=["text"],
        defaultOutputModes=["text"],
        capabilities=AgentCapabilities(
            streaming=True,
            pushNotifications=False
        ),
        skills=[
            AgentSkill(
                id="greeting",
                name="Greeting",
                description="Responds to greetings and casual conversation",
                tags=["greeting", "conversation"],
                examples=["hello", "hi", "hey there"]
            ),
            AgentSkill(
                id="help",
                name="Help",
                description="Provides help and information about capabilities",
                tags=["help", "info"],
                examples=["help", "what can you do", "info"]
            ),
            AgentSkill(
                id="echo",
                name="Echo",
                description="Echoes back text messages",
                tags=["echo", "repeat"],
                examples=["echo hello world", "repeat this message"]
            ),
            AgentSkill(
                id="time",
                name="Time/Date",
                description="Provides current time and date information",
                tags=["time", "date", "clock"],
                examples=["what time is it", "current date", "time"]
            ),
            AgentSkill(
                id="file_analysis",
                name="File Analysis",
                description="Basic file handling and acknowledgment",
                tags=["file", "upload", "analysis"],
                examples=["analyze this file", "process document"]
            )
        ]
    )


def create_llm_agent_card(host: str, port: int, config) -> AgentCard:
    """Create agent card for LLM-powered agent."""
    return AgentCard(
        name=config.agent.name,
        description=config.agent.description,
        url=f"http://{host}:{port}/",
        version=config.agent.version,
        defaultInputModes=["text"],
        defaultOutputModes=["text"],
        capabilities=AgentCapabilities(
            streaming=True,
            pushNotifications=False
        ),
        skills=[
            AgentSkill(
                id="ai_conversation",
                name="AI Conversation",
                description=f"Intelligent conversation powered by {config.default_provider} LLM",
                tags=["ai", "conversation", "general"],
                examples=["Tell me about quantum computing", "Help me write code", "Explain this concept"]
            ),
            AgentSkill(
                id="question_answering",
                name="Question Answering",
                description="Answer questions on a wide range of topics",
                tags=["qa", "knowledge", "help"],
                examples=["What is machine learning?", "How do I use Python?", "Explain the A2A protocol"]
            ),
            AgentSkill(
                id="code_assistance",
                name="Code Assistance",
                description="Help with programming, debugging, and code review",
                tags=["coding", "programming", "debug"],
                examples=["Review this Python code", "Fix this bug", "Suggest improvements"]
            ),
            AgentSkill(
                id="file_analysis",
                name="File Analysis",
                description="Analyze and process uploaded files with AI",
                tags=["file", "analysis", "ai"],
                examples=["Analyze this document", "Summarize this text file", "Review this code file"]
            ),
            AgentSkill(
                id="general_assistance",
                name="General Assistance",
                description="General purpose AI assistance for various tasks",
                tags=["general", "help", "assistant"],
                examples=["Help me plan a project", "Brainstorm ideas", "Solve this problem"]
            )
        ]
    )


def create_server_app(config: ServerConfig, use_llm: bool = False, config_path: Optional[str] = None) -> A2AStarletteApplication:
    """Create and configure the A2A server application."""
    # Load full configuration if using LLM
    if use_llm:
        full_config = ConfigLoader.load_config(config_path)
        agent_card = create_llm_agent_card(config.host, config.port, full_config)
        agent_executor = LLMAgentExecutor(full_config, config_path)
    else:
        agent_card = create_agent_card(config.host, config.port)
        agent_executor = CLIAgentExecutor()
    
    # Create task store
    task_store = InMemoryTaskStore()
    
    # Create request handler
    request_handler = DefaultRequestHandler(
        agent_executor=agent_executor,
        task_store=task_store
    )
    
    # Create and return the server application
    server_app = A2AStarletteApplication(
        agent_card=agent_card,
        http_handler=request_handler
    )
    
    logger.info(f"Created A2A server with agent: {agent_card.name}")
    return server_app


@click.command()
@click.option(
    "--host", 
    default="localhost", 
    help="Host to bind the server to",
    show_default=True
)
@click.option(
    "--port", 
    default=8000, 
    type=int,
    help="Port to bind the server to",
    show_default=True
)
@click.option(
    "--log-level", 
    default="info",
    type=click.Choice(["debug", "info", "warning", "error"]),
    help="Logging level",
    show_default=True
)
@click.option(
    "--reload",
    is_flag=True,
    help="Enable auto-reload for development"
)
@click.option(
    "--llm",
    is_flag=True,
    help="Use LLM-powered agent instead of rule-based agent"
)
@click.option(
    "--config",
    help="Path to configuration file"
)
async def main(
    host: str, 
    port: int, 
    log_level: str, 
    reload: bool,
    llm: bool,
    config: Optional[str]
) -> None:
    """
    Start the A2A CLI server.
    
    The server can run in two modes:
    
    Default mode (rule-based agent):
    - Respond to greetings and basic conversation
    - Provide help information
    - Echo messages
    - Handle file uploads
    - Provide time/date information
    
    LLM mode (--llm flag):
    - AI-powered conversations using configured LLM providers
    - Support for Gemini, Claude, and Ollama
    - Intelligent responses to any questions or tasks
    - File analysis and processing
    - Configurable via config.yaml file
    """
    # Set up logging
    setup_logging(log_level)
    
    # Create configuration
    server_config = ServerConfig(
        host=host,
        port=port,
        log_level=log_level
    )
    
    # Create server application
    try:
        server_app = create_server_app(server_config, use_llm=llm, config_path=config)
        app = server_app.build()
        
        logger.info(f"Starting A2A CLI server on {host}:{port}")
        logger.info(f"Mode: {'LLM-powered' if llm else 'Rule-based'} agent")
        if llm and config:
            logger.info(f"Using configuration from: {config}")
        logger.info(f"Agent card available at: http://{host}:{port}/.well-known/agent.json")
        
        # Configure uvicorn
        uvicorn_config = uvicorn.Config(
            app=app,
            host=host,
            port=port,
            log_level=log_level,
            reload=reload,
            access_log=True
        )
        
        # Start server
        server = uvicorn.Server(uvicorn_config)
        await server.serve()
        
    except Exception as e:
        logger.error(f"Failed to start server: {e}")
        raise click.ClickException(f"Server startup failed: {e}")


def run_server() -> None:
    """Entry point for running the server."""
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())