import os
import pandas as pd
from pypdf import PdfReader
from docx import Document


def clean_text(text: str) -> str:
    if not text:
        return ""
    text = text.replace("\n", " ").replace("\t", " ")
    return " ".join(text.split())


def load_document(file_path: str):
    records = []
    filename = os.path.basename(file_path)

    if file_path.lower().endswith(".pdf"):
        reader = PdfReader(file_path)
        for page_num, page in enumerate(reader.pages):
            text = clean_text(page.extract_text() or "")
            if text:
                records.append({
                    "text": text,
                    "metadata": {
                        "source": filename,
                        "page": page_num + 1,
                        "type": "pdf",
                        "tags": []
                    }
                })

    elif file_path.lower().endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = clean_text(f.read())
            if text:
                records.append({
                    "text": text,
                    "metadata": {
                        "source": filename,
                        "page": None,
                        "type": "txt",
                        "tags": []
                    }
                })
    elif file_path.lower().endswith(".docx"):
        doc = Document(file_path)
        for i, para in enumerate(doc.paragraphs):
            text = clean_text(para.text)
            if text:
                records.append({
                    "text": text,
                    "metadata": {
                        "source": filename,
                        "page": i + 1,
                        "type": "docx",
                        "tags": []
                    }
                })

    elif file_path.lower().endswith(".csv"):
        df = pd.read_csv(file_path)
        for row_idx, row in df.iterrows():
            text = clean_text(row.to_string())
            if text:
                records.append({
                    "text": text,
                    "metadata": {
                        "source": filename,
                        "page": row_idx, 
                        "type": "csv",
                        "tags": []
                    }
                })

    return records
