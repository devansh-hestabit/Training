# AGENT FUNDAMENTALS 

## What is an AI Agent?

An AI agent is a system that can perceive information, reason about
it, and take actions to achieve a goal.

Typical loop:

Perception → Reasoning → Action

In this project: - The system perceives the user question - Agents
reason about the information - Agents produce outputs that help generate
the final answer

## Agent vs Chatbot vs Pipeline

### Chatbot

A chatbot directly responds to a user query with a single model.

User → Model → Response

### Pipeline

A pipeline processes tasks in sequential steps.

Input → Step1 → Step2 → Step3 → Output

### Agent System

Agent systems use role-based components that communicate and
collaborate.

User → Research Agent → Summarizer Agent → Answer Agent

## Agent Architecture

This system uses three specialized agents:

### 1. Research Agent

Role: - Gather factual information about a topic

Responsibilities: - Generate research notes - Provide facts and
explanations - Avoid summarizing or answering the final question

### 2. Summarizer Agent

Role: - Compress research notes into a clear summary

Responsibilities: - Extract key information - Reduce length of research
output - Avoid adding new information

### 3. Answer Agent

Role: - Generate the final response for the user

Responsibilities: - Use the summary - Produce a clear explanation -
Avoid repeating research notes

## Message-Based Communication

Agents communicate through a structured message flow.

User Question ↓ Research Agent ↓ Summarizer Agent ↓ Answer Agent ↓ Final
Answer

Each agent receives the output of the previous agent.

## System Prompts

Each agent has its own system prompt defining its role.

Examples:

Research Agent Prompt: "You are a Research Agent. Your job is to gather
factual information about a topic."

Summarizer Agent Prompt: "You are a Summarizer Agent. Your job is to
compress research notes into a summary."

Answer Agent Prompt: "You are an Answer Agent. Your job is to generate
the final explanation for the user."

System prompts enforce role isolation.
