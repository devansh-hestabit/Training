import uuid
import logging
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
from deploy.model_loader import load_model
from deploy.config import MAX_TOKENS, TEMPERATURE, TOP_P, TOP_K


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Local LLM API",
    description="Quantized TinyLlama API for HR analytics",
    version="1.0"
)

logger.info("Loading GGUF model...")

model = load_model()

logger.info("Model loaded successfully")

class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: int = MAX_TOKENS
    temperature: float = TEMPERATURE
    top_p: float = TOP_P
    top_k: int = TOP_K


class ChatRequest(BaseModel):
    system_prompt: str
    message: str
    temperature: float = TEMPERATURE
    top_p: float = TOP_P
    top_k: int = TOP_K
    max_tokens: int = MAX_TOKENS

chat_history: List[Dict] = []

def build_chat_prompt(system_prompt: str, history: List[Dict], message: str):

    prompt = f"<|system|>\n{system_prompt}\n"

    for turn in history:
        prompt += f"<|user|>\n{turn['user']}\n"
        prompt += f"<|assistant|>\n{turn['assistant']}\n"

    prompt += f"<|user|>\n{message}\n"
    prompt += "<|assistant|>\n"

    return prompt

@app.post("/generate")
def generate(req: GenerateRequest):

    request_id = str(uuid.uuid4())

    logger.info(f"Generate request received | id={request_id}")

    output = model(
        req.prompt,
        max_tokens=req.max_tokens,
        temperature=req.temperature,
        top_p=req.top_p,
        top_k=req.top_k
    )

    text = output["choices"][0]["text"]

    logger.info(f"Generation completed | id={request_id}")

    return {
        "request_id": request_id,
        "response": text.strip()
    }

@app.post("/chat")
def chat(req: ChatRequest):

    global chat_history

    request_id = str(uuid.uuid4())

    logger.info(f"Chat request received | id={request_id}")

    prompt = build_chat_prompt(
        req.system_prompt,
        chat_history,
        req.message
    )

    output = model(
        prompt,
        max_tokens=req.max_tokens,
        temperature=req.temperature,
        top_p=req.top_p,
        top_k=req.top_k
    )

    text = output["choices"][0]["text"].strip()

    chat_history.append({
        "user": req.message,
        "assistant": text
    })

    logger.info(
        f"Chat response generated | id={request_id} | history={len(chat_history)}"
    )

    return {
        "request_id": request_id,
        "response": text,
        "history_length": len(chat_history)
    }
@app.get("/health")
def health():
    return {"status": "running"}