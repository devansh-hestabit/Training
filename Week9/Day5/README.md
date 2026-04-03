# NEXUS AI


## Overview

NEXUS AI is a production-style multi-agent system built to solve complex tasks by:

- Breaking problems into steps
- Assigning tasks to specialized agents
- Executing tools (code, data, files)
- Reflecting and improving results
- Producing clean final outputs


## Architecture

```
User Query
    ↓
Planner
    ↓
Agents (Researcher / Coder / Analyst)
    ↓
Tools (Code Executor / DB Agent)
    ↓
Reflection (Critic → Validator → Optimizer)
    ↓
Reporter (Final Output)
```

## Agents

| Agent | Role |
|------|------|
| Planner | Creates execution plan |
| Researcher | Handles concepts & knowledge |
| Coder | Writes and executes Python code |
| Analyst | Generates insights & strategy |
| Critic | Reviews outputs |
| Optimizer | Improves results |
| Validator | Validates correctness |
| Reporter | Produces final clean output |


## Tools

- **Code Executor** → Executes Python code (data analysis, file handling)
- **DB Agent** → Handles database queries


## How to Run

```bash
python -m nexus_ai.main
```


## Example Queries

- Plan a startup in AI for healthcare  
- Generate backend architecture for scalable app  
- Analyze CSV and provide business insights  
- Design a RAG pipeline for 50k documents  


## Execution Flow

1. User enters query
2. Planner creates step-by-step plan
3. Agents execute tasks
4. Tools run code or queries
5. Reflection improves results (if needed)
6. Reporter generates final output


## Logging

All execution steps are logged in:

```
/logs/nexus.log
```

Includes:
- User queries
- Plans
- Agent outputs
- Final results
