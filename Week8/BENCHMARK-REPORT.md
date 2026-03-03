# BENCHMARK-REPORT

## 1. Goal

Evaluate and optimise inference performance for:

1. Base TinyLlama FP16 model (GPU)
2. Fine-tuned TinyLlama FP16 model (GPU)
3. Quantised GGUF (q8_0) model using llama.cpp (CPU)


## 2. Experimental Setup

### Hardware

- GPU: NVIDIA (Colab environment)
- CPU: Standard Colab CPU runtime
- Frameworks:
  - Transformers (HF)
  - PEFT
  - llama.cpp (GGUF runtime)

### Models Tested

- Base Model: TinyLlama-1.1B-Chat-v1.0 (FP16)
- Fine-tuned Model: QLoRA merged FP16
- Quantised Model: GGUF q8_0 (INT8)


## 3. Benchmark Methodology

### 3.1 Single Prompt Test

Each model was evaluated using structured HR-related prompts.
Measured:
- Generation time
- Tokens generated
- Tokens/sec
- Peak VRAM usage

### 3.2 Multi-Prompt Test

A set of 10 diverse HR prompts was used to:
- Measure stability
- Validate consistent throughput
- Evaluate generalisation

Metrics recorded:
- Average tokens/sec
- Average latency
- Peak memory

### 3.3 Batch Inference Test (GPU)

Multiple prompts processed simultaneously to evaluate:
- Throughput scaling
- Memory impact

### 3.4 GGUF CPU Benchmark

Using llama.cpp:
- Prompt tokens/sec
- Generation tokens/sec
- Host memory breakdown

Streaming output was validated during generation.


## 4. Results

| Model | Tokens/sec | Latency (s) | Memory (MB) | Hardware | Batch |
|-------|------------|-------------|-------------|----------|-------|
| base_fp16 | 30.95 | 2.59 | 2115 | GPU | No |
| fine_tuned_fp16 | 31.52 | 2.46 | 2115 | GPU | No |
| base_fp16_multiprompt | 29.16 | 2.75 | 2115 | GPU | No |
| fine_tuned_fp16_multiprompt | 31.46 | 2.46 | 2115 | GPU | No |
| base_fp16_batch | 109.01 | 9.17 (batch total) | 2178 | GPU | Yes |
| gguf_q8_0 | 7.30 | — | 1229 | CPU | No |


## 5. Analysis

### 5.1 Fine-Tuned vs Base Model

- Nearly identical throughput
- No inference penalty from LoRA merging
- Same VRAM footprint


### 5.2 Multi-Prompt Stability

Throughput remained stable across varied HR prompts.
This confirms:
- Robust generalisation
- No instability under diverse inputs


### 5.3 Batch Inference Impact

Batch throughput:
~109 tokens/sec

Single prompt throughput:
~31 tokens/sec

Improvement:
~3.5× increase

Trade-off:
- Slight increase in VRAM usage


### 5.4 CPU GGUF (q8_0) Performance

Generation speed:
~7.3 tokens/sec

Memory usage:
~1.2 GB RAM

Compared to GPU FP16:
- Slower throughput
- Much lower hardware requirement
- Suitable for CPU-only deployment


