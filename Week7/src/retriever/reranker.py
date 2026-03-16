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
        key=lambda x: x["score"], #sort candidates based on their similarity score to the query
        reverse=True
    )
    return reranked[:top_k]