"""Prompt loading and management utilities."""

import os
import logging
from pathlib import Path
from typing import Dict, Optional

logger = logging.getLogger(__name__)


class PromptLoader:
    """Utility class for loading prompts from files."""
    
    @staticmethod
    def load_prompt(prompt_path: str) -> str:
        """
        Load a prompt from a file.
        
        Args:
            prompt_path: Path to the prompt file (relative to project root)
            
        Returns:
            The prompt content as a string
            
        Raises:
            FileNotFoundError: If the prompt file doesn't exist
            IOError: If there's an error reading the file
        """
        # Convert relative path to absolute
        if not os.path.isabs(prompt_path):
            # Assume paths are relative to project root
            project_root = Path(__file__).parent.parent.parent
            full_path = project_root / prompt_path
        else:
            full_path = Path(prompt_path)
        
        if not full_path.exists():
            raise FileNotFoundError(f"Prompt file not found: {full_path}")
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            
            logger.debug(f"Loaded prompt from: {full_path}")
            return content
            
        except Exception as e:
            logger.error(f"Error loading prompt from {full_path}: {e}")
            raise IOError(f"Failed to load prompt from {full_path}: {e}")
    
    @staticmethod
    def load_prompts(prompt_configs: Dict[str, str]) -> Dict[str, str]:
        """
        Load multiple prompts from their configured paths.
        
        Args:
            prompt_configs: Dictionary mapping prompt names to file paths
            
        Returns:
            Dictionary mapping prompt names to their content
        """
        prompts = {}
        
        for prompt_name, prompt_path in prompt_configs.items():
            try:
                prompts[prompt_name] = PromptLoader.load_prompt(prompt_path)
                logger.info(f"Loaded prompt '{prompt_name}' from: {prompt_path}")
            except (FileNotFoundError, IOError) as e:
                logger.warning(f"Failed to load prompt '{prompt_name}': {e}")
                # Continue loading other prompts
        
        return prompts
    
    @staticmethod
    def format_prompt(template: str, **kwargs) -> str:
        """
        Format a prompt template with variables.
        
        Args:
            template: The prompt template string
            **kwargs: Variables to substitute in the template
            
        Returns:
            The formatted prompt
        """
        try:
            return template.format(**kwargs)
        except KeyError as e:
            logger.warning(f"Missing variable in prompt template: {e}")
            return template
        except Exception as e:
            logger.error(f"Error formatting prompt template: {e}")
            return template