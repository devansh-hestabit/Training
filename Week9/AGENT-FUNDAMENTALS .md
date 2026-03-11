# AGENT FUNDAMENTALS

## What is an AI Agent?

An AI agent is a system that can: - Perceive information - Reason about
the information - Take an action based on that reasoning

Typical loop:

Perception → Reasoning → Action

Agents can also collaborate with other agents to solve complex problems.


## Agent vs Chatbot vs Pipeline

### Chatbot

A chatbot directly answers a user's question using a single model.

Limitations: - Hard to control behavior - No specialization - Difficult
to scale to complex tasks

### Pipeline System

A pipeline breaks the task into sequential stages.

This improves organization but still lacks intelligent role separation.

### Agent-Based System

Agent systems assign roles to different AI components.

Advantages: - Clear role responsibilities - Easier debugging - Scalable
architecture - Closer to real-world task delegation


## System Architecture

The Day-1 system contains three agents:

### Research Agent

Purpose: Gather information related to the user's query.

Responsibilities: - Collect factual information - Identify key
concepts - Provide detailed research notes

Restrictions: - Does NOT summarize - Does NOT provide final answers

Output: Structured research notes.


### Summarizer Agent

Purpose: Condense the research notes into key insights.

Responsibilities: - Extract important ideas - Remove redundancy -
Produce a concise summary

Restrictions: - Must only use the research notes - Must not add new
information - Must not answer the user directly

Output: Structured summary.


### Answer Agent

Purpose: Generate the final response for the user.

Responsibilities: - Convert the summary into a clear explanation -
Provide a structured answer - Ensure readability and clarity

Restrictions: - Must only use the summary - Must not ask follow-up
questions

Output: Final answer.


## Message-Based Communication

Agents communicate through messages instead of direct function calls.

Example:

User Query ↓ Research Agent (collects information) ↓ Summarizer Agent
(extracts key insights) ↓ Answer Agent (generates final explanation)

This design ensures **clear separation of responsibilities**.

