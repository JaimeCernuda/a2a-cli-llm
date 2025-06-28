jcernuda@Desktop:~/micro_agent$ uv run python test_data1_agent.py
🎯 Data1.bp Focused Agent Test Suite
============================================================
Testing hyper-focused agent specialized in data1.bp analysis
Server should be running with: uv run python -m server.main --config test_config_data1_agent.yaml --llm

Starting tests...


🎯 Test 1: File Introspection
❓ Question: What variables are in your file?
🤖 Agent Response (26.59s):


**inspect_variables result:**
{
  "nproc": {
    "AvailableStepsCount": "1",
    "Max": "2",
    "Min": "2",
    "Shape": "",
    "SingleValue": "true",
    "Type": "int64_t"
  },
  "physical_time": {
    "AvailableStepsCount": "5",
    "Max": "0.04",
    "Min": "0",
    "Shape": "",
    "SingleValue": "true",
    "Type": "double"
  },
  "pressure": {
    "AvailableStepsCount": "5",
    "Max": "1",
    "Min": "1",
    "Shape": "20",
    "SingleValue": "false",
    "Type": "double"
  },
  "temperature": {
    "AvailableStepsCount": "5",
    "Max": "0",
    "Min": "0",
    "Shape": "20",
    "SingleValue": "false",
    "Type": "double"
  }
}

============================================================
⚠️  UNCLEAR: Path usage not visible in response

🎯 Test 2: Variable Analysis
❓ Question: Tell me about the pressure variable
🤖 Agent Response (1.60s):


**inspect_variables result:**
{
  "nproc": {
    "AvailableStepsCount": "1",
    "Max": "2",
    "Min": "2",
    "Shape": "",
    "SingleValue": "true",
    "Type": "int64_t"
  },
  "physical_time": {
    "AvailableStepsCount": "5",
    "Max": "0.04",
    "Min": "0",
    "Shape": "",
    "SingleValue": "true",
    "Type": "double"
  },
  "pressure": {
    "AvailableStepsCount": "5",
    "Max": "1",
    "Min": "1",
    "Shape": "20",
    "SingleValue": "false",
    "Type": "double"
  },
  "temperature": {
    "AvailableStepsCount": "5",
    "Max": "0",
    "Min": "0",
    "Shape": "20",
    "SingleValue": "false",
    "Type": "double"
  }
}

============================================================
⚠️  UNCLEAR: Path usage not visible in response

🎯 Test 3: Statistical Query
❓ Question: What are the min and max values for temperature?
🤖 Agent Response (1.96s):


**get_min_max result:**
{
  "min": 0.0,
  "max": 0.0
}

============================================================
⚠️  UNCLEAR: Path usage not visible in response

🎯 Test 4: Temporal Analysis
❓ Question: How does physical_time change across timesteps?
🤖 Agent Response (1.68s):


**inspect_variables result:**
{
  "nproc": {
    "AvailableStepsCount": "1",
    "Max": "2",
    "Min": "2",
    "Shape": "",
    "SingleValue": "true",
    "Type": "int64_t"
  },
  "physical_time": {
    "AvailableStepsCount": "5",
    "Max": "0.04",
    "Min": "0",
    "Shape": "",
    "SingleValue": "true",
    "Type": "double"
  },
  "pressure": {
    "AvailableStepsCount": "5",
    "Max": "1",
    "Min": "1",
    "Shape": "20",
    "SingleValue": "false",
    "Type": "double"
  },
  "temperature": {
    "AvailableStepsCount": "5",
    "Max": "0",
    "Min": "0",
    "Shape": "20",
    "SingleValue": "false",
    "Type": "double"
  }
}

============================================================
⚠️  UNCLEAR: Path usage not visible in response

🎯 Test 5: Scientific Interpretation
❓ Question: Compare pressure and temperature and tell me what this simulation represents
🤖 Agent Response (5.77s):


**get_min_max result:**
{
  "step": 0,
  "min": 0.0,
  "max": 0.0
}

**inspect_attributes result:**
{
  "unit": {
    "value": [
      "Pa"
    ],
    "Type": "string",
    "Elements": "1"
  }
}

**inspect_variables result:**
{
  "nproc": {
    "AvailableStepsCount": "1",
    "Max": "2",
    "Min": "2",
    "Shape": "",
    "SingleValue": "true",
    "Type": "int64_t"
  },
  "physical_time": {
    "AvailableStepsCount": "5",
    "Max": "0.04",
    "Min": "0",
    "Shape": "",
    "SingleValue": "true",
    "Type": "double"
  },
  "pressure": {
    "AvailableStepsCount": "5",
    "Max": "1",
    "Min": "1",
    "Shape": "20",
    "SingleValue": "false",
    "Type": "double"
  },
  "temperature": {
    "AvailableStepsCount": "5",
    "Max": "0",
    "Min": "0",
    "Shape": "20",
    "SingleValue": "false",
    "Type": "double"
  }
}

============================================================
⚠️  UNCLEAR: Path usage not visible in response

🏁 Data1.bp Agent Testing Complete!
The focused agent should consistently use the correct file path and provide expert analysis.
