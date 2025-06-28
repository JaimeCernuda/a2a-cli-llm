# Google A2A (Agent-to-Agent) Protocol - Comprehensive Guide

## Table of Contents
1. [Protocol Overview](#protocol-overview)
2. [Core Concepts](#core-concepts)
3. [Python SDK Structure](#python-sdk-structure)
4. [Advanced Features](#advanced-features)
5. [Implementation Guide](#implementation-guide)
6. [CLI Development Focus](#cli-development-focus)
7. [Multi-Agent Orchestration](#multi-agent-orchestration)
8. [Framework Integrations](#framework-integrations)
9. [Installation and Setup](#installation-and-setup)
10. [Code Examples](#code-examples)
11. [Best Practices](#best-practices)
12. [Security Considerations](#security-considerations)
13. [Resources](#resources)

## Protocol Overview

The Agent-to-Agent (A2A) protocol is Google's standardized communication framework that enables AI agents to discover, communicate, and collaborate with each other using a JSON-RPC based protocol. It provides a uniform way for agents to interact regardless of their underlying implementation.

### Key Features
- **Standardized Communication**: JSON-RPC based protocol for consistent agent interaction
- **Agent Discovery**: Agents expose capabilities through standardized metadata (AgentCard)
- **Streaming Support**: Real-time interactions with streaming responses
- **Task Management**: Comprehensive task lifecycle management
- **Platform Independence**: Framework-agnostic agent communication
- **Security**: Built-in authentication and authorization mechanisms
- **MCP Integration**: Model Context Protocol for tool and data source management
- **Multi-Provider Support**: Works with various LLM providers (Google AI, Azure, OpenAI, etc.)

### Why Use A2A?

**Use A2A for Multi-Agent Systems When:**
- Building complex multi-agent systems requiring coordination
- Agents need independent development, deployment, and scaling
- Integrating agents from different teams or frameworks
- Dynamic agent discovery and composition is needed
- Building platforms where agents can be added/removed dynamically
- Enabling third-party agent integration
- Cross-language agent communication is required

**Use Direct Framework Integration When:**
- All agents are tightly coupled and always used together
- Single framework solution is sufficient
- Performance of in-process communication is critical
- No distributed deployment requirements

## Core Concepts

### AgentCard
The AgentCard is the metadata that describes an agent's capabilities, exposed via the `/.well-known/agent.json` endpoint.

```python
from a2a.types import AgentCard, AgentCapabilities, AgentSkill

agent_card = AgentCard(
    name="My Agent",
    description="Description of what this agent does",
    url="http://localhost:8000/",
    version="1.0.0",
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    capabilities=AgentCapabilities(streaming=True, pushNotifications=True),
    skills=[
        AgentSkill(
            id="skill_id",
            name="Skill Name",
            description="What this skill does",
            tags=["tag1", "tag2"],
            examples=["example 1", "example 2"]
        )
    ]
)
```

### Task States
Tasks progress through defined states:
- `SUBMITTED`: Task received but not yet started
- `WORKING`: Task is being processed
- `INPUT_REQUIRED`: Task needs additional input from user
- `COMPLETED`: Task finished successfully
- `CANCELED`: Task was canceled
- `FAILED`: Task failed with error
- `UNKNOWN`: Task state unknown

### Message Structure
Messages contain parts that can be text, files, or structured data:

```python
from a2a.types import Message, TextPart, FilePart, DataPart

message = Message(
    role="user",  # or "agent"
    parts=[
        TextPart(text="Hello, agent!"),
        # Optional file or data parts
    ]
)
```

### Communication Patterns

#### 1. Direct Task Execution
```python
# Send a task and wait for completion
response = await client.send_task(payload)
```

#### 2. Streaming Communication
```python
# Stream responses for real-time interaction
async for event in client.send_task_streaming(payload):
    # Process streaming events
    pass
```

#### 3. Task Management
```python
# Get task status
task = await client.get_task({"id": task_id})

# Cancel task
await client.cancel_task({"id": task_id})
```

## Python SDK Structure

### Core Components

#### 1. Types (`a2a.types` / `common.types`)
- **Message Components**: `Message`, `TextPart`, `FilePart`, `DataPart`
- **Task Management**: `Task`, `TaskState`, `TaskStatus`, `Artifact`
- **Agent Metadata**: `AgentCard`, `AgentSkill`, `AgentCapabilities`
- **JSON-RPC**: `JSONRPCRequest`, `JSONRPCResponse`, `JSONRPCError`
- **Streaming Events**: `TaskStatusUpdateEvent`, `TaskArtifactUpdateEvent`

#### 2. Client (`a2a.client` / `common.client`)
The A2AClient handles communication with remote agents:

```python
from a2a.client import A2AClient
from a2a.types import AgentCard

# Initialize client
client = A2AClient(agent_card=card)  # or url=agent_url

# Send task
response = await client.send_task(payload)

# Stream task
async for event in client.send_task_streaming(payload):
    process_event(event)
```

#### 3. Server (`a2a.server` / `common.server`)
The A2AServer handles incoming requests and manages agent execution:

```python
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore

# Create server
server = A2AStarletteApplication(
    agent_card=agent_card,
    http_handler=request_handler
)
```

#### 4. Agent Execution
Implement the `AgentExecutor` interface:

```python
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue

class MyAgentExecutor(AgentExecutor):
    async def execute(self, context: RequestContext, event_queue: EventQueue):
        # Process the request
        result = await self.process_request(context.get_user_input())
        
        # Send response
        await event_queue.enqueue_event(
            new_agent_text_message(result)
        )
    
    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        # Handle cancellation
        pass
```

## Advanced Features

### 1. MCP (Model Context Protocol) Integration

MCP enables agents to discover and use external tools and data sources dynamically.

#### MCP Server Integration
```python
# From a2a_mcp sample
class MCPToolManager:
    async def initialize(self) -> None:
        self._connection = ServerConnection(self.config)
        await self._connection.connect()
        
        # Dynamic tool loading
        self._functions_dict = {
            tool_name: self._make_tool_func(tool_name)
            for tool_name in self._tools_cache.keys()
        }

    def _make_tool_func(self, tool_name: str):
        async def async_tool_func(**kwargs):
            result = await self._connection.execute_tool(tool_name, kwargs)
            return result
        return async_tool_func
```

#### Agent Discovery with Embeddings
```python
# Semantic agent matching using embeddings
def find_agent(query: str) -> str:
    query_embedding = genai.embed_content(
        model=MODEL, content=query, task_type='retrieval_query'
    )
    dot_products = np.dot(
        np.stack(df['card_embeddings']), query_embedding['embedding']
    )
    best_match_index = np.argmax(dot_products)
    return df.iloc[best_match_index]['agent_card']
```

### 2. Multi-Provider LLM Support

#### Azure AI Foundry Integration
```python
# Azure AI integration with MCP
from azure.ai.agents import AgentClient

class AzureFoundryAgent:
    def __init__(self, endpoint: str, api_key: str):
        self.client = AgentClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(api_key)
        )
        self.mcp_manager = MCPToolManager()
    
    async def process_message(self, message: str):
        # Use Azure AI with MCP tools
        response = await self.client.create_message(
            assistant_id=self.assistant_id,
            content=message,
            tools=await self.mcp_manager.get_tools()
        )
        return response
```

#### Google AI Integration with ADK
```python
# From telemetry sample
from google.adk.agents import Agent
from google.adk.tools import google_search

agent = Agent(
    model="gemini-2.5-pro",
    name="research_agent",
    instruction="You are a research assistant...",
    tools=[google_search]
)

# ADK integration with A2A
class ADKAgentExecutor(AgentExecutor):
    def __init__(self, agent):
        self.runner = Runner(
            app_name=agent.name,
            agent=agent,
            artifact_service=InMemoryArtifactService(),
            session_service=InMemorySessionService(),
            memory_service=InMemoryMemoryService(),
        )
    
    async def execute(self, context: RequestContext, event_queue: EventQueue):
        session = await self.runner.session_service.create_session(
            app_name=self.agent.name,
            user_id="a2a_user",
            state={},
            session_id=context.task_id,
        )
        
        async for event in self.runner.run_async(
            user_id="a2a_user",
            session_id=session.id,
            new_message=content
        ):
            # Process ADK events and convert to A2A events
            await self.handle_adk_event(event, event_queue)
```

### 3. Authentication and Security

#### OAuth2 Integration
```python
# From headless_agent_auth sample
class OAuth2Middleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return self._unauthorized('Missing or invalid authorization header', request)
        
        access_token = auth_header.split('Bearer ')[1]
        
        # Verify token with Auth0
        payload = await self.api_client.verify_access_token(access_token=access_token)
        
        # Scope validation
        scopes = payload.get('scope', '').split()
        missing_scopes = [s for s in self.a2a_auth['required_scopes'] if s not in scopes]
        if missing_scopes:
            return self._forbidden(f'Missing required scopes: {missing_scopes}', request)
        
        request.state.user = payload
        return await call_next(request)
```

### 4. Push Notifications and Callbacks

#### Async Notification Handling
```python
# From CLI sample
class PushNotificationListener:
    def __init__(self, host, port, notification_receiver_auth):
        self.loop = asyncio.new_event_loop()
        self.thread = threading.Thread(
            target=lambda loop: loop.run_forever(), 
            args=(self.loop,)
        )
        self.thread.daemon = True
        self.thread.start()

    async def handle_notification(self, request: Request):
        if not await self.notification_receiver_auth.verify_push_notification(request):
            return JSONResponse({'error': 'Unauthorized'}, status_code=401)
        
        # Process notification
        notification_data = await request.json()
        await self.process_notification(notification_data)
```

### 5. File and Artifact Management

#### Image Generation and Caching
```python
# From CrewAI sample
@tool('ImageGenerationTool')
def generate_image_tool(prompt: str, session_id: str, artifact_file_id: str = None) -> str:
    if artifact_file_id and artifact_file_id in session_image_data:
        # Reference image handling
        ref_image_data = session_image_data[artifact_file_id]
        ref_bytes = base64.b64decode(ref_image_data.bytes)
        ref_image = Image.open(BytesIO(ref_bytes))
        
        # Gemini 2.0 multimodal generation
        response = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            contents=[text_input, ref_image],
            config=types.GenerateContentConfig(
                response_modalities=['Text', 'Image']
            )
        )
    
    # Cache generated image
    session_image_data[new_file_id] = ImageData(
        name=f"generated_image_{new_file_id}.png",
        bytes=base64.b64encode(image_bytes).decode('utf-8')
    )
    
    return f"Image generated and cached with ID: {new_file_id}"
```

## Implementation Guide

### 1. Creating an A2A Agent

#### Step 1: Define Your Agent Logic
```python
class MyAgent:
    async def process(self, input_text: str) -> str:
        # Your agent logic here
        return f"Processed: {input_text}"
```

#### Step 2: Create Agent Executor
```python
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message

class MyAgentExecutor(AgentExecutor):
    def __init__(self):
        self.agent = MyAgent()
    
    async def execute(self, context: RequestContext, event_queue: EventQueue):
        user_input = context.get_user_input()
        result = await self.agent.process(user_input)
        await event_queue.enqueue_event(new_agent_text_message(result))
    
    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        # Handle cancellation if needed
        pass
```

#### Step 3: Define Agent Card
```python
from a2a.types import AgentCard, AgentCapabilities, AgentSkill

agent_card = AgentCard(
    name="My Agent",
    description="What my agent does",
    url="http://localhost:8000/",
    version="1.0.0",
    capabilities=AgentCapabilities(streaming=True),
    skills=[
        AgentSkill(
            id="my_skill",
            name="My Skill",
            description="Description of the skill",
            examples=["example input 1", "example input 2"]
        )
    ]
)
```

#### Step 4: Create and Run Server
```python
import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore

request_handler = DefaultRequestHandler(
    agent_executor=MyAgentExecutor(),
    task_store=InMemoryTaskStore()
)

server = A2AStarletteApplication(
    agent_card=agent_card,
    http_handler=request_handler
)

# Run server
uvicorn.run(server.build(), host="0.0.0.0", port=8000)
```

### 2. Creating an A2A Client

#### Basic Client Usage
```python
import asyncio
from a2a.client import A2AClient
from a2a.types import Message, TextPart

async def main():
    # Initialize client
    client = A2AClient(agent_card=agent_card)  # or url="http://localhost:8000"
    
    # Create message
    message = Message(
        role="user",
        parts=[TextPart(text="Hello, agent!")]
    )
    
    # Send task
    payload = {"message": message}
    response = await client.send_task(payload)
    
    print(response.result)

asyncio.run(main())
```

#### Streaming Client
```python
async def streaming_example():
    client = A2AClient(url="http://localhost:8000")
    
    payload = {"message": Message(role="user", parts=[TextPart(text="Stream this")])}
    
    async for event in client.send_task_streaming(payload):
        if event.result:
            print(f"Event: {event.result}")
```

## CLI Development Focus

### CLI Implementation Pattern

The A2A CLI client demonstrates key patterns for CLI applications:

#### 1. Agent Discovery
```python
# Fetch agent card to understand capabilities
async with httpx.AsyncClient() as client:
    card_resolver = A2ACardResolver(client, agent_url)
    card = await card_resolver.get_agent_card()
    
    # Check capabilities
    streaming_supported = card.capabilities.streaming
```

#### 2. Interactive Loop
```python
import asyncclick as click

@click.command()
@click.option('--agent', default='http://localhost:10000')
async def cli(agent):
    client = A2AClient(url=agent)
    
    while True:
        user_input = click.prompt("Enter message")
        if user_input in [':q', 'quit']:
            break
            
        # Process input
        await send_message(client, user_input)
```

#### 3. File Attachment Support
```python
# Handle file attachments in CLI
file_path = click.prompt('Select file (enter to skip)', default='')
if file_path.strip():
    with open(file_path, 'rb') as f:
        file_content = base64.b64encode(f.read()).decode('utf-8')
        file_name = os.path.basename(file_path)
    
    message.parts.append(
        Part(root=FilePart(
            file=FileWithBytes(name=file_name, bytes=file_content)
        ))
    )
```

#### 4. Session Management
```python
# Maintain session context
context_id = uuid4().hex
task_id = None

# Include context in messages
message = Message(
    role='user',
    parts=[TextPart(text=prompt)],
    messageId=str(uuid4()),
    taskId=task_id,
    contextId=context_id,
)
```

### CLI-Specific Considerations

1. **Authentication Flow**: Handle authentication for CLI applications
2. **Input/Output Handling**: Process text input and display responses appropriately
3. **File Operations**: Support file uploads and downloads through CLI
4. **Configuration Management**: Handle agent URLs and settings
5. **Session Persistence**: Maintain conversation context across interactions

## Multi-Agent Orchestration

### Host Agent Pattern

The host agent pattern is a key orchestration approach in A2A systems:

```python
# From airbnb_planner_multiagent sample
class RoutingAgent:
    def __init__(self):
        self.remote_agent_connections = {}
        self.registered_agent_cards = {}
    
    async def retrieve_card(self, address: str):
        card_resolver = A2ACardResolver(self.httpx_client, address)
        card = await card_resolver.get_agent_card()
        self.register_agent_card(card)
    
    def register_agent_card(self, card: AgentCard):
        self.registered_agent_cards[card.name] = card
        self.remote_agent_connections[card.name] = A2AClient(
            self.httpx_client, agent_card=card
        )
    
    async def send_message(self, agent_name: str, message: str, tool_context: ToolContext):
        if agent_name not in self.remote_agent_connections:
            raise ValueError(f"Agent {agent_name} not found")
        
        client = self.remote_agent_connections[agent_name]
        request = SendMessageRequest(
            id=str(uuid4()),
            params=MessageSendParams(
                message=Message(
                    messageId=str(uuid4()),
                    role="user",
                    parts=[Part(root=TextPart(text=message))]
                )
            )
        )
        
        response = await client.send_message(request, self.task_callback)
        return self.extract_response_content(response)
```

### Multi-Language Agent Systems

A2A enables cross-language agent communication:

```python
# Python host agent coordinating with Java weather agent
class MultiLanguageOrchestrator:
    def __init__(self):
        self.agents = {
            "airbnb_python": "http://localhost:8001",
            "weather_java": "http://localhost:8080"  # Java Spring Boot agent
        }
    
    async def plan_trip(self, destination: str):
        # Get accommodation recommendations (Python agent)
        airbnb_response = await self.call_agent(
            "airbnb_python", 
            f"Find accommodations in {destination}"
        )
        
        # Get weather forecast (Java agent)
        weather_response = await self.call_agent(
            "weather_java",
            f"Get weather forecast for {destination}"
        )
        
        return {
            "accommodations": airbnb_response,
            "weather": weather_response
        }
```

## Framework Integrations

### 1. LangGraph Integration

```python
# From langgraph sample
from langgraph.graph import StateGraph
from langgraph.checkpoint.memory import MemorySaver

class LangGraphAgent:
    def __init__(self):
        self.workflow = StateGraph(AgentState)
        self.workflow.add_node("agent", self.call_model)
        self.workflow.add_node("tools", self.call_tools)
        
        # Add edges and compile
        self.workflow.add_edge("agent", "tools") 
        self.workflow.add_edge("tools", "agent")
        self.app = self.workflow.compile(checkpointer=MemorySaver())
    
    async def call_model(self, state: AgentState):
        # Model interaction logic
        response = await self.model.ainvoke(state["messages"])
        return {"messages": [response]}
    
    async def call_tools(self, state: AgentState):
        # Tool execution logic
        tools_results = await self.execute_tools(state["tool_calls"])
        return {"messages": tools_results}
```

### 2. CrewAI Integration

```python
# From crewai sample
from crewai import Agent, Task, Crew

class CrewAIAgentExecutor(AgentExecutor):
    def __init__(self):
        self.image_generation_agent = Agent(
            role='Image Generation Specialist',
            goal='Generate high-quality images based on user prompts',
            backstory='An expert in visual content creation...',
            tools=[generate_image_tool],
            verbose=True
        )
        
        self.crew = Crew(
            agents=[self.image_generation_agent],
            verbose=True
        )
    
    async def execute(self, context: RequestContext, event_queue: EventQueue):
        task = Task(
            description=context.get_user_input(),
            agent=self.image_generation_agent,
            expected_output='Generated image with description'
        )
        
        result = await self.crew.kickoff_async(tasks=[task])
        await event_queue.enqueue_event(new_agent_text_message(str(result)))
```

### 3. AutoGen Integration

```python
# From autogen sample
import autogen

class AutoGenAgentExecutor(AgentExecutor):
    def __init__(self):
        self.llm_config = {
            "model": "gemini-2.0-flash",
            "api_key": os.getenv("GOOGLE_API_KEY"),
        }
        
        self.assistant = autogen.AssistantAgent(
            name="assistant",
            llm_config=self.llm_config,
            system_message="You are a helpful assistant."
        )
        
        self.user_proxy = autogen.UserProxyAgent(
            name="user_proxy",
            human_input_mode="NEVER",
            function_map={
                "search_currency": self.search_currency
            }
        )
    
    async def execute(self, context: RequestContext, event_queue: EventQueue):
        chat_result = await self.user_proxy.a_initiate_chat(
            self.assistant,
            message=context.get_user_input()
        )
        
        await event_queue.enqueue_event(
            new_agent_text_message(chat_result.summary)
        )
```

## Installation and Setup

### Prerequisites
- Python 3.12 or higher
- UV package manager (recommended) or pip

### Core Dependencies
```toml
[project]
dependencies = [
    "a2a-sdk>=0.2.9",
    "httpx>=0.28.1",
    "httpx-sse>=0.4.0",
    "pydantic>=2.10.6",
    "starlette>=0.46.1",
    "uvicorn>=0.34.0",
]
```

### Advanced Dependencies

#### For MCP Integration
```toml
dependencies = [
    "fastmcp>=1.0",
    "mcp>=1.5.0",
    "numpy>=1.24.0",  # For embeddings
]
```

#### For Framework Integration
```toml
dependencies = [
    "langgraph>=0.4.1",
    "crewai>=0.80.0",
    "autogen-agentchat>=0.4.0",
    "semantic-kernel>=1.0.0",
]
```

#### For Cloud Providers
```toml
dependencies = [
    "google-adk>=1.0.0",
    "google-generativeai>=0.8.5",
    "azure-ai-agents>=1.0.0",
    "openai>=1.0.0",
]
```

#### For CLI Development
```toml
dependencies = [
    "asyncclick>=8.1.8",
    "rich>=13.0.0",  # For better CLI formatting
]
```

### Installation Steps

#### 1. Install A2A SDK
```bash
pip install a2a-sdk
# or
uv add a2a-sdk
```

#### 2. For CLI Development
```bash
# Additional CLI dependencies
pip install asyncclick rich
```

#### 3. Clone and Setup Samples
```bash
git clone https://github.com/a2aproject/a2a-samples.git
cd a2a-samples/samples/python
uv sync  # or pip install -r requirements.txt
```

### Environment Setup

#### For Google Cloud (Vertex AI)
```bash
export GOOGLE_GENAI_USE_VERTEXAI=TRUE
export GOOGLE_CLOUD_PROJECT=your-project-id
export GOOGLE_CLOUD_LOCATION=global
```

#### For Azure AI Foundry
```bash
export AZURE_AI_ENDPOINT=your-endpoint
export AZURE_AI_API_KEY=your-api-key
```

#### For Local Development  
```bash
# Set up local environment
export A2A_AGENT_URL=http://localhost:8000
```

## Code Examples

### 1. Simple Hello World Agent

```python
# agent.py
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message

class HelloWorldExecutor(AgentExecutor):
    async def execute(self, context: RequestContext, event_queue: EventQueue):
        await event_queue.enqueue_event(
            new_agent_text_message("Hello World!")
        )
    
    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        pass

# server.py
import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCard, AgentCapabilities, AgentSkill

agent_card = AgentCard(
    name="Hello World Agent",
    description="Simple greeting agent",
    url="http://localhost:8000/",
    version="1.0.0",
    capabilities=AgentCapabilities(streaming=True),
    skills=[AgentSkill(id="greet", name="Greet", description="Says hello")]
)

server = A2AStarletteApplication(
    agent_card=agent_card,
    http_handler=DefaultRequestHandler(
        agent_executor=HelloWorldExecutor(),
        task_store=InMemoryTaskStore()
    )
)

if __name__ == "__main__":
    uvicorn.run(server.build(), host="0.0.0.0", port=8000)
```

### 2. Advanced CLI Client with Rich Formatting

```python
# advanced_cli_client.py
import asyncio
import asyncclick as click
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from a2a.client import A2AClient, A2ACardResolver
from a2a.types import Message, TextPart

console = Console()

@click.command()
@click.option('--agent', default='http://localhost:8000')
@click.option('--streaming/--no-streaming', default=True)
async def cli(agent, streaming):
    console.print(Panel.fit("A2A CLI Client", style="bold blue"))
    
    async with httpx.AsyncClient() as httpx_client:
        # Get agent card
        resolver = A2ACardResolver(httpx_client, agent)
        card = await resolver.get_agent_card()
        
        console.print(f"[green]Connected to:[/green] {card.name}")
        console.print(f"[dim]Description:[/dim] {card.description}")
        console.print(f"[dim]Streaming:[/dim] {card.capabilities.streaming}")
        
        # Create client
        client = A2AClient(httpx_client, agent_card=card)
        
        while True:
            user_input = console.input("\n[cyan]You:[/cyan] ")
            if user_input.lower() in ['quit', 'exit', ':q']:
                break
            
            # Create message
            message = Message(
                role="user",
                parts=[TextPart(text=user_input)]
            )
            
            console.print("[yellow]Agent:[/yellow]", end=" ")
            
            # Send message
            if streaming and card.capabilities.streaming:
                # Use streaming with real-time display
                response_parts = []
                async for event in client.send_task_streaming({"message": message}):
                    if event.result and hasattr(event.result, 'message'):
                        for part in event.result.message.parts:
                            if hasattr(part, 'text'):
                                console.print(part.text, end="")
                                response_parts.append(part.text)
                console.print()  # New line after streaming
            else:
                # Non-streaming
                response = await client.send_task({"message": message})
                if response.result:
                    console.print(response.result)

if __name__ == "__main__":
    asyncio.run(cli())
```

### 3. MCP-Enabled Agent with Tool Discovery

```python
# mcp_agent.py
from fastmcp import FastMCP
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message

class MCPAgent:
    def __init__(self):
        self.mcp = FastMCP("MCP Agent")
        self.setup_tools()
    
    def setup_tools(self):
        @self.mcp.tool()
        def search_web(query: str) -> str:
            """Search the web for information"""
            # Implement web search logic
            return f"Search results for: {query}"
        
        @self.mcp.tool()
        def get_weather(location: str) -> str:
            """Get current weather for a location"""
            # Implement weather API call
            return f"Weather in {location}: Sunny, 22°C"
    
    async def process_request(self, user_input: str) -> str:
        # Use MCP tools to process the request
        tools = self.mcp.get_tools()
        
        # Simple tool selection logic (in practice, use LLM)
        if "weather" in user_input.lower():
            location = extract_location(user_input)
            return await tools["get_weather"](location)
        elif "search" in user_input.lower():
            query = extract_query(user_input)
            return await tools["search_web"](query)
        else:
            return "I can help with weather information and web searches."

class MCPAgentExecutor(AgentExecutor):
    def __init__(self):
        self.agent = MCPAgent()
    
    async def execute(self, context: RequestContext, event_queue: EventQueue):
        user_input = context.get_user_input()
        result = await self.agent.process_request(user_input)
        await event_queue.enqueue_event(new_agent_text_message(result))
    
    async def cancel(self, context: RequestContext, event_queue: EventQueue):
        pass
```

### 4. Multi-Agent Orchestration System

```python
# orchestrator.py
class OrchestratorAgent:
    def __init__(self):
        self.remote_agents = {}
        self.agent_embeddings = {}
    
    def add_agent(self, name: str, url: str, description: str):
        """Add an agent with semantic embedding for smart routing"""
        self.remote_agents[name] = A2AClient(url=url)
        # Generate embedding for agent description
        self.agent_embeddings[name] = self.generate_embedding(description)
    
    def find_best_agent(self, task: str) -> str:
        """Use embeddings to find the most suitable agent for a task"""
        task_embedding = self.generate_embedding(task)
        
        best_agent = None
        best_score = -1
        
        for agent_name, agent_embedding in self.agent_embeddings.items():
            similarity = self.cosine_similarity(task_embedding, agent_embedding)
            if similarity > best_score:
                best_score = similarity
                best_agent = agent_name
        
        return best_agent
    
    async def coordinate_multi_step_task(self, task: str):
        """Coordinate a complex task across multiple agents"""
        # Step 1: Analyze task and break it down
        plan = await self.create_execution_plan(task)
        
        results = {}
        for step in plan.steps:
            # Find best agent for this step
            agent_name = self.find_best_agent(step.description)
            
            # Execute step with dependencies
            dependencies = {k: results[k] for k in step.dependencies if k in results}
            step_context = self.build_step_context(step, dependencies)
            
            # Execute step
            result = await self.remote_agents[agent_name].send_task({
                "message": Message(
                    role="user", 
                    parts=[TextPart(text=step_context)]
                )
            })
            
            results[step.id] = result
        
        return self.synthesize_results(results)
    
    async def create_execution_plan(self, task: str):
        """Create a multi-step execution plan"""
        # Use planning agent or LLM to break down task
        planning_agent = self.remote_agents.get("planner")
        if planning_agent:
            plan_response = await planning_agent.send_task({
                "message": Message(
                    role="user",
                    parts=[TextPart(text=f"Create execution plan for: {task}")]
                )
            })
            return self.parse_execution_plan(plan_response.result)
        else:
            # Fallback to simple plan
            return ExecutionPlan(steps=[
                ExecutionStep(id="main", description=task, dependencies=[])
            ])
```

## Best Practices

### 1. Agent Development
- **Clear Skill Definitions**: Define specific, well-documented skills with examples
- **Error Handling**: Implement robust error handling and recovery mechanisms
- **State Management**: Use appropriate task stores for your use case (InMemory vs persistent)
- **Resource Management**: Properly manage connections, file handles, and resources
- **Logging**: Implement comprehensive logging for debugging and monitoring
- **Streaming Support**: Implement streaming for better user experience with long-running tasks

### 2. Client Development
- **Connection Pooling**: Use connection pooling for multiple requests to improve performance
- **Timeout Handling**: Set appropriate timeouts for requests based on expected task duration
- **Retry Logic**: Implement exponential backoff retry mechanisms for failed requests
- **Stream Processing**: Handle streaming responses efficiently without blocking
- **Agent Discovery**: Cache agent cards but refresh periodically to get updates

### 3. CLI Applications
- **User Experience**: Provide clear prompts, progress indicators, and helpful error messages
- **Configuration**: Support configuration files, environment variables, and command-line options
- **File Handling**: Validate file inputs, handle large files efficiently, support multiple formats
- **Session Management**: Maintain conversation context appropriately, allow session save/restore
- **Output Formatting**: Use libraries like Rich for better terminal output formatting

### 4. Multi-Agent Systems
- **Agent Registry**: Maintain a registry of available agents with their capabilities
- **Smart Routing**: Use embeddings or other AI techniques for intelligent task routing
- **Error Propagation**: Handle failures gracefully and provide meaningful error messages
- **Monitoring**: Implement comprehensive monitoring of agent health and performance
- **Circuit Breakers**: Implement circuit breaker patterns for failing agents

### 5. Security
- **Input Validation**: Always validate and sanitize inputs from external agents
- **Authentication**: Implement proper authentication mechanisms (OAuth2, API keys, etc.)
- **Rate Limiting**: Implement rate limiting to prevent abuse and resource exhaustion
- **Audit Logging**: Log important security events and agent interactions
- **Sandboxing**: Consider sandboxing agent execution environments

## Security Considerations

### Critical Security Warnings

⚠️ **Important**: All data received from external agents should be treated as untrusted input. This includes:
- AgentCard metadata (name, description, skills)
- Message content and artifacts
- Task statuses and responses
- File uploads and downloads

### Security Measures

1. **Input Sanitization**
   ```python
   import html
   import bleach
   
   def sanitize_text_input(text: str) -> str:
       # HTML escaping
       escaped = html.escape(text)
       # Additional sanitization for specific contexts
       return bleach.clean(escaped, tags=[], strip=True)
   
   def validate_file_upload(file_data: bytes, mime_type: str) -> bool:
       # Validate file type and content
       if mime_type not in ALLOWED_MIME_TYPES:
           return False
       
       # Additional content validation
       if len(file_data) > MAX_FILE_SIZE:
           return False
           
       return True
   ```

2. **Authentication and Authorization**
   ```python
   # OAuth2 with scope validation
   class SecureA2AServer(A2AStarletteApplication):
       def __init__(self, agent_card, http_handler, auth_config):
           super().__init__(agent_card, http_handler)
           self.app.add_middleware(OAuth2Middleware, auth_config=auth_config)
           self.app.add_middleware(RateLimitMiddleware, 
                                  requests_per_minute=60)
   
   # API Key authentication
   async def verify_api_key(request: Request):
       api_key = request.headers.get("X-API-Key")
       if not api_key or not is_valid_api_key(api_key):
           raise HTTPException(status_code=401, detail="Invalid API key")
   ```

3. **Secure Agent Card Validation**
   ```python
   from pydantic import ValidationError, validator
   
   class SecureAgentCard(AgentCard):
       @validator('name', 'description')
       def validate_text_fields(cls, v):
           if len(v) > 1000:  # Prevent excessively long strings
               raise ValueError('Text field too long')
           return sanitize_text_input(v)
       
       @validator('url')
       def validate_url(cls, v):
           # Only allow HTTPS URLs
           if not v.startswith('https://'):
               raise ValueError('Only HTTPS URLs allowed')
           return v
   ```

4. **Rate Limiting and Circuit Breakers**
   ```python
   from circuitbreaker import circuit
   import asyncio
   from collections import defaultdict
   
   class RateLimitedA2AClient:
       def __init__(self, url: str, requests_per_second: int = 10):
           self.client = A2AClient(url=url)
           self.rate_limiter = asyncio.Semaphore(requests_per_second)
           self.request_times = defaultdict(list)
       
       @circuit(failure_threshold=5, recovery_timeout=30)
       async def send_task_with_protection(self, payload):
           async with self.rate_limiter:
               # Rate limiting logic
               now = time.time()
               self.request_times[self.client.url] = [
                   t for t in self.request_times[self.client.url] 
                   if now - t < 60  # Keep only last minute
               ]
               
               if len(self.request_times[self.client.url]) >= 60:
                   raise RateLimitExceeded("Too many requests")
               
               self.request_times[self.client.url].append(now)
               return await self.client.send_task(payload)
   ```

5. **Secure File Handling**
   ```python
   import tempfile
   import os
   from pathlib import Path
   
   class SecureFileHandler:
       def __init__(self, max_file_size: int = 10 * 1024 * 1024):  # 10MB
           self.max_file_size = max_file_size
           self.allowed_extensions = {'.txt', '.json', '.csv', '.png', '.jpg'}
       
       async def handle_file_upload(self, file_part: FilePart) -> str:
           # Validate file
           if len(file_part.file.bytes) > self.max_file_size:
               raise ValueError("File too large")
           
           file_ext = Path(file_part.file.name).suffix.lower()
           if file_ext not in self.allowed_extensions:
               raise ValueError(f"File type {file_ext} not allowed")
           
           # Save to secure temporary location
           with tempfile.NamedTemporaryFile(
               delete=False, 
               suffix=file_ext,
               dir='/secure/temp/path'
           ) as tmp_file:
               tmp_file.write(base64.b64decode(file_part.file.bytes))
               return tmp_file.name
   ```

### Common Vulnerabilities and Mitigations

1. **Prompt Injection**
   - **Risk**: Malicious agents could inject crafted prompts to manipulate LLM behavior
   - **Mitigation**: Sanitize all inputs, use structured prompts, implement output filtering

2. **Data Exfiltration**
   - **Risk**: Untrusted agents might attempt to extract sensitive data
   - **Mitigation**: Implement data classification, access controls, and audit logging

3. **Resource Exhaustion (DoS)**
   - **Risk**: Agents could consume excessive resources (CPU, memory, network)
   - **Mitigation**: Implement resource limits, timeouts, and circuit breakers

4. **File-based Attacks**
   - **Risk**: Malicious file uploads could contain viruses or exploit vulnerabilities
   - **Mitigation**: File type validation, virus scanning, sandboxed processing

5. **Man-in-the-Middle Attacks**
   - **Risk**: Interception of agent communications
   - **Mitigation**: Use HTTPS/TLS for all communications, certificate validation

## Resources

### Official Documentation
- [A2A Protocol Specification](https://github.com/a2aproject/A2A) - Core protocol specification
- [A2A Python SDK](https://github.com/a2aproject/a2a-python) - Python implementation
- [A2A Inspector](https://github.com/a2aproject/a2a-inspector) - UI tool for inspecting A2A agents
- [Google ADK Documentation](https://google.github.io/adk-docs/) - Agent Development Kit

### Codelabs and Tutorials
- [Google's Agent Stack in Action: ADK, A2A, MCP on Google Cloud](https://codelabs.developers.google.com/instavibe-adk-multi-agents/instructions)
- [Getting Started with Agent-to-Agent (A2A) Protocol: Gemini on Cloud Run](https://codelabs.developers.google.com/intro-a2a-purchasing-concierge)
- [Getting Started with MCP, ADK and A2A](https://codelabs.developers.google.com/codelabs/currency-agent)

### Related Technologies
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) - Tool and data source integration
- [Vertex AI Documentation](https://cloud.google.com/vertex-ai) - Google Cloud AI platform
- [Azure AI Foundry](https://docs.microsoft.com/en-us/azure/ai/) - Microsoft Azure AI platform

### Framework Documentation
- [LangGraph](https://langchain-ai.github.io/langgraph/) - Agent workflow orchestration
- [CrewAI](https://docs.crewai.com/) - Multi-agent collaboration framework
- [AutoGen](https://microsoft.github.io/autogen/) - Conversational AI framework
- [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/) - Microsoft's AI orchestration SDK

### Sample Projects by Category

#### **CLI Clients**
- `samples/python/hosts/cli/` - Python CLI with streaming support
- `samples/js/src/cli.ts` - TypeScript CLI with rich formatting

#### **Basic Agent Examples**
- `samples/python/agents/helloworld/` - Simple greeting agent
- `samples/python/agents/dice_agent_grpc/` - gRPC-based agent

#### **Framework Integration**
- `samples/python/agents/langgraph/` - LangGraph workflow integration
- `samples/python/agents/crewai/` - CrewAI multi-agent system
- `samples/python/agents/autogen/` - AutoGen conversation framework

#### **Cloud Provider Integration**
- `samples/python/agents/azureaifoundry_sdk/` - Azure AI Foundry integration
- `samples/python/agents/a2a_telemetry/` - Google ADK integration

#### **MCP Integration**
- `samples/python/agents/a2a_mcp/` - Full MCP travel planning system
- `samples/python/agents/a2a-mcp-without-framework/` - Pure A2A/MCP integration

#### **Multi-Agent Systems**
- `samples/python/agents/airbnb_planner_multiagent/` - Multi-agent orchestration
- `samples/multi_language/` - Cross-language agent communication

#### **Security and Authentication**
- `samples/python/agents/headless_agent_auth/` - OAuth2 authentication
- `samples/python/hosts/cli/push_notification_listener.py` - Secure push notifications

#### **External Service Integration**
- `samples/python/agents/github-agent/` - GitHub API integration
- `samples/python/agents/travel_planner_agent/` - Travel booking APIs

### Getting Help
- [Issues Page](https://github.com/a2aproject/a2a-samples/issues) - For feedback and bug reports
- [Contributing Guide](https://github.com/a2aproject/a2a-samples/blob/main/CONTRIBUTING.md) - How to contribute
- [Security Guidelines](https://github.com/a2aproject/a2a-samples/blob/main/SECURITY.md) - Security best practices

---

## Conclusion

The A2A protocol provides a powerful foundation for building distributed, interoperable agent systems that can leverage multiple AI frameworks, cloud providers, and external services. The comprehensive examples in the a2a-samples repository demonstrate sophisticated patterns for:

1. **Multi-Agent Orchestration**: Complex workflows with intelligent task routing and coordination
2. **Framework Integration**: Seamless integration with LangGraph, CrewAI, AutoGen, and other AI frameworks
3. **Cloud-Native Architecture**: Native integration with Google AI, Azure AI Foundry, and other cloud platforms
4. **Security and Authentication**: Production-ready security patterns with OAuth2, rate limiting, and input validation
5. **MCP Integration**: Dynamic tool and data source discovery using the Model Context Protocol
6. **Real-time Communication**: Streaming responses, push notifications, and async processing

By following the patterns and practices outlined in this guide, you can create robust, scalable, and secure CLI applications and agent systems that leverage the full capabilities of the A2A ecosystem.

The protocol is actively evolving with new features like MCP integration, enhanced security models, and improved multi-agent orchestration capabilities. Stay updated with the latest developments through the official repositories and documentation.

**Key Takeaways for CLI Development:**
- Use the A2A client patterns for agent discovery and communication
- Implement streaming for better user experience
- Support file uploads/downloads with proper security validation
- Maintain session context for conversational interactions
- Integrate with multiple agents for complex task orchestration
- Follow security best practices for handling untrusted agent data