# QUANTISATION-REPORT.md

## Goal

The objective of Day 3 was to perform post-training quantisation on a fine-tuned
TinyLlama HR model and evaluate the trade-offs between memory usage, inference speed,
and output quality using GGUF format and llama.cpp.


## 2. Source Model

- **Base Model:** TinyLlama-1.1B-Chat-v1.0  
- **Fine-tuning Method:** QLoRA (HR domain)  
- **Original Precision:** FP16  
- **Runtime:** llama.cpp  


## 3. Quantisation Methods

The following post-training static quantisation formats were evaluated:

| Format | Description |
|------|-------------|
| FP16 | Baseline full-precision GGUF |
| INT8 | 8-bit static quantisation |
| INT4 | 4-bit static quantisation |
| GGUF | llama.cpp runtime format |

> **Note:** The final GGUF model selected for deployment uses **q8_0 (INT8)** quantisation.


## 4. Quantisation Pipeline

1. Merge LoRA adapters into base FP16 model  
2. Convert HuggingFace FP16 model → GGUF  
3. Quantise GGUF using llama.cpp:
   - `q8_0` for INT8
   - `q4_0` for INT4
4. Run inference and measure performance

## 5. Results

### Model Size

| Format | Size |
|------|------|
| FP16 | 2.1 GB |
| INT8 (q8_0) | 1.1 GB |
| INT4 (q4_0) | 608 MB |

### Inference Speed (CPU)

| Format | Generation Speed |
|------|------------------|
| FP16 | ~4.4 tokens/sec |
| INT8 (q8_0) | ~6.5 tokens/sec |
| INT4 (q4_0) | ~10.7 tokens/sec |


### Output Quality (Qualitative)

| Format | Quality |
|------|---------|
| FP16 | Excellent |
| INT8 (q8_0) | Very Good |
| INT4 (q4_0) | Good |


## 6. Observations

- INT8 (q8_0) provides a strong balance between size reduction and reasoning quality
- INT4 (q4_0) offers maximum compression with acceptable quality degradation
- FP16 delivers the highest fidelity but is slow and memory-heavy on CPU
- GGUF enables efficient CPU-only inference via llama.cpp
