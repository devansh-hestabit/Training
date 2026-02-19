import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def rerank(query: str, candidates: list, top_k: int = 5):
    if not candidates:
        return []

    query_embedding = model.encode([query])
    candidate_texts = [c["text"] for c in candidates]
    candidate_embeddings = model.encode(candidate_texts)
    scores = cosine_similarity(query_embedding, candidate_embeddings)[0]

    for i, score in enumerate(scores):
        candidates[i]["score"] = float(score)
    reranked = sorted(
        candidates,
        key=lambda x: x["score"],
        reverse=True
    )
    return reranked[:top_k]

if __name__ == "__main__":
    from src.retriever.hybrid_retriever import hybrid_retrieve

    query = "Explain how credit underwriting works"

    candidates = hybrid_retrieve(query, top_k=10, filters={"type": "pdf"})
    results = rerank(query, candidates, top_k=5)

    for i, res in enumerate(results, 1):
        print(f"\nRank {i}")
        print(f"Score: {res['score']:.4f}")
        print("Metadata:", res["metadata"])
        print("Text:", res["text"][:400])
