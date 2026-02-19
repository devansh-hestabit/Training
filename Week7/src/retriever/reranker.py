import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Load embedding model
# -----------------------------
model = SentenceTransformer("all-MiniLM-L6-v2")


def rerank(query: str, candidates: list, top_k: int = 5):
    """
    Reranks retrieved candidates using cosine similarity.

    Args:
        query (str): User query
        candidates (list): Output from hybrid_retriever
        top_k (int): Number of final results

    Returns:
        List of reranked candidates with scores
    """

    if not candidates:
        return []

    # Embed query
    query_embedding = model.encode([query])

    # Embed candidate texts
    candidate_texts = [c["text"] for c in candidates]
    candidate_embeddings = model.encode(candidate_texts)

    # Compute cosine similarity
    scores = cosine_similarity(query_embedding, candidate_embeddings)[0]

    # Attach scores
    for i, score in enumerate(scores):
        candidates[i]["score"] = float(score)

    # Sort by score (higher = better)
    reranked = sorted(
        candidates,
        key=lambda x: x["score"],
        reverse=True
    )

    return reranked[:top_k]


if __name__ == "__main__":
    # Simple standalone test
    from src.retriever.hybrid_retriever import hybrid_retrieve

    query = "Explain how credit underwriting works"

    candidates = hybrid_retrieve(query, top_k=10, filters={"type": "pdf"})
    results = rerank(query, candidates, top_k=5)

    for i, res in enumerate(results, 1):
        print(f"\nRank {i}")
        print(f"Score: {res['score']:.4f}")
        print("Metadata:", res["metadata"])
        print("Text:", res["text"][:400])
