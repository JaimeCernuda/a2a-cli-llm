# A2A CLI Client and Server

A simple but functional Python CLI application demonstrating A2A (Agent-to-Agent) protocol client and server functionality.

## Quick Start

### Installation
```bash
# Install dependencies
uv sync

# Or if you don't have uv:
pip install -e .
```

### Running the Server
```bash
# Start the A2A server
uv run server --host 0.0.0.0 --port 8000

# Or with specific configuration
uv run server --host localhost --port 9000 --log-level debug
```

### Running the Client
```bash
# Send a simple message
uv run client send --agent http://localhost:8000 --message "Hello, agent!"

# Interactive mode
uv run client interactive --agent http://localhost:8000

# Get agent information
uv run client info --agent http://localhost:8000

# Send a file
uv run client send --agent http://localhost:8000 --message "Analyze this file" --file document.txt
```

### Testing
```bash
# Run basic validation
uv run test

# Or run pytest directly
uv run pytest
```

## Project Structure

```
a2a_cli/
├── __init__.py
├── client.py          # CLI client implementation
├── server.py          # CLI server implementation
├── core/
│   ├── __init__.py
│   ├── agent.py       # Agent executor implementation
│   ├── config.py      # Configuration management
│   └── utils.py       # Utility functions
└── tests/
    ├── __init__.py
    └── test_basic.py   # Basic functionality tests
```

## Features

### Server Features
- A2A protocol compliant server
- Configurable host/port
- Basic message processing
- Streaming support
- Proper logging and error handling

### Client Features
- Multiple operation modes (send, interactive, info)
- File attachment support
- Rich terminal output
- Error handling and validation
- Agent card discovery

## Documentation

See [DEVELOPMENT_NOTES.md](DEVELOPMENT_NOTES.md) for detailed implementation notes, technical insights, and development lessons learned.