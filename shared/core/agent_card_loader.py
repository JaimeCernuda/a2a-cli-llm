"""Agent card loader for external agent card configurations."""

import logging
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Any
from a2a.types import AgentCard, AgentCapabilities, AgentSkill

logger = logging.getLogger(__name__)


class AgentCardLoader:
    """Loader for external agent card configurations."""
    
    @staticmethod
    def load_agent_card_config(agent_card_path: str) -> Optional[Dict[str, Any]]:
        """
        Load agent card configuration from external file.
        
        Args:
            agent_card_path: Path to the agent card configuration file
            
        Returns:
            Parsed agent card configuration or None if loading fails
        """
        try:
            card_file = Path(agent_card_path)
            if not card_file.exists():
                logger.warning(f"Agent card file not found: {agent_card_path}")
                return None
            
            logger.info(f"Loading agent card configuration from: {agent_card_path}")
            
            with open(card_file, 'r', encoding='utf-8') as f:
                if card_file.suffix.lower() in ['.yaml', '.yml']:
                    config = yaml.safe_load(f)
                else:
                    logger.error(f"Unsupported agent card file format: {card_file.suffix}")
                    return None
            
            if 'agent_card' not in config:
                logger.error(f"No 'agent_card' section found in {agent_card_path}")
                return None
            
            logger.info(f"Successfully loaded agent card configuration")
            return config['agent_card']
            
        except Exception as e:
            logger.error(f"Failed to load agent card from {agent_card_path}: {e}")
            return None
    
    @staticmethod
    def create_agent_card_from_config(
        host: str, 
        port: int, 
        config: Any,
        agent_card_config: Optional[Dict[str, Any]] = None
    ) -> AgentCard:
        """
        Create AgentCard from configuration.
        
        Args:
            host: Server host
            port: Server port
            config: Main application configuration
            agent_card_config: External agent card configuration (optional)
            
        Returns:
            Configured AgentCard
        """
        # Use external configuration if available, otherwise fall back to defaults
        if agent_card_config:
            logger.info("Using external agent card configuration")
            
            # Get configuration values with defaults
            default_input_modes = agent_card_config.get('default_input_modes', ['text'])
            default_output_modes = agent_card_config.get('default_output_modes', ['text'])
            
            # Create capabilities
            cap_config = agent_card_config.get('capabilities', {})
            capabilities = AgentCapabilities(
                streaming=cap_config.get('streaming', True),
                pushNotifications=cap_config.get('push_notifications', False)
            )
            
            # Create skills from configuration
            skills = []
            skills_config = agent_card_config.get('skills', [])
            for skill_config in skills_config:
                skill = AgentSkill(
                    id=skill_config.get('id', ''),
                    name=skill_config.get('name', ''),
                    description=skill_config.get('description', ''),
                    tags=skill_config.get('tags', []),
                    examples=skill_config.get('examples', [])
                )
                skills.append(skill)
            
            logger.info(f"Created agent card with {len(skills)} skills from external configuration")
            
        else:
            # No fallback - crash with clear error message
            logger.error("No external agent card configuration provided and no fallback available")
            raise RuntimeError(
                "Agent card configuration is required but not provided. "
                "Please specify 'agent_card' in your configuration file pointing to a valid agent card YAML file. "
                "This ensures the agent's capabilities and skills are properly defined for your specific use case."
            )
        
        # Create and return agent card
        return AgentCard(
            name=config.agent.name,
            description=config.agent.description,
            url=f"http://{host}:{port}/",
            version=config.agent.version,
            defaultInputModes=default_input_modes,
            defaultOutputModes=default_output_modes,
            capabilities=capabilities,
            skills=skills
        )