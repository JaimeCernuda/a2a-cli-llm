"""A2A CLI Server implementation."""

import asyncio
import logging
import uuid
from typing import Optional

import asyncclick as click
import uvicorn
from a2a.server.apps.jsonrpc.starlette_app import A2AStarletteApplication
from a2a.server.request_handlers.default_request_handler import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCard, AgentCapabilities, AgentSkill

from shared.core.llm_agent import LLMAgentExecutor
from shared.core.config_loader import ConfigLoader
from shared.core.utils import setup_logging, setup_session_logging


logger = logging.getLogger(__name__)


def create_agent_card(host: str, port: int, config) -> AgentCard:
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


def create_server_app(host: str, port: int, config_path: Optional[str] = None) -> A2AStarletteApplication:
    """Create and configure the A2A server application."""
    # Load configuration
    full_config = ConfigLoader.load_config(config_path)
    agent_card = create_agent_card(host, port, full_config)
    agent_executor = LLMAgentExecutor(full_config, config_path)
    
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
    "--config",
    help="Path to configuration file"
)
@click.option(
    "--log",
    default="file",
    type=click.Choice(["console", "file"]),
    help="Logging destination: console for terminal output, file for session-based files",
    show_default=True
)
@click.option(
    "--log-everything",
    is_flag=True,
    help="Enable detailed logging including prompts, tools, and full content (default: true for file mode, false for console mode)"
)
async def main(
    host: str, 
    port: int, 
    log_level: str, 
    reload: bool,
    config: Optional[str],
    log: str,
    log_everything: bool
) -> None:
    """
    Start the A2A CLI server.
    
    LLM-powered agent features:
    - AI-powered conversations using configured LLM providers
    - Support for Gemini, Claude, and Ollama
    - Intelligent responses to any questions or tasks
    - File analysis and processing
    - MCP server integration for tool calling
    - Configurable via config.yaml file
    """
    # Generate session ID for this server instance
    session_id = str(uuid.uuid4())[:8]
    
    # Determine log_everything default based on log destination if not explicitly set
    # For file mode: default to True unless user explicitly uses --log-everything to force False
    # For console mode: default to False unless user explicitly uses --log-everything to force True
    if log == "file":
        actual_log_everything = True  # Always True for file mode unless overridden
    else:
        actual_log_everything = log_everything  # Only True for console if flag used
    
    # Set up logging based on destination
    if log == "file":
        setup_session_logging(session_id, log_level, actual_log_everything)
        # Note: Don't log this message as it will go to the log file and show up in console
    else:
        setup_logging(log_level)
    
    # Create server application
    try:
        server_app = create_server_app(host, port, config_path=config)
        app = server_app.build()
        
        logger.info(f"Starting A2A CLI server on {host}:{port}")
        logger.info(f"Mode: LLM-powered agent")
        if config:
            logger.info(f"Using configuration from: {config}")
        logger.info(f"Agent card available at: http://{host}:{port}/.well-known/agent.json")
        
        # Configure uvicorn - disable its logging when using file mode
        if log == "file":
            # For file mode, completely disable uvicorn's internal logging
            uvicorn_config = uvicorn.Config(
                app=app,
                host=host,
                port=port,
                log_config=None,  # Disable uvicorn's default logging
                reload=reload,
                access_log=False
            )
        else:
            # For console mode, use normal uvicorn logging
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