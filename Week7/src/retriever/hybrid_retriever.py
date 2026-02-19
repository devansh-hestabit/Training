import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from rank_bm25 import BM25Okapi

EMBEDDINGS_PATH = "src/embeddings/embeddings.pkl"
FAISS_INDEX_PATH = "src/vectorstore/index.faiss"
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
faiss_index = faiss.read_index(FAISS_INDEX_PATH)

with open(EMBEDDINGS_PATH, "rb") as f:
    embeddings, texts, metadata = pickle.load(f)

tokenized_texts = [t.lower().split() for t in texts]
bm25 = BM25Okapi(tokenized_texts)
def apply_filters(indices, filters):
    if not filters:
        return indices

    filtered = []
    for idx in indices:
        meta = metadata[idx]
        keep = True 

        for key, value in filters.items():
            if key not in meta or str(meta[key]) != str(value):
                keep = False
                break

        if keep:
            filtered.append(idx)

    return filtered

def hybrid_retrieve(
    query: str,
    top_k: int = 5,
    filters: dict | None = None
):
    
    query_embedding = embedding_model.encode([query]).astype("float32")
    _, semantic_indices = faiss_index.search(query_embedding, top_k * 2) #_ is for distances which we don't need here
    semantic_indices = semantic_indices[0].tolist() 
    semantic_indices = apply_filters(semantic_indices, filters)

    query_tokens = query.lower().split()
    bm25_scores = bm25.get_scores(query_tokens)
    keyword_indices = np.argsort(bm25_scores)[::-1][: top_k * 2].tolist() #[::-1] is for sorting in descending order and [: top_k * 2] is to get the top K results

    keyword_indices = apply_filters(keyword_indices, filters)
    
    combined_indices = list(dict.fromkeys(semantic_indices + keyword_indices)) #dict.fromkeys is used to remove duplicates while preserving order

    candidates = []
    for idx in combined_indices:
        candidates.append({
            "text": texts[idx],
            "metadata": metadata[idx],
            "source": metadata[idx].get("source"),
            "chunk_id": idx
        })

    return candidates[: top_k * 2]


if __name__ == "__main__":
    query = "Explain how credit underwriting works"
    filters = {"type": "pdf"}

    results = hybrid_retrieve(query, top_k=5, filters=filters)

    for i, res in enumerate(results, 1):
        print(f"\nCandidate {i}")
        print("Source:", res["source"])
        print("Metadata:", res["metadata"])
        print("Text:", res["text"][:400])
