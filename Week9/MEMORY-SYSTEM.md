# Memory System Architecture

## Overview

This project implements a memory-enabled AI agent system with three
types of memory:

-   Short-term memory (Session)
-   Vector memory (FAISS)
-   Long-term memory (SQLite)

## Memory Types

### 1. Session Memory (Short-Term)

-   Stores recent conversation history
-   Limited to last N messages
-   Helps maintain conversational context

### 2. Vector Memory (FAISS)

-   Stores embeddings of past interactions
-   Enables similarity-based recall
-   Retrieves relevant past conversations

### 3. Long-Term Memory (SQLite)

-   Persistent storage across sessions
-   Stores summarized facts and insights
-   Supports retrieval even after restart


## Memory Flow

New Query\
↓\
Search Vector Memory (FAISS)\
↓\
Fetch Similar Context\
↓\
Fetch Long-Term Memory\
↓\
Fetch Session Context\
↓\
Inject into Prompt\
↓\
Generate Response\
↓\
Store Back into Memory

## Summarization System

Instead of storing raw text, the system summarizes important facts.

Example:

Input: "I am interested in electronics sales"

Stored as: "User prefers electronics sales"

This improves recall accuracy and reduces noise.

## Memory Control Commands

The system supports runtime memory management:

-   clear memory → Clears all memory layers

## Key Features

-   Multi-layer memory architecture
-   Semantic search using FAISS
-   Persistent storage using SQLite
-   Memory summarization using LLM
-   Context-aware response generation
-   Memory reset and control

## Conclusion

This system demonstrates how modern AI agents use memory to enhance
reasoning and interaction.

By combining: - short-term context - semantic recall - persistent
storage

the agent becomes significantly more intelligent and adaptive.
