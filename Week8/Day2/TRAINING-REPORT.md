# TRAINING-REPORT

## Goal

The goal of this training was to perform parameter-efficient fine-tuning (QLoRA) on a small open-source LLM to specialize it for HR-focused instruction following, including:
- Employee profile analysis
- Information extraction
- Structured summarization
- Reasoned HR insights


## Base Model

- **Model:** TinyLlama/TinyLlama-1.1B-Chat-v1.0  
- **Architecture:** LLaMA-style decoder-only transformer  
- **Parameters:** ~1.1B  
- **Context Length:** 2048 tokens  

## 3. Fine-Tuning Method

- **Technique:** QLoRA (Quantized Low-Rank Adaptation)
- **Quantization:** 4-bit NF4 (BitsAndBytes)
- **Trainable Parameters:** 1.133% of total parameters
- **Frozen Parameters:** Base model fully frozen
- **Adapter Format:** `safetensors` (modern, safe serialization)

### LoRA Configuration
- Rank (`r`): 16  
- Alpha: 32
- Dropout: 0.05  
- Target Modules:
  - Attention: `q_proj`, `k_proj`, `v_proj`, `o_proj`
  - MLP: `gate_proj`, `up_proj`, `down_proj`

### Dataset Size
- **Training samples:** 3,969  
- **Validation samples:** 441  


## Training Configuration

| Parameter | Value |
|--------|------|
| Epochs | 3 |
| Train Batch Size | 4 |
| Eval Batch Size | 4 |
| Learning Rate | 2e-4 |
| Optimizer | paged_adamw_8bit |
| Gradient Accumulation | 1 |
| Precision | FP32 (AMP disabled for stability) |
| Packing | Disabled |
| Evaluation Strategy | Steps (every 200 steps) |
| Hardware | Google Colab GPU |


## 6. Training Stability Notes

- Mixed precision (FP16/BF16) was **disabled** due to Colab AMP limitations.
- Packing was disabled to avoid attention incompatibilities without FlashAttention.
- Tokenizer PAD/BOS/EOS tokens were automatically aligned with the model config — this is expected and safe.

## 7. Training Results

### Loss Progression (Selected)

| Step | Training Loss | Validation Loss |
|----|--------------|----------------|
| 200 | 0.1864 | 0.1865 |
| 600 | 0.1784 | 0.1784 |
| 1200 | 0.1807 | 0.1777 |
| 1800 | 0.1681 | 0.1769 |
| 2400 | 0.1673 | 0.1752 |
| 2800 | 0.1772 | **0.1748** |

### Final Metrics
- **Final Training Loss:** ~0.179  
- **Final Validation Loss:** ~0.175  
- **Total Steps:** 2,979  
- **Training Time:** ~46 minutes  

### Observations
- Training and validation loss track closely
- No overfitting observed
- Convergence stabilized after ~2 epochs
- Strong domain adaptation achieved

---

## 8. Artifacts Generated

Saved to persistent storage (Google Drive):

```
adapters/
├── adapter_model.safetensors
├── adapter_config.json
├── tokenizer.json
├── tokenizer_config.json
├── chat_template.jinja
├── README.md
```

---

## 9. Inference Verification

Post-training inference confirmed:
- Correct adapter loading via `PeftModel`
- HR-specific structured outputs
- Consistent tone and formatting aligned with training data

---

## 10. Conclusion

This project successfully demonstrates:
- End-to-end QLoRA fine-tuning on limited hardware
- Stable and efficient training with ~1% trainable parameters
- Effective domain adaptation for HR tasks
- Proper handling of modern TRL + PEFT APIs

The resulting model is suitable for:
- Internal HR assistants
- Resume / employee profile analysis
- Structured HR data interpretation
- Further deployment or evaluation work
