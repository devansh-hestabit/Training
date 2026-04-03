import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

EMBEDDINGS_PATH = "src/embeddings/embeddings.pkl"
FAISS_INDEX_PATH = "src/vectorstore/index.faiss"

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index(FAISS_INDEX_PATH)

with open(EMBEDDINGS_PATH, "rb") as f:
    embeddings, texts, metadata = pickle.load(f)

def retrieve(query: str, top_k: int = 5):

    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, top_k)
    results = []

    for rank, idx in enumerate(indices[0]):
        results.append({
            "rank": rank + 1,
            "distance": float(distances[0][rank]),#convert numpy float to regular float for better readability
            "text": texts[idx],
            "metadata": metadata[idx]
        })

    return results

if __name__ == "__main__":
    query_text = "What is name of company?"
    results = retrieve(query_text)

    for res in results:
        print(f"\nRank: {res['rank']}")
        print(f"Distance (L2 score): {res['distance']:.4f}")
        print("Metadata:", res["metadata"])
        print("Text:", res["text"][:500]) #print only the first 500 characters of the retrieved text for better readability

