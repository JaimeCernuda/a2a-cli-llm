"""Persona loading utilities for A2A CLI."""

import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


class PersonaLoader:
    """Load persona prompts from markdown files."""
    
    DEFAULT_PERSONAS_DIR = Path("personas")
    
    @classmethod
    def load_persona(cls, persona_name: str, personas_dir: Optional[Path] = None) -> str:
        """
        Load a persona prompt from a markdown file.
        
        Args:
            persona_name: Name of the persona (e.g., 'developer', 'analyst') or path to file
            personas_dir: Directory containing persona files (defaults to 'personas/')
            
        Returns:
            The persona prompt text
            
        Raises:
            FileNotFoundError: If the persona file doesn't exist
            IOError: If there's an error reading the file
        """
        if personas_dir is None:
            personas_dir = cls.DEFAULT_PERSONAS_DIR
        
        # Check if persona_name is a direct path
        if "/" in persona_name or "\\" in persona_name:
            persona_path = Path(persona_name)
        else:
            # Standard persona file in personas directory
            persona_path = personas_dir / f"{persona_name}.md"
        
        try:
            if not persona_path.exists():
                raise FileNotFoundError(f"Persona file not found: {persona_path}")
            
            with open(persona_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            
            if not content:
                logger.warning(f"Persona file is empty: {persona_path}")
                return cls._get_fallback_prompt()
            
            logger.info(f"Loaded persona from: {persona_path}")
            return content
            
        except FileNotFoundError:
            logger.error(f"Persona file not found: {persona_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading persona from {persona_path}: {e}")
            raise IOError(f"Failed to load persona: {e}")
    
    @classmethod
    def list_available_personas(cls, personas_dir: Optional[Path] = None) -> list[str]:
        """
        List all available persona names.
        
        Args:
            personas_dir: Directory to search for persona files
            
        Returns:
            List of available persona names (without .md extension)
        """
        if personas_dir is None:
            personas_dir = cls.DEFAULT_PERSONAS_DIR
        
        if not personas_dir.exists():
            logger.warning(f"Personas directory not found: {personas_dir}")
            return []
        
        personas = []
        for file_path in personas_dir.glob("*.md"):
            personas.append(file_path.stem)
        
        return sorted(personas)
    
    @classmethod
    def _get_fallback_prompt(cls) -> str:
        """Get a basic fallback prompt when persona loading fails."""
        return """You are a helpful AI assistant. Respond clearly and helpfully to user questions and requests."""
    
    @classmethod
    def validate_persona(cls, persona_name: str, personas_dir: Optional[Path] = None) -> bool:
        """
        Check if a persona exists and is valid.
        
        Args:
            persona_name: Name of the persona to validate
            personas_dir: Directory containing persona files
            
        Returns:
            True if persona exists and is readable, False otherwise
        """
        try:
            cls.load_persona(persona_name, personas_dir)
            return True
        except (FileNotFoundError, IOError):
            return False
    
    @classmethod
    def get_persona_info(cls, persona_name: str, personas_dir: Optional[Path] = None) -> dict:
        """
        Get metadata about a persona file.
        
        Args:
            persona_name: Name of the persona
            personas_dir: Directory containing persona files
            
        Returns:
            Dictionary with persona metadata
        """
        if personas_dir is None:
            personas_dir = cls.DEFAULT_PERSONAS_DIR
        
        persona_path = personas_dir / f"{persona_name}.md"
        
        info = {
            "name": persona_name,
            "path": str(persona_path),
            "exists": persona_path.exists(),
            "size": 0,
            "title": persona_name.title(),
            "description": ""
        }
        
        if persona_path.exists():
            try:
                stat = persona_path.stat()
                info["size"] = stat.st_size
                
                # Try to extract title from first line
                with open(persona_path, 'r', encoding='utf-8') as f:
                    first_line = f.readline().strip()
                    if first_line.startswith('# '):
                        info["title"] = first_line[2:].strip()
                    
                    # Try to extract description from second paragraph
                    content = f.read()
                    lines = content.split('\n')
                    for line in lines:
                        line = line.strip()
                        if line and not line.startswith('#') and not line.startswith('-'):
                            info["description"] = line[:200] + "..." if len(line) > 200 else line
                            break
                            
            except Exception as e:
                logger.warning(f"Error reading persona metadata for {persona_name}: {e}")
        
        return info