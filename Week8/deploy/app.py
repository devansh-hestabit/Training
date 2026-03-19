import uuid
import logging
import streamlit as st
from typing import List, Dict

from model_loader import load_model
from config import MAX_TOKENS, TEMPERATURE, TOP_P, TOP_K

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

@st.cache_resource
def init_model():
    logger.info("Loading GGUF model...")
    model = load_model()
    logger.info("Model loaded successfully")
    return model

model = init_model()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def build_chat_prompt(system_prompt: str, history: List[Dict], message: str):
    prompt = f"<|system|>\n{system_prompt}\n"

    for turn in history:
        prompt += f"<|user|>\n{turn['user']}\n"
        prompt += f"<|assistant|>\n{turn['assistant']}\n"

    prompt += f"<|user|>\n{message}\n"
    prompt += "<|assistant|>\n"

    return prompt

def format_generate_prompt(user_prompt: str):
    return f"""<|system|>
You are a professional Virtual HR Assistant. Provide helpful answer keeping yourelf at place of user. Be concise and to the point. Avoid unnecessary explanations or filler content. Focus on delivering clear and actionable responses to the user's queries.
<|user|>
{user_prompt}

<|assistant|>
"""

st.set_page_config(page_title="Local LLM UI", layout="wide")

st.title("Local LLM (TinyLlama)")
st.caption("HR Analytics Assistant")

st.sidebar.header("Parameters")

temperature = st.sidebar.slider("Temperature", 0.0, 1.5, 0.3)
top_p = st.sidebar.slider("Top P", 0.0, 1.0, 0.8)
top_k = st.sidebar.slider("Top K", 1, 100, 20)
max_tokens = st.sidebar.slider("Max Tokens", 50, 2048, MAX_TOKENS)

mode = st.sidebar.radio("Mode", ["Chat", "Generate"])

if mode == "Generate":
    st.subheader("Text Generation")

    prompt = st.text_area("Enter Prompt", height=200)

    if st.button("Generate"):
        if prompt.strip():
            request_id = str(uuid.uuid4())
            logger.info(f"Generate request | id={request_id}")

            formatted_prompt = format_generate_prompt(prompt)

            with st.spinner("Generating..."):
                output = model(
                    formatted_prompt,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    top_p=top_p,
                    top_k=top_k,
                    stop=["<|user|>", "<|system|>"] 
                )

            text = output["choices"][0]["text"].strip()

            st.success("Done!")
            st.text_area("Response", text, height=200)

else:
    st.subheader("Chat")

    system_prompt = st.text_area(
        "System Prompt",
        value="You are a Virtual HR Assistant",
        height=100
    )

    for turn in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(turn["user"])
        with st.chat_message("assistant"):
            st.write(turn["assistant"])

    user_input = st.chat_input("Type your message...")

    if user_input:
        request_id = str(uuid.uuid4())
        logger.info(f"Chat request | id={request_id}")

        with st.chat_message("user"):
            st.write(user_input)

        prompt = build_chat_prompt(
            system_prompt,
            st.session_state.chat_history,
            user_input
        )

        with st.spinner("Thinking..."):
            output = model(
                prompt,
                max_tokens=max_tokens,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                stop=["<|user|>", "<|system|>"] 
            )

        text = output["choices"][0]["text"].strip()

        with st.chat_message("assistant"):
            st.write(text)

        st.session_state.chat_history.append({
            "user": user_input,
            "assistant": text
        })

        logger.info(
            f"Chat response | id={request_id} | history={len(st.session_state.chat_history)}"
        )

    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()