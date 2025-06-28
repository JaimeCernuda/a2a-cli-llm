# ADIOS2 Tool Chaining Solution: Agentic Intelligence for Scientific Computing

## Overview

This document describes the comprehensive solution implemented to enable intelligent tool chaining for ADIOS2 scientific data analysis. The system transforms the A2A CLI from a simple tool executor into a truly agentic entity capable of:

- **Conversation Memory**: Maintaining context across multiple tool invocations
- **Intelligent Parameter Inference**: Automatically suggesting parameters based on previous results
- **Tool Chain Orchestration**: Understanding tool dependencies and prerequisites
- **Error Recovery**: Adapting when tool calls fail by using correct context
- **Scientific Workflow Automation**: Executing complex multi-step analysis autonomously

## Problem Statement

### Initial Limitation
The original system suffered from a critical limitation where the LLM would generate incorrect file paths (e.g., `/home/user/data/bp5_file1.bp5.bp`) instead of using the actual file paths returned by `list_bp5`. This prevented proper chaining of ADIOS2 tools and made complex scientific workflows impossible.

### Root Causes
1. **No Tool Result Context**: LLM didn't maintain context of previous tool results
2. **Static Tool Schema**: Tool descriptions didn't guide result reuse
3. **Missing Conversation Memory**: System didn't preserve tool execution results
4. **Weak Persona Guidance**: Limited instructions for tool chaining behavior

## Solution Architecture

### Core Components

#### 1. Tool Context Management System (`shared/core/tool_context.py`)

**ToolResult Class**: Captures comprehensive tool execution metadata
```python
@dataclass
class ToolResult:
    tool_name: str
    arguments: Dict[str, Any]
    result: Any
    timestamp: datetime
    success: bool
    error_message: Optional[str] = None
    execution_time_ms: float = 0.0
```

**ConversationContext Class**: Maintains conversation-wide context
- Tracks discovered files from `list_bp5` results
- Stores analyzed variables from `inspect_variables` results  
- Provides context summaries for LLM prompting
- Enables intelligent parameter suggestions

**ToolContextManager Class**: Orchestrates intelligent tool behavior
- Suggests parameters based on conversation history
- Detects missing tool prerequisites
- Provides LLM guidance for next steps
- Manages tool dependency chains

#### 2. Enhanced LLM Agent (`shared/core/llm_agent.py`)

**Agentic Execute Method**: Core enhancement enabling intelligent behavior
- Creates conversation contexts with unique IDs
- Builds enhanced system prompts with conversation context
- Handles tool calls with intelligent parameter enhancement
- Maintains persistent memory across interactions

**Key Enhancements**:
```python
async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
    # Create conversation context
    conversation_id = context.context_id or str(uuid.uuid4())
    
    # Enhanced system prompt with context
    enhanced_system_prompt = self._build_enhanced_system_prompt(conversation_id, user_input)
    
    # Agentic tool call handling
    response_text = await self._handle_agentic_tool_calls(llm_response, conversation_id)
```

#### 3. Intelligent Parameter Enhancement

**Smart Parameter Suggestion**: Automatically enhances tool parameters
- File paths: Uses exact paths from `list_bp5` results
- Variable names: Extracts from `inspect_variables` results
- Prerequisites: Ensures tool dependencies are met
- Context reuse: Leverages conversation history

**Example Enhancement**:
```python
# Raw LLM call: inspect_variables(filename="data1.bp")
# Enhanced call: inspect_variables(filename="/home/jcernuda/micro_agent/adios/data/data1.bp")
```

#### 4. Enhanced ADIOS2 Scientist Persona

**Agentic Workflow Guidance**: Explicit instructions for intelligent behavior
- Critical tool chaining rules with exact path usage requirements
- Tool dependency mapping for prerequisite awareness
- Multi-turn conversation strategies for context building
- Error recovery patterns for robust execution

**Key Additions**:
- ⚠️ **ESSENTIAL**: Always use exact file paths returned by tools
- 🔗 **Tool Dependencies**: Clear prerequisite mapping
- 🧠 **Smart Parameter Usage**: Context-aware parameter selection
- 🎯 **Goal-Oriented**: Continue chaining until objectives achieved

### Tool Dependency Graph

```
list_bp5 (discover files)
    ↓
    ├── inspect_variables (analyze structure)
    ├── inspect_attributes (metadata)
    └── read_bp5 (full data)
         ↓
         ├── read_variable_at_step (temporal analysis)
         ├── get_min_max (statistics) 
         └── add_variables (mathematical operations)
```

## Implementation Details

### Conversation Context Flow

1. **Tool Execution**: Each tool call creates a `ToolResult` object
2. **Context Extraction**: Results are analyzed for useful context (files, variables)
3. **Memory Storage**: Context is stored in conversation-specific storage
4. **Parameter Enhancement**: Subsequent tools use stored context for parameters
5. **LLM Guidance**: Enhanced prompts include context and guidance

### Enhanced System Prompting

The system builds dynamic prompts that include:
- **Base Persona**: Scientific domain expertise
- **Conversation Context**: Previously discovered files and variables
- **Tool Guidance**: Next recommended steps based on current state
- **Critical Instructions**: Explicit rules for exact path usage

### Intelligent Error Recovery

When tool calls fail:
1. **Error Analysis**: Determine if it's a path/parameter issue
2. **Context Lookup**: Check conversation history for correct values
3. **Parameter Correction**: Suggest correct paths/variables
4. **Retry Logic**: Enable LLM to retry with correct parameters

## Testing and Validation

### Comprehensive Test Suite (`test_agentic_workflow.py`)

The test suite validates agentic behavior across multiple dimensions:

**Test Categories**:
1. **Basic File Discovery**: Simple `list_bp5` execution
2. **Multi-Step Analysis**: Chained tool execution with path reuse
3. **Context-Aware Follow-up**: Using previous results in new requests
4. **Intelligent Inference**: Automatic parameter suggestion
5. **Complex Workflows**: Multi-tool scientific analysis pipelines

**Agentic Behavior Metrics**:
- **Tool Chaining**: Multiple tools called in sequence
- **Path Reuse**: Exact file paths from previous results
- **Context Awareness**: Reference to previous conversation elements
- **Intelligent Inference**: Successful parameter enhancement

### Expected Success Criteria

✅ **Perfect Tool Chaining**: 100% success rate in file path reuse  
✅ **Scientific Workflow**: Complete ADIOS2 analysis without manual intervention  
✅ **Error Resilience**: Automatic recovery from parameter errors  
✅ **Natural Conversation**: Multi-turn scientific analysis discussions  

## Usage Examples

### Simple Discovery and Analysis
```
User: "Analyze the ADIOS2 dataset in /home/jcernuda/micro_agent/adios/data"

Agent: 
1. Calls list_bp5("/home/jcernuda/micro_agent/adios/data")
2. Discovers ["/home/jcernuda/micro_agent/adios/data/data1.bp", ...]
3. Calls inspect_variables("/home/jcernuda/micro_agent/adios/data/data1.bp")
4. Finds variables: temperature, pressure, physical_time, nproc
5. Provides scientific analysis of the simulation data
```

### Multi-Turn Context-Aware Analysis
```
User: "List all BP5 files"
Agent: [Discovers 3 files, stores in context]

User: "Analyze variables in the first file"  
Agent: [Uses first file from context, analyzes variables, stores results]

User: "Get statistics for the pressure variable"
Agent: [Uses same file + pressure variable from context, calculates statistics]
```

### Complex Scientific Workflow
```
User: "Perform comprehensive temporal analysis of all files"

Agent:
1. list_bp5() → discovers all files
2. For each file: inspect_variables() → analyzes structure  
3. For key variables: get_min_max() → calculates statistics
4. Performs temporal analysis across timesteps
5. Provides scientific insights about simulation dynamics
```

## Benefits Achieved

### 🤖 **True Agentic Behavior**
- Autonomous multi-step task execution
- Intelligent tool sequencing based on dependencies
- Context-aware parameter inference
- Goal-oriented workflow completion

### 🔬 **Enhanced Scientific Capabilities**
- Seamless ADIOS2 data analysis workflows
- Automatic discovery and characterization of scientific datasets
- Intelligent temporal and statistical analysis
- Domain-expert interpretation of results

### 🛠️ **Robust Error Handling**
- Automatic recovery from path/parameter errors
- Context-based parameter correction
- Prerequisite detection and guidance
- Graceful degradation with informative feedback

### 💬 **Natural User Experience**
- Conversational scientific analysis
- Memory of previous discoveries and results
- Progressive workflow building
- Minimal user intervention required

## Future Enhancements

### Advanced Context Intelligence
- Cross-conversation context persistence
- Pattern recognition in scientific workflows
- Predictive tool suggestions based on data characteristics
- Automated hypothesis generation from data patterns

### Enhanced Tool Ecosystem
- Integration with additional scientific computing tools
- Support for visualization and plotting capabilities
- Connection to external databases and repositories
- Collaborative analysis with multiple agents

### Performance Optimization
- Parallel tool execution for independent operations
- Caching of expensive analysis results
- Streaming analysis for large datasets
- Distributed computation support

## Conclusion

The ADIOS2 Tool Chaining Solution transforms the A2A CLI into a truly intelligent agentic system capable of autonomous scientific computing workflows. By implementing conversation memory, intelligent parameter inference, and enhanced domain expertise, we've created a system that can:

- Understand and execute complex multi-step scientific analysis tasks
- Learn from previous interactions and build upon results
- Adapt to errors and recover intelligently
- Provide natural, conversational scientific computing experiences

This foundation enables sophisticated scientific AI agents that can collaborate with researchers to accelerate discovery and insight generation in high-performance computing environments.