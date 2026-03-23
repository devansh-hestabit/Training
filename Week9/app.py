import streamlit as st
import asyncio

# Import your async pipeline
from nexus_ai.main import run_nexus

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Nexus AI",
    page_icon="🤖",
    layout="wide"
)

# ---------------- SESSION STATE ---------------- #
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- HEADER ---------------- #
st.title("🤖 Nexus AI")
st.caption("Multi-Agent AI System with Planning, Execution & Reflection")

# ---------------- CHAT DISPLAY ---------------- #
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- USER INPUT ---------------- #
user_input = st.chat_input("Ask something...")

if user_input:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # ---------------- RUN PIPELINE ---------------- #
    with st.chat_message("assistant"):
        with st.spinner("🧠 Thinking..."):

            try:
                # Run async function safely inside Streamlit
                response = asyncio.run(run_nexus(user_input))
            except RuntimeError:
                # Fix for event loop already running (Streamlit issue)
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                response = loop.run_until_complete(run_nexus(user_input))

            st.markdown(response)

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})