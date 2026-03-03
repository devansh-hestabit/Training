import time
import torch
import pandas as pd
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

device = "cuda" if torch.cuda.is_available() else "cpu"

BASE_MODEL = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
MERGED_MODEL = "/content/drive/MyDrive/merged-fp16"

prompts = [
    "Analyze attrition risk for employee age 45 in HR.",
    "Summarize this profile: Age 32, Dept Sales, Salary 6000.",
    "Extract salary and satisfaction from: Age 41, Salary 9000, Satisfaction 4/5.",
    "Predict turnover risk for employee age 29 in Manufacturing.",
    "Explain performance risk for employee with satisfaction 1/5.",
    "List HR metrics from profile: Age 50, Dept R&D, Salary 12000.",
    "Classify attrition probability for age 38, HR manager.",
    "Summarize employee strengths: 10 years experience, satisfaction 5/5.",
    "Identify key risk indicators in this employee record.",
    "Provide structured summary of HR employee profile."
]
def batch_benchmark(model_path, name):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path).to(device)
    model.eval()

    inputs = tokenizer(prompts, return_tensors="pt", padding=True).to(device)

    start = time.time()
    outputs = model.generate(**inputs, max_new_tokens=100)
    end = time.time()

    total_tokens = 0
    for i in range(len(prompts)):
        gen_tokens = outputs[i].shape[0] - inputs["input_ids"][i].shape[0]
        total_tokens += gen_tokens

    total_time = end - start
    tokens_per_sec = total_tokens / total_time

    return {
        "model": name + "_batch",
        "tokens_per_sec": tokens_per_sec,
        "latency_sec": total_time,
        "vram_MB": torch.cuda.max_memory_allocated() / (1024**2) if device=="cuda" else 0
    }

def benchmark_model(model_path, name, use_peft=False):
    print(f"\nRunning benchmark for {name}")
    
    tokenizer = AutoTokenizer.from_pretrained(model_path if not use_peft else BASE_MODEL)
    
    if use_peft:
        model = AutoModelForCausalLM.from_pretrained(BASE_MODEL).to(device)
        model = PeftModel.from_pretrained(model, model_path)
    else:
        model = AutoModelForCausalLM.from_pretrained(model_path).to(device)

    model.eval()

    total_tokens = 0
    total_time = 0
    
    torch.cuda.reset_peak_memory_stats()
    start_vram = torch.cuda.memory_allocated() if device=="cuda" else 0

    for prompt in prompts:
        inputs = tokenizer(prompt, return_tensors="pt").to(device)

        start = time.time()
        outputs = model.generate(**inputs, max_new_tokens=100)
        end = time.time()

        gen_tokens = outputs.shape[1] - inputs["input_ids"].shape[1]
        total_tokens += gen_tokens
        total_time += (end - start)

    end_vram = torch.cuda.max_memory_allocated() if device=="cuda" else 0
    
    tokens_per_sec = total_tokens / total_time
    latency = total_time / len(prompts)

    return {
        "model": name,
        "tokens_per_sec": tokens_per_sec,
        "latency_sec": latency,
        "vram_MB": end_vram / (1024**2)
    }

def multiprompt_benchmark(model_path, name):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path).to(device)
    model.eval()

    total_tokens = 0
    total_time = 0

    for prompt in prompts:
        inputs = tokenizer(prompt, return_tensors="pt").to(device)

        start = time.time()
        outputs = model.generate(**inputs, max_new_tokens=100)
        end = time.time()

        gen_tokens = outputs.shape[1] - inputs["input_ids"].shape[1]
        total_tokens += gen_tokens
        total_time += (end - start)

    return {
        "model": name + "_multiprompt",
        "tokens_per_sec": total_tokens / total_time,
        "latency_sec": total_time / len(prompts),
        "vram_MB": torch.cuda.max_memory_allocated() / (1024**2) if device=="cuda" else 0
    }


results = []

results = []

results.append(benchmark_model(BASE_MODEL, "base_fp16"))
results.append(benchmark_model(MERGED_MODEL, "fine_tuned_fp16"))

results.append(multiprompt_benchmark(BASE_MODEL, "base_fp16"))
results.append(multiprompt_benchmark(MERGED_MODEL, "fine_tuned_fp16"))

results.append(batch_benchmark(BASE_MODEL, "base_fp16"))
results.append({
    "model": "gguf_q8_0",
    "tokens_per_sec": 7.3,
    "latency_sec": None,
    "vram_MB": 1229
})

df = pd.DataFrame(results)
df.to_csv("/content/drive/MyDrive/day4/benchmarks/results.csv", index=False)

print(df)
