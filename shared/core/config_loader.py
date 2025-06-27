"""Configuration loading and management."""

import os
import logging
from pathlib import Path
from typing import Dict, Any, Optional
import yaml
from dataclasses import dataclass, asdict
from typing import List


logger = logging.getLogger(__name__)


@dataclass
class AgentConfig:
    """Agent configuration."""
    name: str = "A2A CLI AI Agent"
    description: str = "An intelligent agent powered by configurable LLM providers"
    version: str = "0.2.0"
    persona: Optional[str] = None
    system_prompt: Optional[str] = None


@dataclass
class ProviderConfig:
    """LLM provider configuration."""
    api_key: Optional[str] = None
    model: str = "default"
    max_tokens: int = 2048
    temperature: float = 0.7
    base_url: Optional[str] = None
    timeout: int = 60


@dataclass
class ServerConfig:
    """Server configuration."""
    host: str = "localhost"
    port: int = 8000
    log_level: str = "info"
    streaming: bool = True
    push_notifications: bool = False


@dataclass
class MCPServerConfig:
    """MCP server configuration."""
    name: str
    command: List[str]
    cwd: Optional[str] = None
    enabled: bool = True


@dataclass
class ClientConfig:
    """Client configuration."""
    timeout: int = 30
    max_retries: int = 3
    prefer_streaming: bool = True


@dataclass
class LoggingConfig:
    """Logging configuration."""
    level: str = "info"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


@dataclass 
class A2AConfig:
    """Complete A2A CLI configuration."""
    default_provider: str = "gemini"
    agent: AgentConfig = None
    providers: Dict[str, ProviderConfig] = None
    mcp_servers: Dict[str, MCPServerConfig] = None
    server: ServerConfig = None
    client: ClientConfig = None
    logging: LoggingConfig = None
    
    def __post_init__(self):
        if self.agent is None:
            self.agent = AgentConfig()
        if self.providers is None:
            self.providers = {}
        if self.mcp_servers is None:
            self.mcp_servers = {}
        if self.server is None:
            self.server = ServerConfig()
        if self.client is None:
            self.client = ClientConfig()
        if self.logging is None:
            self.logging = LoggingConfig()


class ConfigLoader:
    """Configuration loader with environment variable substitution."""
    
    DEFAULT_CONFIG_PATHS = [
        "./config.yaml",
        "./a2a_config.yaml",
        "~/.a2a/config.yaml",
        "/etc/a2a/config.yaml"
    ]
    
    @staticmethod
    def find_config_file(config_path: Optional[str] = None) -> Optional[Path]:
        """Find configuration file."""
        if config_path:
            path = Path(config_path).expanduser()
            if path.exists():
                return path
            else:
                logger.warning(f"Specified config file not found: {config_path}")
                return None
        
        # Search default locations
        for default_path in ConfigLoader.DEFAULT_CONFIG_PATHS:
            path = Path(default_path).expanduser()
            if path.exists():
                logger.info(f"Found config file: {path}")
                return path
        
        logger.info("No config file found, using defaults")
        return None
    
    @staticmethod
    def substitute_env_vars(value: Any) -> Any:
        """Recursively substitute environment variables in configuration values."""
        if isinstance(value, str):
            # Handle ${VAR_NAME} syntax
            if value.startswith("${") and value.endswith("}"):
                env_var = value[2:-1]
                default_value = None
                
                # Handle ${VAR_NAME:default} syntax
                if ":" in env_var:
                    env_var, default_value = env_var.split(":", 1)
                
                result = os.getenv(env_var, default_value)
                if result is None:
                    logger.warning(f"Environment variable {env_var} not set")
                    return ""
                return result
            return value
        elif isinstance(value, dict):
            return {k: ConfigLoader.substitute_env_vars(v) for k, v in value.items()}
        elif isinstance(value, list):
            return [ConfigLoader.substitute_env_vars(item) for item in value]
        else:
            return value
    
    @staticmethod
    def load_config(config_path: Optional[str] = None) -> A2AConfig:
        """Load configuration from file or defaults."""
        config_file = ConfigLoader.find_config_file(config_path)
        
        if config_file:
            try:
                with open(config_file, 'r') as f:
                    raw_config = yaml.safe_load(f)
                
                # Substitute environment variables
                config_data = ConfigLoader.substitute_env_vars(raw_config)
                
                # Parse configuration
                config = A2AConfig()
                
                # Set simple fields
                config.default_provider = config_data.get("default_provider", "gemini")
                
                # Parse agent config
                if "agent" in config_data:
                    agent_data = config_data["agent"]
                    config.agent = AgentConfig(
                        name=agent_data.get("name", "A2A CLI AI Agent"),
                        description=agent_data.get("description", "An intelligent agent powered by configurable LLM providers"),
                        version=agent_data.get("version", "0.2.0"),
                        persona=agent_data.get("persona"),
                        system_prompt=agent_data.get("system_prompt")
                    )
                
                # Parse provider configs
                if "providers" in config_data:
                    config.providers = {}
                    for provider_name, provider_data in config_data["providers"].items():
                        config.providers[provider_name] = ProviderConfig(
                            api_key=provider_data.get("api_key"),
                            model=provider_data.get("model", "default"),
                            max_tokens=provider_data.get("max_tokens", 2048),
                            temperature=provider_data.get("temperature", 0.7),
                            base_url=provider_data.get("base_url"),
                            timeout=provider_data.get("timeout", 60)
                        )
                
                # Parse MCP server configs
                if "mcp_servers" in config_data:
                    config.mcp_servers = {}
                    for server_name, server_data in config_data["mcp_servers"].items():
                        config.mcp_servers[server_name] = MCPServerConfig(
                            name=server_name,
                            command=server_data.get("command", []),
                            cwd=server_data.get("cwd"),
                            enabled=server_data.get("enabled", True)
                        )
                
                # Parse server config
                if "server" in config_data:
                    server_data = config_data["server"]
                    config.server = ServerConfig(
                        host=server_data.get("host", "localhost"),
                        port=server_data.get("port", 8000),
                        log_level=server_data.get("log_level", "info"),
                        streaming=server_data.get("streaming", True),
                        push_notifications=server_data.get("push_notifications", False)
                    )
                
                # Parse client config
                if "client" in config_data:
                    client_data = config_data["client"]
                    config.client = ClientConfig(
                        timeout=client_data.get("timeout", 30),
                        max_retries=client_data.get("max_retries", 3),
                        prefer_streaming=client_data.get("prefer_streaming", True)
                    )
                
                # Parse logging config
                if "logging" in config_data:
                    logging_data = config_data["logging"]
                    config.logging = LoggingConfig(
                        level=logging_data.get("level", "info"),
                        format=logging_data.get("format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
                    )
                
                logger.info(f"Loaded configuration from {config_file}")
                return config
                
            except Exception as e:
                logger.error(f"Failed to load config from {config_file}: {e}")
                logger.info("Using default configuration")
        
        # Return default configuration
        return A2AConfig()
    
    @staticmethod
    def get_provider_config(config: A2AConfig, provider_name: str) -> Dict[str, Any]:
        """Get provider configuration as dictionary."""
        if provider_name not in config.providers:
            raise ValueError(f"Provider {provider_name} not configured")
        
        provider_config = config.providers[provider_name]
        return asdict(provider_config)
    
    @staticmethod
    def validate_config(config: A2AConfig) -> list[str]:
        """Validate configuration and return list of errors."""
        errors = []
        
        # Check default provider exists
        if config.default_provider not in config.providers:
            errors.append(f"Default provider '{config.default_provider}' not configured")
        
        # Validate provider configs
        for provider_name, provider_config in config.providers.items():
            if provider_name in ["gemini", "claude"] and not provider_config.api_key:
                errors.append(f"{provider_name} provider missing API key")
            
            if provider_name == "ollama" and not provider_config.base_url:
                errors.append("Ollama provider missing base_url")
        
        return errors