import os
import pickle
from langchain_text_splitters import RecursiveCharacterTextSplitter #for chunking
from src.utils.doc_load import load_document

RAW_DATA_DIR = "src/data/raw"
CHUNKS_OUTPUT_PATH = "src/data/chunks/chunks.pkl"

os.makedirs("src/data/chunks", exist_ok=True)
splitter = RecursiveCharacterTextSplitter(
    chunk_size=700,
    chunk_overlap=100
)

def run_ingestion():
    all_chunks = []

    for filename in os.listdir(RAW_DATA_DIR):
        file_path = os.path.join(RAW_DATA_DIR, filename)

        if not os.path.isfile(file_path):
            continue

        records = load_document(file_path)

        for record in records:
            text = record["text"]
            metadata = record["metadata"]

            chunks = splitter.split_text(text)

            for chunk in chunks:
                all_chunks.append({
                    "text": chunk,
                    "metadata": metadata
                })

    with open(CHUNKS_OUTPUT_PATH, "wb") as f: #wb for writing in binary mode
        pickle.dump(all_chunks, f)

    print(f"Ingestion completed")
    print(f"Total chunks created: {len(all_chunks)}")


if __name__ == "__main__":
    run_ingestion()
