from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from pathlib import Path
import pandas as pd
from src.pipelines.sql_pipeline import sql_qa_pipeline

st.set_page_config(page_title="NL2SQL", layout="wide")
st.title("NL 2 SQL")
UPLOAD_DIR = Path("src/data/sql")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
uploaded_files = st.file_uploader(
    "Upload CSV or Excel files",
    type=["csv", "xls", "xlsx"],
    accept_multiple_files=True
)
question = st.text_input(
    "Ask a question about your data (in plain English)"
)
if st.button("Run Query"):

    if not uploaded_files:
        st.error("Please upload at least one file.")
        st.stop()
    if not question:
        st.error("Please enter a question.")
        st.stop()
    file_paths = []
    for file in uploaded_files:
        save_path = UPLOAD_DIR / file.name
        with open(save_path, "wb") as f:
            f.write(file.getbuffer())
        file_paths.append(str(save_path))
    result = sql_qa_pipeline(
        files=file_paths,
        question=question
    )
    st.subheader("Generated SQL")
    st.code(result["generated_sql"], language="sql")
    df = result["dataframe"]
    st.subheader("Query Result")
    st.dataframe(df, use_container_width=True)
    st.download_button(
        label="⬇Download Result as CSV",
        data=df.to_csv(index=False),
        file_name="query_result.csv",
        mime="text/csv"
    )
    st.subheader("Summary")
    st.write(result["summary"])