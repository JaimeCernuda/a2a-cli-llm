# A2A CLI Test Commands

This file contains example commands for testing the A2A CLI application.

## Starting the Server

```bash
# Basic server start
uv run server

# Server with custom settings
uv run server --host 0.0.0.0 --port 9000 --log-level debug

# Server with auto-reload for development
uv run server --reload
```

## Client Commands

### Basic Message Sending
```bash
# Send a simple message
uv run client send --agent http://localhost:8000 --message "Hello, agent!"

# Send a greeting
uv run client send --agent http://localhost:8000 --message "Hi there!"

# Request help
uv run client send --agent http://localhost:8000 --message "help"

# Ask for time
uv run client send --agent http://localhost:8000 --message "What time is it?"

# Echo test
uv run client send --agent http://localhost:8000 --message "echo This is a test"
```

### File Upload
```bash
# Send a message with file attachment
uv run client send --agent http://localhost:8000 --message "Please analyze this file" --file examples/sample.txt

# Send without streaming
uv run client send --agent http://localhost:8000 --message "Process this document" --file examples/sample.txt --no-streaming
```

### Agent Information
```bash
# Get agent information
uv run client info --agent http://localhost:8000
```

### Interactive Mode
```bash
# Start interactive conversation
uv run client interactive --agent http://localhost:8000
```

## Testing

```bash
# Run all tests
uv run test

# Or run pytest directly
uv run pytest -v
```

## Example Interactive Session

When running `uv run client interactive --agent http://localhost:8000`:

```
You: hello
Agent: Hello! I received your greeting: 'hello'. How can I help you today?

You: help
Agent: I'm a simple CLI agent that can help with:
        
• Greetings (hello, hi, hey)
• Help information (help)
• Time/date requests (time, date)
• Echo messages (echo <message>)
• Agent information (info, about)
• File analysis (when you send files)
• General conversation

Try sending me a message or ask for help with any of these topics!

You: what time is it
Agent: The current date and time is: 2024-01-15 14:30:25

You: echo Hello World
Agent: Echo: Hello World

You: quit
Goodbye!
```