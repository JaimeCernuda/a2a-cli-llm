# A2A (Agent2Agent) Protocol Documentation and Implementation Guide

## Table of Contents

1. [Protocol Overview](#protocol-overview)
2. [Core Architecture](#core-architecture)
3. [Installation and Setup](#installation-and-setup)
4. [SDK Structure](#sdk-structure)
5. [Client Implementation](#client-implementation)
6. [Server Implementation](#server-implementation)
7. [Authentication and Security](#authentication-and-security)
8. [Message Formats and Types](#message-formats-and-types)
9. [Task Management](#task-management)
10. [CLI Implementation Guidance](#cli-implementation-guidance)
11. [Code Examples](#code-examples)
12. [Best Practices](#best-practices)

## Protocol Overview

The A2A (Agent2Agent) protocol is a communication standard designed for agentic applications to interact with each other. It provides a standardized way for agents to:

- **Discover capabilities** through Agent Cards
- **Exchange messages** with structured content
- **Manage long-running tasks** with status tracking
- **Stream responses** for real-time interactions
- **Handle authentication** securely
- **Support multiple transports** (JSON-RPC, gRPC, HTTP)

### Key Concepts

- **Agent Card**: A discovery document that describes an agent's capabilities, skills, and interface
- **Message**: A structured communication unit between agents containing text, files, or data
- **Task**: A unit of work that can be tracked through its lifecycle
- **Skills**: Specific capabilities that an agent can perform
- **Parts**: Components of messages (text, file, or data segments)

## Core Architecture

### Transport Layers

The A2A protocol supports multiple transport mechanisms:

1. **JSON-RPC over HTTP** (Primary) - Standard HTTP with JSON-RPC 2.0
2. **gRPC** - High-performance binary protocol
3. **HTTP+JSON** - Direct HTTP REST-like interface

### Message Types

The protocol defines several core message types:

- `message/send` - Send a message to an agent
- `message/stream` - Send a message with streaming response
- `tasks/get` - Retrieve task information
- `tasks/cancel` - Cancel a running task
- `tasks/pushNotificationConfig/*` - Configure push notifications

## Installation and Setup

### Prerequisites

- **Python 3.10+** (Required)
- **uv** (Recommended) or **pip** for package management

### Installation

```bash
# Using uv (preferred)
uv add a2a-sdk

# Using pip
pip install a2a-sdk
```

### Key Dependencies

The SDK automatically installs these dependencies:

- **FastAPI** (≥0.115.2) - Web framework for servers
- **httpx** (≥0.28.1) - HTTP client
- **pydantic** (≥2.11.3) - Data validation
- **grpcio** (≥1.60) - gRPC support
- **protobuf** (5.29.5) - Protocol buffers
- **opentelemetry** - Observability

## SDK Structure

### Core Modules

```
src/a2a/
├── __init__.py               # Main SDK exports
├── types.py                  # Type definitions (generated from protocol spec)
├── client/                   # Client-side components
│   ├── __init__.py
│   ├── client.py            # Main A2A client
│   ├── grpc_client.py       # gRPC client variant
│   ├── helpers.py           # Utility functions
│   ├── auth/                # Authentication components
│   └── middleware.py        # Request interceptors
├── server/                   # Server-side components
│   ├── __init__.py
│   ├── apps/                # Application frameworks
│   │   └── jsonrpc/         # JSON-RPC server implementations
│   ├── request_handlers/    # Request processing
│   ├── tasks/               # Task management
│   └── events/              # Event system
├── auth/                    # Authentication framework
├── grpc/                    # Generated gRPC code
└── utils/                   # Utility functions
```

### Main Components

#### Client Components (`a2a.client`)

- **`A2AClient`** - Main HTTP client for agent communication
- **`A2ACardResolver`** - Fetches and validates agent cards
- **`A2AGrpcClient`** - gRPC client variant
- **`create_text_message_object`** - Helper for creating text messages
- **`AuthInterceptor`** - Authentication middleware
- **`CredentialService`** - Credential management

#### Server Components (`a2a.server`)

- **`A2AFastAPIApplication`** - FastAPI-based server
- **`A2AStarletteApplication`** - Starlette-based server
- **`RequestHandler`** - Base class for request processing
- **`TaskManager`** - Task lifecycle management
- **`EventQueue`** - Event-driven processing

## Client Implementation

### Basic Client Usage

```python
import asyncio
import httpx
from a2a.client import A2AClient, create_text_message_object
from a2a.types import SendMessageRequest, MessageSendParams

async def basic_client_example():
    async with httpx.AsyncClient() as http_client:
        # Option 1: Auto-discover via agent card
        a2a_client = await A2AClient.get_client_from_agent_card_url(
            httpx_client=http_client,
            base_url="http://localhost:8000"
        )
        
        # Option 2: Direct URL connection
        # a2a_client = A2AClient(httpx_client=http_client, url="http://localhost:8000/")
        
        # Create and send a message
        message = create_text_message_object(content="Hello, agent!")
        request = SendMessageRequest(
            id="req-123",
            params=MessageSendParams(message=message)
        )
        
        response = await a2a_client.send_message(request)
        print(f"Response: {response}")

if __name__ == "__main__":
    asyncio.run(basic_client_example())
```

### Streaming Client Usage

```python
from a2a.types import SendStreamingMessageRequest

async def streaming_client_example():
    async with httpx.AsyncClient() as http_client:
        a2a_client = A2AClient(httpx_client=http_client, url="http://localhost:8000/")
        
        message = create_text_message_object(content="Stream me results!")
        request = SendStreamingMessageRequest(
            id="stream-123",
            params=MessageSendParams(message=message)
        )
        
        # Stream responses
        async for response in a2a_client.send_message_streaming(request):
            print(f"Streaming response: {response}")
```

### Agent Card Resolution

```python
from a2a.client import A2ACardResolver

async def agent_card_example():
    async with httpx.AsyncClient() as http_client:
        resolver = A2ACardResolver(
            httpx_client=http_client,
            base_url="http://localhost:8000",
            agent_card_path="/.well-known/agent.json"
        )
        
        # Fetch public agent card
        agent_card = await resolver.get_agent_card()
        print(f"Agent: {agent_card.name}")
        print(f"Skills: {[skill.name for skill in agent_card.skills]}")
        
        # Use agent card to create client
        client = A2AClient(httpx_client=http_client, agent_card=agent_card)
```

## Server Implementation

### Basic Server Setup

```python
from a2a.server.apps.jsonrpc.fastapi_app import A2AFastAPIApplication
from a2a.server.request_handlers.default_request_handler import DefaultRequestHandler
from a2a.types import (
    AgentCard, AgentCapabilities, AgentSkill, 
    MessageSendParams, SendMessageSuccessResponse, Task, TaskStatus, TaskState
)

class MyAgentHandler(DefaultRequestHandler):
    """Custom handler for processing A2A requests."""
    
    async def on_message_send(
        self, 
        params: MessageSendParams, 
        context=None
    ) -> SendMessageSuccessResponse:
        """Handle incoming messages."""
        
        # Extract message content
        message = params.message
        text_content = ""
        for part in message.parts:
            if hasattr(part.root, 'text'):
                text_content += part.root.text
        
        print(f"Received message: {text_content}")
        
        # Process the message and create response
        response_message = create_text_message_object(
            role="agent",
            content=f"Hello! You said: {text_content}"
        )
        
        # Create task (simplified)
        task = Task(
            id="task-123",
            contextId="context-123",
            status=TaskStatus(
                state=TaskState.completed,
                message=response_message
            )
        )
        
        return SendMessageSuccessResponse(
            id="response-123",
            result=task
        )

# Define agent capabilities
agent_card = AgentCard(
    name="My CLI Agent",
    description="A sample A2A agent for CLI interactions",
    url="http://localhost:8000/",
    version="1.0.0",
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    capabilities=AgentCapabilities(
        streaming=True,
        pushNotifications=False
    ),
    skills=[
        AgentSkill(
            id="hello_world",
            name="Hello World",
            description="Responds with a greeting",
            tags=["greeting", "basic"],
            examples=["hello", "hi", "greetings"]
        )
    ]
)

# Create and build the server
handler = MyAgentHandler()
app_builder = A2AFastAPIApplication(agent_card, handler)
app = app_builder.build()

# Run with: uvicorn main:app --host 0.0.0.0 --port 8000
```

### Advanced Server with Streaming

```python
from a2a.types import SendStreamingMessageSuccessResponse, TaskStatusUpdateEvent

class StreamingAgentHandler(DefaultRequestHandler):
    """Handler that supports streaming responses."""
    
    async def on_message_stream(
        self, 
        params: MessageSendParams, 
        context=None
    ) -> AsyncGenerator[SendStreamingMessageSuccessResponse, None]:
        """Handle streaming message requests."""
        
        # Initial response
        initial_task = Task(
            id="stream-task-123",
            contextId="stream-context-123",
            status=TaskStatus(state=TaskState.working)
        )
        
        yield SendStreamingMessageSuccessResponse(
            id="stream-response-1",
            result=initial_task
        )
        
        # Stream updates
        for i in range(3):
            await asyncio.sleep(1)  # Simulate work
            
            update_event = TaskStatusUpdateEvent(
                taskId="stream-task-123",
                contextId="stream-context-123",
                status=TaskStatus(
                    state=TaskState.working,
                    message=create_text_message_object(
                        role="agent",
                        content=f"Processing step {i+1}..."
                    )
                ),
                final=False
            )
            
            yield SendStreamingMessageSuccessResponse(
                id=f"stream-response-{i+2}",
                result=update_event
            )
        
        # Final response
        final_event = TaskStatusUpdateEvent(
            taskId="stream-task-123",
            contextId="stream-context-123",
            status=TaskStatus(
                state=TaskState.completed,
                message=create_text_message_object(
                    role="agent",
                    content="Task completed successfully!"
                )
            ),
            final=True
        )
        
        yield SendStreamingMessageSuccessResponse(
            id="stream-response-final",
            result=final_event
        )
```

## Authentication and Security

### Security Schemes

The A2A protocol supports multiple authentication methods:

- **API Key** - Header, query parameter, or cookie-based
- **HTTP Auth** - Basic, Bearer, or custom schemes
- **OAuth2** - Full OAuth2 flow support
- **OpenID Connect** - OIDC integration

### Client-Side Authentication

```python
from a2a.client.auth import AuthInterceptor, InMemoryContextCredentialStore
from a2a.client.middleware import ClientCallContext

# Set up credential store
credential_store = InMemoryContextCredentialStore()
await credential_store.set_credentials(
    session_id="session-123",
    security_scheme_name="api_key",
    credential="sk-1234567890abcdef"
)

# Create auth interceptor
auth_interceptor = AuthInterceptor(credential_store)

# Create client with authentication
client = A2AClient(
    httpx_client=http_client,
    url="http://localhost:8000/",
    interceptors=[auth_interceptor]
)

# Set context for requests
context = ClientCallContext(state={"sessionId": "session-123"})
```

### Server-Side Authentication

```python
from a2a.types import SecurityScheme, APIKeySecurityScheme

# Define security schemes in agent card
agent_card = AgentCard(
    name="Secure Agent",
    # ... other fields ...
    securitySchemes={
        "api_key": SecurityScheme(
            root=APIKeySecurityScheme(
                type="apiKey",
                name="X-API-Key",
                in_="header",
                description="API key for authentication"
            )
        )
    },
    security=[{"api_key": []}]  # Require API key for all operations
)
```

## Message Formats and Types

### Message Structure

```python
from a2a.types import Message, Part, TextPart, FilePart, DataPart, Role

# Text message
text_message = Message(
    messageId="msg-123",
    role=Role.user,
    parts=[
        Part(root=TextPart(text="Hello, agent!"))
    ]
)

# File message
file_message = Message(
    messageId="msg-124",
    role=Role.user,
    parts=[
        Part(root=FilePart(
            file=FileWithBytes(
                bytes="base64-encoded-content",
                name="document.pdf",
                mimeType="application/pdf"
            )
        ))
    ]
)

# Data message
data_message = Message(
    messageId="msg-125",
    role=Role.user,
    parts=[
        Part(root=DataPart(
            data={"key": "value", "nested": {"field": 123}}
        ))
    ]
)
```

### Complex Messages

```python
# Multi-part message
complex_message = Message(
    messageId="msg-126",
    role=Role.user,
    parts=[
        Part(root=TextPart(text="Please analyze this document:")),
        Part(root=FilePart(
            file=FileWithUri(
                uri="https://example.com/document.pdf",
                name="analysis_target.pdf",
                mimeType="application/pdf"
            )
        )),
        Part(root=DataPart(
            data={"analysis_type": "sentiment", "detailed": True}
        ))
    ],
    referenceTaskIds=["previous-task-123"]  # Reference related tasks
)
```

## Task Management

### Task Lifecycle

Tasks in A2A follow this lifecycle:

1. **submitted** - Task has been received
2. **working** - Task is being processed
3. **input-required** - Task needs additional input
4. **completed** - Task finished successfully
5. **failed** - Task encountered an error
6. **canceled** - Task was canceled
7. **rejected** - Task was rejected
8. **auth-required** - Authentication needed

### Task Operations

```python
from a2a.types import GetTaskRequest, TaskQueryParams, CancelTaskRequest, TaskIdParams

# Get task details
get_task_request = GetTaskRequest(
    id="req-123",
    params=TaskQueryParams(
        id="task-123",
        historyLength=10  # Get last 10 messages
    )
)

task_response = await client.get_task(get_task_request)

# Cancel task
cancel_request = CancelTaskRequest(
    id="req-124",
    params=TaskIdParams(id="task-123")
)

cancel_response = await client.cancel_task(cancel_request)
```

### Push Notifications

```python
from a2a.types import (
    SetTaskPushNotificationConfigRequest,
    TaskPushNotificationConfig,
    PushNotificationConfig
)

# Configure push notifications
push_config = PushNotificationConfig(
    url="https://my-app.com/webhook",
    token="webhook-token-123"
)

push_request = SetTaskPushNotificationConfigRequest(
    id="req-125",
    params=TaskPushNotificationConfig(
        taskId="task-123",
        pushNotificationConfig=push_config
    )
)

await client.set_task_push_notification_config(push_request)
```

## CLI Implementation Guidance

### CLI Client Architecture

```python
import argparse
import asyncio
import httpx
from a2a.client import A2AClient, create_text_message_object
from a2a.types import SendMessageRequest, MessageSendParams

class A2ACLIClient:
    """CLI client for A2A agents."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = None
    
    async def __aenter__(self):
        self.http_client = httpx.AsyncClient()
        self.client = await A2AClient.get_client_from_agent_card_url(
            httpx_client=self.http_client,
            base_url=self.base_url
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.http_client.aclose()
    
    async def send_message(self, text: str, stream: bool = False):
        """Send a message to the agent."""
        message = create_text_message_object(content=text)
        
        if stream:
            request = SendStreamingMessageRequest(
                id=f"cli-{uuid4()}",
                params=MessageSendParams(message=message)
            )
            async for response in self.client.send_message_streaming(request):
                yield response
        else:
            request = SendMessageRequest(
                id=f"cli-{uuid4()}",
                params=MessageSendParams(message=message)
            )
            response = await self.client.send_message(request)
            return response

async def main():
    parser = argparse.ArgumentParser(description="A2A CLI Client")
    parser.add_argument("--url", required=True, help="Agent base URL")
    parser.add_argument("--message", required=True, help="Message to send")
    parser.add_argument("--stream", action="store_true", help="Use streaming")
    
    args = parser.parse_args()
    
    async with A2ACLIClient(args.url) as client:
        if args.stream:
            async for response in client.send_message(args.message, stream=True):
                print(f"Stream: {response}")
        else:
            response = await client.send_message(args.message)
            print(f"Response: {response}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Interactive CLI

```python
import readline
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

class InteractiveA2ACLI:
    """Interactive CLI for A2A agents."""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.commands = WordCompleter([
            'send', 'stream', 'tasks', 'help', 'exit'
        ])
    
    async def run(self):
        """Run the interactive CLI."""
        async with A2ACLIClient(self.base_url) as client:
            print(f"Connected to A2A agent at {self.base_url}")
            print("Type 'help' for available commands")
            
            while True:
                try:
                    user_input = await prompt(
                        "a2a> ",
                        completer=self.commands,
                        async_=True
                    )
                    
                    if user_input.lower() in ['exit', 'quit']:
                        break
                    elif user_input.lower() == 'help':
                        self.show_help()
                    elif user_input.startswith('send '):
                        message = user_input[5:]
                        response = await client.send_message(message)
                        print(f"Response: {response}")
                    elif user_input.startswith('stream '):
                        message = user_input[7:]
                        async for response in client.send_message(message, stream=True):
                            print(f"Stream: {response}")
                    else:
                        print("Unknown command. Type 'help' for available commands.")
                
                except KeyboardInterrupt:
                    print("\nExiting...")
                    break
                except Exception as e:
                    print(f"Error: {e}")
    
    def show_help(self):
        """Show available commands."""
        print("""
Available commands:
  send <message>    - Send a message to the agent
  stream <message>  - Send a message with streaming response
  tasks             - List active tasks
  help              - Show this help message
  exit              - Exit the CLI
        """)

# Usage: python cli.py --interactive --url http://localhost:8000
```

## Code Examples

### File Upload Example

```python
import base64
from a2a.types import FilePart, FileWithBytes

async def upload_file_example():
    # Read file content
    with open("document.pdf", "rb") as f:
        file_content = f.read()
    
    # Create file part
    file_part = Part(root=FilePart(
        file=FileWithBytes(
            bytes=base64.b64encode(file_content).decode('utf-8'),
            name="document.pdf",
            mimeType="application/pdf"
        )
    ))
    
    # Create message with file
    message = Message(
        messageId=str(uuid4()),
        role=Role.user,
        parts=[
            Part(root=TextPart(text="Please analyze this document:")),
            file_part
        ]
    )
    
    # Send message
    request = SendMessageRequest(
        id=str(uuid4()),
        params=MessageSendParams(message=message)
    )
    
    response = await client.send_message(request)
    return response
```

### Error Handling Example

```python
from a2a.client.errors import A2AClientError, A2AClientHTTPError, A2AClientJSONError

async def robust_client_example():
    try:
        async with httpx.AsyncClient() as http_client:
            client = A2AClient(httpx_client=http_client, url="http://localhost:8000/")
            
            message = create_text_message_object(content="Hello!")
            request = SendMessageRequest(
                id="req-123",
                params=MessageSendParams(message=message)
            )
            
            response = await client.send_message(request)
            return response
    
    except A2AClientHTTPError as e:
        print(f"HTTP Error {e.status_code}: {e.message}")
        if e.status_code == 401:
            print("Authentication required")
        elif e.status_code == 404:
            print("Agent not found")
    
    except A2AClientJSONError as e:
        print(f"JSON Error: {e.message}")
        print("Invalid response format from agent")
    
    except A2AClientError as e:
        print(f"A2A Client Error: {e}")
    
    except Exception as e:
        print(f"Unexpected error: {e}")
```

## Best Practices

### Client Best Practices

1. **Connection Management**
   - Always use async context managers for HTTP clients
   - Reuse HTTP clients when possible
   - Handle connection timeouts gracefully

2. **Error Handling**
   - Catch specific A2A exceptions
   - Implement retry logic for transient failures
   - Log errors with sufficient context

3. **Message Design**
   - Use appropriate message parts (text, file, data)
   - Include relevant metadata
   - Reference related tasks when applicable

4. **Authentication**
   - Store credentials securely
   - Use appropriate security schemes
   - Handle token refresh automatically

### Server Best Practices

1. **Handler Implementation**
   - Inherit from appropriate base handlers
   - Implement proper error handling
   - Use async/await consistently

2. **Task Management**
   - Provide meaningful task IDs
   - Update task status appropriately
   - Handle task cancellation gracefully

3. **Performance**
   - Use streaming for long-running operations
   - Implement proper request queuing
   - Monitor resource usage

4. **Security**
   - Validate all inputs
   - Implement proper authentication
   - Use HTTPS in production

### CLI-Specific Best Practices

1. **User Experience**
   - Provide clear help messages
   - Support command completion
   - Handle interrupts gracefully

2. **Configuration**
   - Support configuration files
   - Allow environment variable overrides
   - Provide sensible defaults

3. **Output Formatting**
   - Use structured output formats (JSON, YAML)
   - Support different verbosity levels
   - Color-code output when appropriate

4. **Testing**
   - Mock external dependencies
   - Test error conditions
   - Validate CLI argument parsing

## Dependencies and Version Compatibility

### Core Dependencies

- **Python**: 3.10+
- **FastAPI**: ≥0.115.2
- **httpx**: ≥0.28.1
- **pydantic**: ≥2.11.3
- **grpcio**: ≥1.60
- **protobuf**: 5.29.5

### Development Dependencies

- **pytest**: ≥8.3.5
- **pytest-asyncio**: ≥0.26.0
- **mypy**: ≥1.15.0
- **ruff**: ≥0.11.6

### External Resources

- **A2A Samples**: https://github.com/a2aproject/a2a-samples
- **Protocol Documentation**: https://a2aproject.github.io/A2A/
- **Python SDK Docs**: https://a2aproject.github.io/A2A/sdk/python/

## Conclusion

The A2A protocol provides a robust framework for agent-to-agent communication with comprehensive support for various interaction patterns. The Python SDK offers both client and server implementations with strong type safety, authentication support, and production-ready features.

For CLI applications, the SDK provides all necessary building blocks while allowing flexibility in implementation approach. Whether building simple command-line tools or complex interactive applications, the A2A protocol and Python SDK provide the foundation for reliable agent communication.

The protocol's support for multiple transport methods, streaming responses, and comprehensive task management makes it suitable for a wide range of use cases, from simple request-response interactions to complex multi-step workflows.