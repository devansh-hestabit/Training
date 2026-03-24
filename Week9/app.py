import streamlit as st
import asyncio
from nexus_ai.main import run_nexus


st.set_page_config(
    page_title="Nexus AI",
    page_icon="🤖",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Nexus AI")
st.caption("Multi-Agent AI System with Planning, Execution & Reflection")


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask something...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            try:

                response = asyncio.run(run_nexus(user_input))
            except RuntimeError:
  
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                response = loop.run_until_complete(run_nexus(user_input))

            st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

    