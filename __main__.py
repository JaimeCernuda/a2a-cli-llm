"""Entry point for running A2A CLI with uv run commands."""

import sys
import asyncio

def main():
    """Main entry point that routes to client or server."""
    if len(sys.argv) < 2:
        print("Usage: uv run [client|server|test] [options]")
        print("\nCommands:")
        print("  client    - Run A2A CLI client")
        print("  server    - Run A2A CLI server") 
        print("  test      - Run tests")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "client":
        from client.main import main as client_main
        # Remove the command from sys.argv so click gets the right args
        sys.argv = [sys.argv[0]] + sys.argv[2:]
        asyncio.run(client_main())
    elif command == "server":
        from server.main import main as server_main
        # Remove the command from sys.argv so click gets the right args
        sys.argv = [sys.argv[0]] + sys.argv[2:]
        asyncio.run(server_main())
    elif command == "test":
        import pytest
        # Run tests
        pytest.main(["-v", "tests/"])
    else:
        print(f"Unknown command: {command}")
        print("Available commands: client, server, test")
        sys.exit(1)

if __name__ == "__main__":
    main()