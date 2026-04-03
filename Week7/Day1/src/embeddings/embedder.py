import os
import pickle
from sentence_transformers import SentenceTransformer #for generating embeddings
 
CHUNKS_PATH = "src/data/chunks/chunks.pkl"
EMBEDDINGS_DIR = "src/data/embeddings"
EMBEDDINGS_PATH = "src/embeddings/embeddings.pkl"

os.makedirs(EMBEDDINGS_DIR, exist_ok=True)
model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings():

    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)

    texts = [c["text"] for c in chunks]
    metadata = [c["metadata"] for c in chunks]

    print(f"Generating embeddings for {len(texts)} chunks")

    embeddings = model.encode(
        texts,
        show_progress_bar=True  #displays a progress bar during embedding generation
    )   

    with open(EMBEDDINGS_PATH, "wb") as f:
        pickle.dump((embeddings, texts, metadata), f)

    print("Embeddings generated and saved")


if __name__ == "__main__":
    generate_embeddings()
