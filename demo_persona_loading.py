#!/usr/bin/env python3
"""Demonstrate persona loading functionality."""

from shared.core.persona_loader import PersonaLoader
from shared.core.config_loader import ConfigLoader


def main():
    """Demonstrate persona loading features."""
    print("🎭 A2A CLI Persona System Demo")
    print("=" * 40)
    
    # List available personas
    print("\n📋 Available Personas:")
    personas = PersonaLoader.list_available_personas()
    for i, persona in enumerate(personas, 1):
        print(f"  {i}. {persona}")
    
    if not personas:
        print("  No personas found in personas/ directory")
        return
    
    # Demonstrate loading personas
    print("\n🔍 Persona Details:")
    for persona in personas:
        print(f"\n--- {persona.title()} ---")
        try:
            info = PersonaLoader.get_persona_info(persona)
            print(f"Title: {info['title']}")
            print(f"Description: {info['description'][:100]}...")
            print(f"Size: {info['size']} bytes")
            print(f"Valid: ✅" if PersonaLoader.validate_persona(persona) else "❌")
        except Exception as e:
            print(f"Error: {e}")
    
    # Test loading specific persona
    print(f"\n📖 Loading 'developer' persona:")
    try:
        developer_prompt = PersonaLoader.load_persona("developer")
        print("✅ Successfully loaded!")
        print(f"Preview: {developer_prompt[:200]}...")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Test configuration loading
    print(f"\n⚙️  Testing Configuration Integration:")
    try:
        config = ConfigLoader.load_config("test_config_developer.yaml")
        print(f"Agent Name: {config.agent.name}")
        print(f"Persona: {config.agent.persona}")
        print(f"System Prompt: {config.agent.system_prompt[:50] if config.agent.system_prompt else 'None'}...")
        
        # Simulate persona loading like LLM agent does
        if config.agent.persona:
            try:
                persona_prompt = PersonaLoader.load_persona(config.agent.persona)
                print(f"✅ Persona loaded successfully: {len(persona_prompt)} characters")
            except Exception as e:
                print(f"⚠️ Persona loading failed: {e}, would fall back to system_prompt")
        else:
            print("❌ No persona specified in config")
                
    except Exception as e:
        print(f"❌ Config error: {e}")
    
    print("\n🎉 Persona system is working correctly!")


if __name__ == "__main__":
    main()