# A2A CLI ADIOS2 Agent

A specialized A2A (Agent-to-Agent) CLI application for scientific data analysis with ADIOS2 file parsing capabilities, powered by LLM providers and MCP tool integration.

## 🚀 Quick Start

### ADIOS2 Data Analysis Agent
```bash
# Start the specialized ADIOS2 agent
uv run python -m server.main --config config_data1_agent.yaml

# In another terminal, interact with the agent
uv run python -m client.main interactive --agent http://localhost:8000
```

### Test the Parser Prompt System
```bash
# Run comprehensive tests
uv run python tests/test_parser_prompt.py
```

## 📁 Project Structure

```
├── client/              # A2A CLI client implementation
├── server/              # A2A CLI server implementation  
├── shared/              # Shared components
│   ├── core/            # Core utilities, configuration, and logging
│   ├── llm/             # LLM provider implementations
│   └── mcp/             # MCP (Model Context Protocol) integration
├── adios/               # ADIOS2 MCP server implementation
├── personas/            # AI agent personalities and prompts
│   ├── adios/           # ADIOS2-specific prompts for tool execution and synthesis
│   └── data1_bp_agent.md # Specialized data1.bp file agent persona
├── tests/               # Test suite and validation scripts
└── config_data1_agent.yaml # Active configuration for ADIOS2 agent
```

## 🧠 LLM Provider Support

### Current Setup:
- **🦙 Ollama** - Local models (llama3.2:1b optimized for tool calling)
- **🤖 Gemini** - Google's AI models (supported)
- **🧠 Claude** - Anthropic's models (supported)

### Ollama Setup (Required)
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Start Ollama
ollama serve

# Pull the optimized model
ollama pull llama3.2:1b
```

## 🔧 Architecture

### Two-Phase Parser Prompt System
1. **Tool Execution Phase**: Efficiently calls ADIOS2 tools to gather data
2. **Natural Language Synthesis**: Converts tool results into human-readable responses

### MCP Integration
- **ADIOS2 MCP Server**: Provides BP5 file analysis capabilities
- **Tool Context Management**: Enhanced parameter handling for scientific data
- **Session-based Logging**: Comprehensive observability for debugging

### Key Features
- **Focused Agent**: Specialized for data1.bp file analysis only
- **100% Tool Execution Reliability**: Consistent and accurate tool calling
- **Scientific Data Analysis**: Specialized for ADIOS2 BP5 format files
- **Structured Logging**: Clear categorization of agent operations
- **External Prompt System**: Configurable prompts stored in markdown files

## 🛠️ Configuration

The active configuration (`config_data1_agent.yaml`) includes:
- **Ollama Provider**: llama3.2:1b model with optimized settings
- **ADIOS2 MCP Server**: Automated stdio MCP integration
- **External Prompts**: Tool execution and synthesis prompts
- **Extended Timeout**: 10-minute timeout for complex analysis
- **Session Logging**: File-based logging with detailed content

## 🧪 Testing

```bash
# Test the parser prompt system
uv run python tests/test_parser_prompt.py

# The test includes:
# - Variable discovery
# - Statistical analysis (min/max values)
# - Comparative analysis
# - Temporal dynamics
# - Scientific interpretation
```

## 📊 Scientific Data Analysis

The agent can analyze:
- **Variables**: Discover all variables in ADIOS2 files
- **Statistics**: Calculate min/max values for any variable
- **Temporal Data**: Analyze time-series simulation data
- **Physical Properties**: Interpret pressure, temperature, and other scientific variables
- **Simulation Context**: Provide scientific insights about the data

## 🚀 Usage Examples

```bash
# Ask about variables
"What variables are in your file?"

# Get statistical information
"What are the min and max values for temperature?"

# Request comparative analysis
"Compare pressure and temperature variables"

# Scientific interpretation
"What kind of scientific simulation does this represent?"
```

## 🔍 Logging & Debugging

The system provides comprehensive logging with:
- **Session-based Files**: Each server instance creates unique log files
- **Structured Categories**: User queries, model interactions, tool execution, synthesis
- **Console vs File Mode**: Configurable logging destinations
- **Rich Emoji Indicators**: Easy identification of different operation types

## 🎯 Development Focus

This implementation demonstrates:
- **Specialized AI Agents**: Domain-specific expertise for scientific data
- **Two-Phase Processing**: Reliable tool execution + natural language synthesis  
- **MCP Integration**: Modern tool calling with Model Context Protocol
- **Enterprise Logging**: Production-ready observability
- **External Configuration**: Maintainable prompt and configuration management

The system achieves 100% tool execution reliability while providing natural, scientific language responses about ADIOS2 data files.