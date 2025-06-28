"""A2A CLI Client implementation."""

import asyncio
import sys
from pathlib import Path
from typing import Optional
from uuid import uuid4

import asyncclick as click
import httpx
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.syntax import Syntax

from a2a.client import A2AClient, A2ACardResolver
from a2a.types import (
    Message, 
    SendMessageRequest, 
    SendStreamingMessageRequest,
    MessageSendParams,
    Task,
    TaskState,
    GetTaskRequest,
    TaskQueryParams
)

# Simple client config
class ClientConfig:
    def __init__(self, agent_url: str, timeout: int = 30, max_retries: int = 3):
        self.agent_url = agent_url
        self.timeout = timeout
        self.max_retries = max_retries
    
    @classmethod
    def from_url(cls, agent_url: str) -> "ClientConfig":
        import os
        return cls(
            agent_url=agent_url,
            timeout=int(os.getenv("A2A_TIMEOUT", "30")),
            max_retries=int(os.getenv("A2A_MAX_RETRIES", "3"))
        )
from shared.core.utils import (
    setup_logging, 
    create_text_message, 
    create_message_with_file,
    extract_text_from_message,
    format_agent_info
)


console = Console()


class A2ACLIClient:
    """A2A CLI client for interacting with agents."""
    
    def __init__(self, config: ClientConfig):
        """Initialize the CLI client."""
        self.config = config
        self.httpx_client: Optional[httpx.AsyncClient] = None
        self.a2a_client: Optional[A2AClient] = None
        self.agent_card = None
    
    async def __aenter__(self):
        """Async context manager entry."""
        self.httpx_client = httpx.AsyncClient(
            timeout=httpx.Timeout(self.config.timeout)
        )
        
        # Resolve agent card
        resolver = A2ACardResolver(
            httpx_client=self.httpx_client,
            base_url=self.config.agent_url
        )
        
        try:
            self.agent_card = await resolver.get_agent_card()
            self.a2a_client = A2AClient(
                httpx_client=self.httpx_client,
                agent_card=self.agent_card
            )
        except Exception as e:
            await self.httpx_client.aclose()
            raise click.ClickException(f"Failed to connect to agent: {e}")
        
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self.httpx_client:
            await self.httpx_client.aclose()
    
    async def send_message(
        self, 
        text: str, 
        file_path: Optional[str] = None,
        streaming: bool = False
    ) -> None:
        """Send a message to the agent."""
        if not self.a2a_client:
            raise click.ClickException("Client not initialized")
        
        # Create message
        if file_path:
            message = create_message_with_file(text, file_path)
            console.print(f"[blue]Sending message with file:[/blue] {Path(file_path).name}")
        else:
            message = create_text_message(text)
        
        console.print(f"[blue]You:[/blue] {text}")
        
        try:
            if streaming and self.agent_card.capabilities.streaming:
                await self._handle_streaming_response(message)
            else:
                await self._handle_synchronous_response(message)
        except Exception as e:
            console.print(f"[red]Error:[/red] {e}")
            raise click.ClickException(f"Failed to send message: {e}")
    
    async def _handle_streaming_response(self, message: Message) -> None:
        """Handle streaming response from agent."""
        request = SendStreamingMessageRequest(
            id=str(uuid4()),
            params=MessageSendParams(message=message)
        )
        
        console.print("[yellow]Agent:[/yellow] ", end="")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("Waiting for response...", total=None)
            
            response_parts = []
            async for event in self.a2a_client.send_message_streaming(request):
                progress.update(task, description="Receiving response...")
                
                if hasattr(event, 'result') and event.result:
                    if isinstance(event.result, Task):
                        if hasattr(event.result.status, 'message') and event.result.status.message:
                            text = extract_text_from_message(event.result.status.message)
                            if text:
                                console.print(text, end="")
                                response_parts.append(text)
                        
                        if event.result.status.state in [TaskState.completed, TaskState.failed]:
                            break
            
            progress.update(task, description="Complete")
        
        console.print()  # New line after streaming
        
        if not response_parts:
            console.print("[yellow](No response received)[/yellow]")
    
    async def _handle_synchronous_response(self, message: Message) -> None:
        """Handle synchronous response from agent."""
        request = SendMessageRequest(
            id=str(uuid4()),
            params=MessageSendParams(message=message)
        )
        
        with Progress(
            SpinnerColumn(),
            TextColumn("Sending message..."),
            console=console,
            transient=True
        ) as progress:
            task = progress.add_task("Processing...", total=None)
            
            response = await self.a2a_client.send_message(request)
            
            progress.update(task, description="Complete")
        
        # Handle response - check both response.result and response.root.result
        result = None
        if hasattr(response, 'result') and response.result:
            result = response.result
        elif hasattr(response, 'root') and hasattr(response.root, 'result') and response.root.result:
            result = response.root.result
        
        if result:
            if isinstance(result, Task):
                if hasattr(result.status, 'message') and result.status.message:
                    text = extract_text_from_message(result.status.message)
                    if text:
                        console.print(f"[yellow]Agent:[/yellow] {text}")
                    else:
                        console.print(f"[yellow]Agent:[/yellow] Task {result.status.state}")
                else:
                    console.print(f"[yellow]Agent:[/yellow] Task {result.status.state}")
            elif isinstance(result, Message):
                # Handle direct message response
                text = extract_text_from_message(result)
                if text:
                    console.print(f"[yellow]Agent:[/yellow] {text}")
                else:
                    console.print(f"[yellow]Agent:[/yellow] (Empty message)")
            else:
                console.print(f"[yellow]Agent:[/yellow] {result}")
        else:
            console.print("[yellow]Agent:[/yellow] (No response)")
    
    async def get_agent_info(self) -> None:
        """Display agent information."""
        if not self.agent_card:
            raise click.ClickException("No agent card available")
        
        info = format_agent_info(self.agent_card)
        panel = Panel(
            info,
            title="Agent Information",
            border_style="blue"
        )
        console.print(panel)
    
    async def interactive_mode(self) -> None:
        """Run in interactive mode."""
        console.print(Panel.fit("A2A CLI Interactive Mode", style="bold blue"))
        
        if self.agent_card:
            console.print(f"[green]Connected to:[/green] {self.agent_card.name}")
            console.print(f"[dim]Description:[/dim] {self.agent_card.description}")
            if self.agent_card.capabilities.streaming:
                console.print("[dim]Streaming enabled[/dim]")
            console.print()
        
        console.print("[dim]Commands: 'help', 'info', 'quit' or just type a message[/dim]")
        console.print()
        
        context_id = uuid4().hex
        
        while True:
            try:
                user_input = console.input("[cyan]You:[/cyan] ")
                
                if user_input.lower() in ['quit', 'exit', ':q']:
                    console.print("[dim]Goodbye![/dim]")
                    break
                elif user_input.lower() == 'help':
                    self._show_help()
                    continue
                elif user_input.lower() == 'info':
                    await self.get_agent_info()
                    continue
                elif not user_input.strip():
                    continue
                
                # Send message
                message = create_text_message(user_input, context_id=context_id)
                
                if self.agent_card.capabilities.streaming:
                    await self._handle_streaming_response(message)
                else:
                    await self._handle_synchronous_response(message)
                
                console.print()
                
            except KeyboardInterrupt:
                console.print("\n[dim]Goodbye![/dim]")
                break
            except Exception as e:
                console.print(f"[red]Error:[/red] {e}")
    
    def _show_help(self) -> None:
        """Show help information."""
        help_text = """Available commands:
        
• Type any message to send to the agent
• 'help' - Show this help
• 'info' - Show agent information  
• 'quit', 'exit', ':q' - Exit interactive mode

The agent can respond to:
• Greetings (hello, hi, hey)
• Help requests (help)
• Time/date requests (time, date)
• Echo commands (echo <message>)
• General conversation"""
        
        panel = Panel(
            help_text,
            title="Help",
            border_style="green"
        )
        console.print(panel)


@click.group()
@click.option("--log-level", default="warning", type=click.Choice(["debug", "info", "warning", "error"]))
async def cli(log_level: str) -> None:
    """A2A CLI Client - Interact with A2A agents."""
    setup_logging(log_level)


@cli.command()
@click.option("--agent", required=True, help="Agent URL")
@click.option("--message", required=True, help="Message to send")
@click.option("--file", "file_path", help="File to attach")
@click.option("--streaming/--no-streaming", default=True, help="Use streaming if available")
async def send(agent: str, message: str, file_path: Optional[str], streaming: bool) -> None:
    """Send a message to an agent."""
    config = ClientConfig.from_url(agent)
    
    async with A2ACLIClient(config) as client:
        await client.send_message(message, file_path, streaming)


@cli.command()
@click.option("--agent", required=True, help="Agent URL")
async def interactive(agent: str) -> None:
    """Start interactive mode with an agent."""
    config = ClientConfig.from_url(agent)
    
    async with A2ACLIClient(config) as client:
        await client.interactive_mode()


@cli.command()
@click.option("--agent", required=True, help="Agent URL")
async def info(agent: str) -> None:
    """Get information about an agent."""
    config = ClientConfig.from_url(agent)
    
    async with A2ACLIClient(config) as client:
        await client.get_agent_info()


async def main() -> None:
    """Main entry point for the CLI."""
    try:
        await cli()
    except click.ClickException as e:
        console.print(f"[red]Error:[/red] {e.message}")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Unexpected error:[/red] {e}")
        sys.exit(1)


def run_client() -> None:
    """Entry point for running the client."""
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())