# FINAL REPORT - HR Analytics LLM Microservice

## Project Overview

This project implements a complete local LLM pipeline, starting from
dataset preparation and model fine‑tuning to quantisation, benchmarking,
and deployment of a production‑ready LLM microservice

The final system serves a quantised TinyLlama model through a FastAPI-based local API, enabling both prompt-based generation and
multi‑turn conversational interaction.

The project demonstrates practical LLM engineering skills including:

-   Instruction dataset design
-   Parameter‑efficient fine‑tuning
-   Model quantisation
-   Inference benchmarking
-   API deployment


## System Architecture

Client\
↓\
FastAPI API Server\
↓\
Quantised GGUF LLM Model (TinyLlama)\
↓\
Generated Response

The API acts as a lightweight LLM inference server that can be
extended for:

-   Retrieval‑Augmented Generation (RAG)
-   AI agents
-   Enterprise AI assistants
-   Chat interfaces


## Model Training

The base model used:

TinyLlama‑1.1B

The model was fine‑tuned using QLoRA (Quantized Low‑Rank Adaptation)
which enables efficient training while updating only a small portion of
model parameters.

Training configuration:

-   LoRA Rank: 16
-   Learning Rate: 2e‑4
-   Batch Size: 4
-   Epochs: 3
-   4‑bit loading

This approach reduces GPU memory requirements while maintaining strong
performance.


## Model Quantisation

To improve inference efficiency, the fine‑tuned model was quantised into
several formats.

Formats generated:

FP16 -- Full precision merged model\
INT8 -- Moderate compression\
INT4 -- High compression\
GGUF (q8_0) -- Optimised format for llama.cpp

Approximate model sizes:

FP16 ≈ 2.1 GB\
q8_0 ≈ 1.1 GB\
q4_0 ≈ 608 MB

The GGUF q8_0 model was used for deployment due to its balance
between performance and output quality.


## Inference Benchmarking

Several inference configurations were tested.

Metrics measured:

-   Tokens per second
-   Latency
-   Memory usage

Example results:

Base FP16 model ≈ 30 tokens/sec\
Fine‑tuned FP16 model ≈ 31 tokens/sec\
Quantised GGUF model ≈ 7 tokens/sec (CPU inference)

Batch inference demonstrated higher throughput when processing multiple
prompts simultaneously.

## API Deployment

A FastAPI server was developed to expose the model as a local LLM
service.

Endpoints implemented:

POST /generate
POST /chat

### Generate Endpoint

Used for single prompt completion with configurable parameters.

Example request:

{ "prompt": "Summarize this employee profile", "max_tokens": 100,
"temperature": 0.7, "top_p": 0.9, "top_k": 40 }

![API Docs](screenshots/generate.png)

### Chat Endpoint

Supports conversational interaction including:

-   System prompts
-   User messages
-   Persistent chat history

Example request:

{ "system_prompt": "You are an HR analytics assistant", "message":
"Analyze attrition risk for employee age 45", "temperature": 0.7 }

Additional features:

-   Request ID logging
-   Sampling controls
-   Model caching at startup
-   Infinite chat mode

![API Docs](screenshots/chat_1.png)
![API Docs](screenshots/chat_2.png)


## Deployment Environment

The API runs locally using:

FastAPI + Uvicorn

A Dockerfile is also provided to run the system inside a container
for easier deployment.

## Logging
The API includes logging of request IDs and inference times for monitoring and debugging purposes.
![API Logs](screenshots/logging.png)