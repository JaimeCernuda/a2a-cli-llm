# A2A CLI Client and Server

A powerful A2A (Agent-to-Agent) CLI application with support for multiple LLM providers including Gemini, Claude, and Ollama.

## 🚀 Quick Start

### Basic Usage (Rule-based Agent)
```bash
# Start the server
uv run server

# In another terminal, use the client
uv run client send --agent http://localhost:8000 --message "Hello!"
uv run client interactive --agent http://localhost:8000
```

### LLM-Powered Agent
```bash
# Start LLM-powered server (requires configuration)
uv run server --llm --config docs/config.yaml

# Use with any LLM provider
uv run client interactive --agent http://localhost:8000
```

## 📁 Project Structure

```
├── client/          # A2A CLI client implementation
├── server/          # A2A CLI server implementation  
├── shared/          # Shared components
│   ├── core/        # Core utilities and configuration
│   └── llm/         # LLM provider implementations
├── tests/           # Test suite and validation scripts
├── docs/            # Documentation and configuration files
└── examples/        # Example files for testing
```

## 🧠 LLM Provider Support

### Supported Providers:
- **🦙 Ollama** - Local models (free, no API key required)
- **🤖 Gemini** - Google's AI models (free tier available)
- **🧠 Claude** - Anthropic's models (paid subscription)

### Setup Instructions:

#### Ollama (Recommended for getting started)
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Start Ollama
ollama serve

# Pull a model
ollama pull llama3.2:3b
```

#### Gemini (Free tier)
1. Get API key: https://makersuite.google.com/app/apikey
2. Set environment: `export GEMINI_API_KEY=your_key_here`

#### Claude (Paid)
1. Get API key: https://console.anthropic.com/
2. Set environment: `export CLAUDE_API_KEY=your_key_here`

## 🔧 Configuration

Copy `docs/config.yaml` to customize:
- LLM provider settings
- Model selection  
- API keys and endpoints
- Agent behavior

## 🧪 Testing

```bash
# Run all tests
uv run test

# Test LLM providers
uv run python tests/test_llm_providers.py

# Validate system
uv run python tests/validate_system.py
```

## 📚 Documentation

- [Development Notes](docs/DEVELOPMENT_NOTES.md) - Detailed implementation guide
- [Configuration Guide](docs/config.yaml) - LLM provider setup
- [Example Commands](examples/test_commands.md) - Usage examples

## 🌟 Features

### Client Features
- Multiple operation modes (send, interactive, info)
- File upload support
- Rich terminal interface
- Streaming response handling
- Error handling and retry logic

### Server Features  
- Rule-based and LLM-powered modes
- Multiple LLM provider support
- Configurable agent behavior
- Streaming responses
- File processing capabilities
- Health checks and fallback mechanisms

## 🤝 Development

This project demonstrates:
- A2A protocol implementation
- Multi-LLM provider architecture
- Clean, modular codebase
- Comprehensive testing
- Rich CLI experiences

See [docs/DEVELOPMENT_NOTES.md](docs/DEVELOPMENT_NOTES.md) for detailed implementation insights.