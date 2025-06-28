# ADIOS MCP Server

A read-only Model Context Protocol (MCP) server for ADIOS datasets, enabling LLMS to query scientific simulation and real-time data.

## Key Features

- **Read-Only ADIOS Access**  
  Uses the ADIOS2 Python API to list files, inspect variables, and retrieve data slices or full arrays without modifying the source.

- **Standardized MCP Interface**  
  Exposes data-access tools via the MCP JSON-RPC protocol.

- **Local LLM Integration**  
  Connects to local language models through ollama, allowing natural-language queries and inference without internet or cloud dependencies.

- **Cross-Platform**  
  Pure Python implementation runs on Linux, macOS, and Windows. Package installable via `pip` or Spack.

## Architecture

 ![](https://github.com/iowarp/scientific-mcps/blob/main/Adios/assets/architecture.png)

## Capabilities

 1. list_bp5: List all the bp5 files in a directory. 

 2. inspect_variables: Inspect all variables in a BP5 file (type, shape, available steps).

 3. inspect_attributes: Read global or variable-specific attributes from a BP5 file. 

 4. read_variable_at_step: Read a named variable at a specific step from a BP5 file.

 5. read_bp5: Reads all the variables/data and their steps from a BP5 file.

 6. get_min_max: Get minimum and maximum of a variable in a BP5 file.

 7. add_variables: Sum two variables in a BP5 file, either globally or at specific steps.

---

## Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- Linux/macOS environment (for optimal compatibility)

## Setup
**Run the Mcp Server directly:**

   ```bash
   uv run adios-mcp
   ```
   
   This will create a `.venv/` folder, install all required packages, and run the server directly.
--- 

## Running the Server with different types of Clients:

### Running the Server with the WARP Client
To interact with the ADIOS MCP server, use the main `wrp.py` client. You will need to configure it to point to the ADIOS server.

1.  **Configure:** Ensure that `Adios` is listed in the `MCP` section of your chosen configuration file (e.g., in `bin/confs/Gemini.yaml` or `bin/confs/Ollama.yaml`).
    ```yaml
    # In bin/confs/Gemini.yaml
    MCP:
      - Adios
      # - Jarvis
      # - HDF5
    ```

2.  **Run:** Start the client from the repository root with your desired configuration:
    ```bash
    # Example using the Gemini configuration 
    
    python3 bin/wrp.py --conf=bin/confs/Gemini.yaml
    ```
    For quick setup with Gemini, see our [Quick Start Guide](docs/basic_install.md).
    
    
    For detailed setup with local LLMs and other providers, see the [Complete Installation Guide](../bin/docs/Installation.md).

### Running the Server on Claude Command Line Interface Tool.

1. Install the Claude Code using NPM,
Install [NodeJS 18+](https://nodejs.org/en/download), then run:

```bash
npm install -g @anthropic-ai/claude-code
```

2. Running the server:
```bash
claude add mcp adios -- uv --directory ~/scientific-mcps/Adios run adios-mcp
```

### Running the Server on open source LLM client (Claude, Copilot, etc.)

**Put the following in settings.json of any open source LLMs like Claude or Microsoft Co-pilot:**

```bash
"adios-mcp": {
    "command": "uv",
    "args": [
        "--directory",
        "path/to/directory/src/adiosmcp/",
        "run",
        "server.py"
    ]
}
```

---
## Few Examples

**Note: Mention Absolute path of all the files you want to have operations ex. Read file at Adios/data/data1.bp**

1. Read variables/data at specific step in a Bp5 File 

 ![](https://github.com/iowarp/scientific-mcps/blob/main/Adios/assets/read_steps.png)

2. Inspect the variables in a BP5 file (type, shape, available steps)

 ![](https://github.com/iowarp/scientific-mcps/blob/main/Adios/assets/steps.png)

3. Inspect and read the attributes of a specific variable

 ![](https://github.com/iowarp/scientific-mcps/blob/main/Adios/assets/attributes.png)

**Detailed demonstration of use cases are available at [Examples](https://github.com/sohamvsonar/scientific-mcps/tree/main/Adios/docs/example_uses.md).**

## Project Structure
```text
Adios/
├── pyproject.toml           # Project metadata & dependencies
├── README.md                # Project documentation
├── assets/                  # Images and other assets
├── data/                    # Sample data directory
├── docs/                    # Additional documentation
│     ├── adios_setup        # Detailed guide on installing the Adios2
│     └── example_uses       # Example use cases with prompt, answers and pictures
├── pyproject.toml           # Project metadata & dependencies
├── src/                     # Source code directory
│   └── adiosmcp/
│       ├── __init__.py      # Package init
│       ├── server.py        # The MCP server
│       ├── mcp_handlers.py  # MCP methods
│       └── capabilities/
│           ├── __init__.py
│           ├── bp5_add.py                    # Add variables functionality
│           ├── bp5_attributes.py             # Inspect attributes functionality
│           ├── bp5_inspect_variables.py      # Inspect variables functionality
│           ├── bp5_list.py                   # List BP5 files functionality
│           ├── bp5_minmax.py                 # Get min/max functionality
│           ├── bp5_read_all_variables.py     # Read all variables functionality
│           ├── bp5_read_variable_at_step.py  # Read variable at step functionality
├── uv.lock                  # Dependency lock file
```