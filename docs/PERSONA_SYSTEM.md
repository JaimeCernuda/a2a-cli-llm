# A2A CLI Persona System

The A2A CLI now supports customizable AI personas that allow you to configure the agent's behavior, expertise, and communication style through external configuration files.

## 🎭 What are Personas?

Personas are predefined AI character profiles stored as Markdown files that define:
- The agent's role and expertise
- Communication style and approach
- Specific skills and knowledge areas
- Guidelines for responses

## 📁 File Structure

```
personas/
├── default.md      # General helpful assistant
├── developer.md    # Software development expert
├── analyst.md      # Data analyst and researcher
├── teacher.md      # Educational assistant
└── custom.md       # Your custom personas
```

## ⚙️ Configuration

### Basic Usage

In your configuration file (e.g., `config.yaml`):

```yaml
agent:
  name: "My Custom Agent"
  description: "Agent description"
  version: "1.0.0"
  persona: "developer"  # Reference to personas/developer.md
```

### Fallback Behavior

1. **Persona specified**: Loads from `personas/{persona}.md`
2. **Persona missing**: Falls back to `system_prompt` in config
3. **No system_prompt**: Uses default helpful assistant prompt

### Custom Persona Paths

You can also specify a direct path to a persona file:

```yaml
agent:
  persona: "/path/to/my/custom_persona.md"
```

## 📝 Creating Custom Personas

### Persona File Format

Persona files are Markdown documents with the following structure:

```markdown
# Persona Title

Brief description of the persona's role and expertise.

## Core Competencies
- Skill 1: Description
- Skill 2: Description

## Communication Style
- Style guideline 1
- Style guideline 2

## Approach
1. Step 1
2. Step 2
3. Step 3
```

### Example: Custom Research Assistant

Create `personas/researcher.md`:

```markdown
# Research Assistant

You are a meticulous researcher with expertise in academic and industry research methodologies.

## Core Competencies
- **Literature Review**: Finding and analyzing academic papers
- **Data Collection**: Gathering information from multiple sources
- **Citation Management**: Proper academic referencing
- **Synthesis**: Combining findings into coherent insights

## Communication Style
- Cite sources when making claims
- Present both supporting and opposing viewpoints
- Use academic language appropriately
- Acknowledge limitations and uncertainties

## Research Process
1. **Define Scope**: Clarify research questions and objectives
2. **Source Identification**: Find authoritative and relevant sources
3. **Critical Analysis**: Evaluate source credibility and relevance
4. **Synthesis**: Combine findings into actionable insights
5. **Documentation**: Provide proper citations and references
```

## 🚀 Usage Examples

### Start Server with Persona

```bash
# Developer persona
uv run python -m server.main --llm --config config_developer.yaml

# Teacher persona  
uv run python -m server.main --llm --config config_teacher.yaml

# Custom persona
uv run python -m server.main --llm --config config_custom.yaml
```

### Test Different Personas

```bash
# Test persona loading
uv run python demo_persona_loading.py

# Compare persona responses
uv run python test_persona_comparison.py
```

## 🔧 Persona Management

### List Available Personas

```python
from shared.core.persona_loader import PersonaLoader

personas = PersonaLoader.list_available_personas()
print("Available personas:", personas)
```

### Validate Persona

```python
is_valid = PersonaLoader.validate_persona("developer")
print(f"Developer persona valid: {is_valid}")
```

### Get Persona Info

```python
info = PersonaLoader.get_persona_info("developer")
print(f"Title: {info['title']}")
print(f"Description: {info['description']}")
```

## 📋 Built-in Personas

### Default (`default.md`)
- **Role**: General helpful assistant
- **Style**: Professional yet friendly
- **Best for**: General questions, mixed topics

### Developer (`developer.md`)
- **Role**: Expert software developer and architect
- **Style**: Technical, precise, solution-focused
- **Best for**: Code review, architecture, debugging, best practices

### Analyst (`analyst.md`)
- **Role**: Data analyst and researcher
- **Style**: Analytical, evidence-based, structured
- **Best for**: Data analysis, research, business intelligence

### Teacher (`teacher.md`)
- **Role**: Patient educator and tutor
- **Style**: Clear explanations, encouraging, adaptive
- **Best for**: Learning, explanations, educational content

## 🎯 Best Practices

### Designing Effective Personas

1. **Clear Role Definition**: Specify exactly what the persona does
2. **Specific Expertise**: Define clear areas of knowledge and skills
3. **Communication Guidelines**: Set tone, style, and approach
4. **Response Structure**: Provide templates or patterns for responses
5. **Limitations**: Acknowledge what the persona doesn't do

### Configuration Tips

1. **Consistent Naming**: Use descriptive, lowercase names
2. **Version Control**: Track persona changes in git
3. **Documentation**: Document your custom personas
4. **Testing**: Validate personas work as expected
5. **Feedback Loop**: Iterate based on user feedback

### Performance Considerations

1. **File Size**: Keep persona files reasonable (< 5KB recommended)
2. **Complexity**: Avoid overly complex instructions
3. **Caching**: Persona files are loaded once at startup
4. **Fallbacks**: Always provide fallback prompts

## 🔍 Troubleshooting

### Common Issues

1. **Persona Not Found**
   ```
   FileNotFoundError: Persona file not found: personas/custom.md
   ```
   - Verify the file exists in the `personas/` directory
   - Check spelling and file extension (.md)

2. **Empty Persona**
   ```
   WARNING: Persona file is empty: personas/custom.md
   ```
   - Add content to the persona file
   - System will fall back to default prompt

3. **Configuration Not Loading**
   ```
   No persona specified in config
   ```
   - Verify `persona:` field is in the `agent:` section
   - Check YAML syntax and indentation

### Debugging

Enable debug logging to see persona loading:

```yaml
logging:
  level: "debug"
```

Look for log messages:
- `"Loaded persona from: personas/developer.md"`
- `"Loaded persona: developer"`
- `"Falling back to system_prompt from config"`

## 🔮 Advanced Features

### Dynamic Persona Switching

Currently, personas are loaded at startup. Future versions may support:
- Runtime persona switching
- Multi-persona conversations
- Persona inheritance and composition

### Integration with LLM Providers

Different personas can use different provider settings:

```yaml
providers:
  ollama:
    temperature: 0.3  # Lower for developer (precise)
  
  gemini:
    temperature: 0.7  # Higher for teacher (creative)
```

## 📚 Related Documentation

- [Configuration Guide](config.yaml) - LLM provider setup
- [Development Notes](DEVELOPMENT_NOTES.md) - Implementation details
- [Example Configurations](../test_config_*.yaml) - Sample setups