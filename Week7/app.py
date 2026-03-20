from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from pathlib import Path
from src.deployment.app import ask_text, ask_image, ask_sql
from src.memory.memory_store import (
    get_conversation,
    clear_conversation,
)
st.set_page_config(
    page_title="GenAI Capstone",
    layout="wide"
)
if "session_id" not in st.session_state:
    st.session_state.session_id = "streamlit-user"

if "ui_mode" not in st.session_state:
    st.session_state.ui_mode = "Document (Text RAG)"

MODE_MAP = {
    "Document (Text RAG)": "text",
    "Image (Image RAG)": "image",
    "SQL (NL → SQL)": "sql",
}

st.title("GenAI RAG Model")

ui_mode = st.sidebar.radio(
    "Select Mode",
    list(MODE_MAP.keys()),
    index=list(MODE_MAP.keys()).index(st.session_state.ui_mode)
)

st.session_state.ui_mode = ui_mode
st.session_state.mode_id = MODE_MAP[ui_mode]

st.sidebar.markdown("### Recent Chat")

with st.sidebar.expander("Show / Hide Chat Memory", expanded=True):

    if st.button("Clear Chat Memory"):
        clear_conversation(
            st.session_state.session_id,
            st.session_state.mode_id
        )
        st.rerun()

    history = get_conversation(
        session_id=st.session_state.session_id,
        mode=st.session_state.mode_id
    )

    if not history:
        st.caption("No conversation yet.")
    else:
        for i, msg in enumerate(reversed(history), start=1):
            role_label = "You" if msg["role"] == "user" else "AI"
            preview = msg["content"][:80] + ("..." if len(msg["content"]) > 80 else "")

            with st.expander(
                f"{role_label} • {msg['timestamp']} • {preview}",
                expanded=False
            ):
                st.markdown(msg["content"])

if st.session_state.mode_id == "text":

    st.header("Document Question Answering")

    question = st.text_input("Ask a question about your documents")

    if st.button("Ask"):
        result = ask_text(
            session_id=st.session_state.session_id,
            question=question,
            filters={"type": "pdf"},
            mode=st.session_state.mode_id
        )
        st.subheader("Answer")
        st.write(result["answer"])
        col1, col2 = st.columns(2)
        col1.progress(result["confidence"])
        col1.caption(f"Confidence: {int(result['confidence'] * 100)}%")
        col2.progress(result["faithfulness"])
        col2.caption(f"Faithfulness: {int(result['faithfulness'] * 100)}%")

elif st.session_state.mode_id == "image":

    st.header("Image Search")

    query = st.text_input("Enter an image name or description")

    if st.button("Search Image"):
        result = ask_image(
            session_id=st.session_state.session_id,
            query=query,
            mode=st.session_state.mode_id
        )

        if result.get("image_path"):
            st.image(
                result["image_path"],
                caption=result["image_id"],
                use_container_width=True
            )
            st.subheader("Image Description")
            st.write(result["description"])
            # st.caption(f"Similarity score: {round(result['score'], 3)}")
        else:
            st.error("No image found.")

elif st.session_state.mode_id == "sql":

    st.header("Natural Language → SQL")

    UPLOAD_DIR = Path("src/data/sql")
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    uploaded_files = st.file_uploader(
        "Upload CSV or Excel files",
        type=["csv", "xls", "xlsx"],
        accept_multiple_files=True
    )

    question = st.text_input("Ask a question about your data")

    if st.button("Run Query"):

        file_paths = []
        for file in uploaded_files:
            path = UPLOAD_DIR / file.name
            with open(path, "wb") as f:
                f.write(file.getbuffer())
            file_paths.append(str(path))

        result = ask_sql(
            session_id=st.session_state.session_id,
            files=file_paths,
            question=question,
            mode=st.session_state.mode_id
        )

        st.subheader("Generated SQL")
        st.code(result["generated_sql"], language="sql")

        st.subheader("Query Result")
        st.dataframe(result["dataframe"], use_container_width=True)

        st.subheader("Summary")
        st.write(result["summary"])