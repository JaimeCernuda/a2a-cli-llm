# A2A Agentic Server Framework

A production-ready, domain-agnostic framework for building intelligent A2A (Agent-to-Agent) servers with LLM integration, multi-turn cognitive processing, and MCP tool support.

## 🎯 What Makes This Special

This project demonstrates how to build **truly intelligent A2A agents** that go beyond simple protocol compliance to provide:

### ✅ Core Innovations
- **Two-Phase Cognitive Processing**: Separates tool execution from language generation for reliability and quality
- **Intelligent Tool Context**: Context-aware parameter inference and tool chaining across conversations
- **Domain-Agnostic Design**: No hardcoded domain logic - everything configurable externally
- **Fail-Fast Architecture**: Clear error messages instead of silent fallbacks
- **MCP Integration**: Automatic tool discovery with Model Context Protocol support

### ✅ Production Features
- **Multi-Provider LLM Support**: Ollama (local), Gemini, Claude with automatic failover
- **External Configuration**: Agent cards, prompts, and behaviors defined in external files
- **Structured Logging**: Comprehensive observability with session-based logging
- **Health Monitoring**: Provider health checks and MCP server status monitoring
- **Error Recovery**: Graceful handling of provider and tool failures

## 🚀 Quick Start

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd micro_agent

# Install dependencies
uv sync

# Or without uv:
pip install -e .
```

### Basic Setup
```bash
# 1. Install and start Ollama (for local LLM)
curl -fsSL https://ollama.ai/install.sh | sh
ollama serve
ollama pull llama3.2:1b

# 2. Start the A2A server with ADIOS2 example
uv run python -m server.main --config config_data1_agent.yaml

# 3. In another terminal, interact with the agent
uv run python -m client.main interactive --agent http://localhost:8000
```

### Agent Card Discovery
```bash
# Check the agent's capabilities
curl http://localhost:8000/.well-known/agent.json | jq
```

## 📚 Comprehensive Documentation

This project includes a complete **technical wiki** covering every aspect of the implementation:

### 🏗️ Architecture & Design
- **[📖 Overview](docs/wiki/00-OVERVIEW.md)** - Project goals and architecture overview
- **[🎯 Design Architecture](docs/wiki/01-DESIGN-ARCHITECTURE.md)** - Core design principles and system architecture
- **[🚀 Server Setup](docs/wiki/02-SERVER-SETUP.md)** - A2A server implementation and configuration

### 🧠 LLM Integration
- **[🤖 LLM Providers](docs/wiki/04-LLM-PROVIDERS.md)** - Multi-provider setup (Ollama, Gemini, Claude)
- **[⚡ LLM Agent Core](docs/wiki/05-LLM-AGENT-CORE.md)** - Core agent implementation and lifecycle
- **[🧠 Cognitive Processing](docs/wiki/06-LLM-AGENT-COGNITIVE.md)** - Two-phase reasoning system
- **[🔧 Tool Handling](docs/wiki/07-LLM-AGENT-TOOLS.md)** - Intelligent tool calling and parameter inference

### 🛠️ Tool Integration
- **[🌐 MCP Integration](docs/wiki/08-MCP-INTEGRATION.md)** - Model Context Protocol implementation
- **[📋 Tool Context](docs/wiki/09-TOOL-CONTEXT.md)** - Conversation context and intelligent tool chaining

### ⚙️ Configuration
- **[📝 Configuration](docs/wiki/11-CONFIGURATION.md)** - Configuration system and external files
- **[💬 Prompt System](docs/wiki/12-PROMPT-SYSTEM.md)** - External prompt management
- **[📊 Logging](docs/wiki/13-LOGGING.md)** - Structured logging and observability

## 🎭 Example: Scientific Data Analysis Agent

The included example demonstrates a specialized agent for scientific data analysis:

```yaml
# config_data1_agent.yaml
agent:
  name: "Data1.bp File Agent"
  description: "Specialized agent for analyzing scientific data"
  agent_card: "agent_cards/scientific_data_analysis.yaml"
  prompts:
    tool_execution: "personas/adios/adios2_tool_execution.md"
    parser_synthesis: "personas/adios/adios2_parser_synthesis.md"

providers:
  ollama:
    base_url: "http://localhost:11434"
    model: "llama3.2:1b"
    temperature: 0.05  # Low temperature for reliable tool calling

mcp_servers:
  adios2:
    name: "adios2"
    command: ["uv", "--directory", "adios", "run", "adios-mcp"]
    enabled: true
```

### Example Interactions
```bash
# Discover available data
"What files are available for analysis?"

# Analyze variables
"What variables are in the dataset?"

# Get statistical information
"What are the min and max values for temperature?"

# Comparative analysis
"Compare pressure and temperature over time"
```

## 🔧 Project Structure

```
micro_agent/
├── client/              # A2A CLI client implementation
├── server/              # A2A server with LLM agent executor
├── shared/              # Shared components
│   ├── core/            # Core utilities and agent logic
│   │   ├── llm_agent.py        # Main LLM agent executor
│   │   ├── tool_context.py     # Intelligent tool context management
│   │   ├── config_loader.py    # Configuration management
│   │   └── agent_card_loader.py # External agent card system
│   ├── llm/             # LLM provider implementations
│   └── mcp/             # MCP integration
├── agent_cards/         # External agent card configurations
├── personas/            # External prompt files
├── adios/               # Example MCP server for ADIOS2 tools
└── docs/wiki/           # Comprehensive technical documentation
```

## 🎯 Key Design Principles

### 1. Domain Agnostic
- No hardcoded domain logic in shared components
- External configuration for all domain-specific behavior
- Generic tool patterns that work across different use cases

### 2. Fail Fast
- Clear error messages instead of silent fallbacks
- Configuration validation at startup
- Explicit failures when tools are misconfigured

### 3. External Configuration
- Agent cards define capabilities and skills
- Prompts stored in external markdown files
- MCP servers configured via YAML

### 4. Intelligent Context
- Conversation continuity across interactions
- Tool parameter inference from context
- Smart tool chaining and prerequisite detection

## 🏆 Production Features

### Reliability
- **Provider Failover**: Automatic switching between LLM providers
- **Health Monitoring**: Continuous health checks for all components
- **Error Recovery**: Graceful handling of failures with detailed diagnostics
- **Connection Management**: Robust MCP server connection handling

### Observability
- **Session-Based Logging**: Unique log files per server session
- **Structured Logging**: Categorized logs for different operation types
- **Performance Monitoring**: Tool execution timing and provider metrics
- **Debug Support**: Comprehensive logging for troubleshooting

### Scalability
- **Multi-Provider Support**: Mix local and cloud LLM providers
- **Multiple MCP Servers**: Support for diverse tool ecosystems
- **Configuration-Driven**: No code changes needed for new domains
- **Modular Design**: Easy to extend and customize

## 🎉 Who Should Use This

### For AI Researchers
- Study multi-turn reasoning and tool usage patterns
- Experiment with different cognitive architectures
- Research tool context and parameter inference

### For Developers
- Build production A2A agents for specific domains
- Integrate multiple tool systems via MCP
- Create intelligent conversational interfaces

### For Organizations
- Deploy reliable A2A agents with full observability
- Integrate existing tools via standardized protocols
- Scale agent capabilities across different domains

## 🤝 Contributing

This project serves as a comprehensive reference implementation. See the [technical documentation](docs/wiki/) for detailed implementation guides.

## 📄 License

MIT License - See LICENSE file for details

---

**Ready to build intelligent agents?** Start with the [Overview](docs/wiki/00-OVERVIEW.md) and dive into the [Architecture Guide](docs/wiki/01-DESIGN-ARCHITECTURE.md) to understand the core concepts.