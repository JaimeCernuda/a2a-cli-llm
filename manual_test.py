#!/usr/bin/env python3
"""Manual test script for A2A CLI system."""

import asyncio
import threading
import time
import uvicorn
from a2a_cli.server import create_server_app
from a2a_cli.core.config import ServerConfig


def start_test_server():
    """Start a test server."""
    print("Starting test server on localhost:8889...")
    
    config = ServerConfig(host="localhost", port=8889, log_level="warning")
    server_app = create_server_app(config)
    app = server_app.build()
    
    uvicorn_config = uvicorn.Config(
        app=app,
        host="localhost",
        port=8889,
        log_level="warning"
    )
    
    server = uvicorn.Server(uvicorn_config)
    
    def run_server():
        asyncio.run(server.serve())
    
    thread = threading.Thread(target=run_server)
    thread.daemon = True
    thread.start()
    
    time.sleep(2)
    print("Test server started successfully!")
    print("Agent card available at: http://localhost:8889/.well-known/agent.json")
    print()
    print("Now you can test the client with commands like:")
    print("  uv run python -m a2a_cli.client info --agent http://localhost:8889")
    print("  uv run python -m a2a_cli.client send --agent http://localhost:8889 --message 'Hello!'")
    print("  uv run python -m a2a_cli.client interactive --agent http://localhost:8889")
    print()
    print("Press Enter to stop the server...")
    
    try:
        input()
    except KeyboardInterrupt:
        pass
    
    print("Stopping server...")
    server.should_exit = True


if __name__ == "__main__":
    start_test_server()