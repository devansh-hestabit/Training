import streamlit as st
import asyncio
from nexus_ai.main import run_nexus

st.set_page_config(
    page_title="Nexus AI",
    page_icon="🤖",
    layout="wide"
)

with st.sidebar:
    st.title("🤖 Nexus AI")
    st.markdown("Multi-Agent AI System")
    st.divider()

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.caption("Built with Planning • Execution • Reflection")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown(
    """
    <h1 style='text-align: center;'>🤖 Nexus AI</h1>
    <p style='text-align: center; color: gray;'>
    Multi-Agent AI with Planner • Coder • Analyst • Critic
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

chat_container = st.container()

with chat_container:
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(msg["content"])
        else:
            with st.chat_message("assistant"):
                st.markdown(msg["content"])

user_input = st.chat_input("Ask Nexus anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()

        with st.spinner("🧠 Nexus is thinking..."):
            try:
                response = asyncio.run(run_nexus(user_input))
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                response = loop.run_until_complete(run_nexus(user_input))

        displayed_text = ""
        for chunk in response.split():
            displayed_text += chunk + " "
            response_placeholder.markdown(displayed_text)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )