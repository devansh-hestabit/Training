import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
model = SentenceTransformer("all-MiniLM-L6-v2")

def deduplicate(chunks, similarity_threshold=0.9):
    texts = [c["text"] for c in chunks]
    embeddings = model.encode(texts)

    keep_indices = []
    for i, emb in enumerate(embeddings):
        duplicate = False
        for j in keep_indices:
            sim = cosine_similarity(
                [embeddings[j]],
                [emb]
            )[0][0] #[0][0] is to get the similarity score from the 2D array returned by cosine_similarity
            if sim > similarity_threshold:
                duplicate = True
                break
        if not duplicate:
            keep_indices.append(i)

    return [chunks[i] for i in keep_indices]


def mmr_select(chunks, query, max_chunks=5, lambda_param=0.7):
    texts = [c["text"] for c in chunks]
    embeddings = model.encode(texts)
    query_embedding = model.encode([query])

    selected = []
    selected_indices = []

    similarities = cosine_similarity(embeddings, query_embedding).reshape(-1)

    for _ in range(min(max_chunks, len(chunks))):
        mmr_scores = []

        for i in range(len(chunks)):
            if i in selected_indices:
                continue

            diversity_penalty = 0
            if selected_indices:
                diversity_penalty = max(
                    cosine_similarity(
                        [embeddings[i]],
                        [embeddings[j]]
                    )[0][0]
                    for j in selected_indices
                )

            mmr_score = (
                lambda_param * similarities[i]
                - (1 - lambda_param) * diversity_penalty
            )
            mmr_scores.append((i, mmr_score))

        best_idx = max(mmr_scores, key=lambda x: x[1])[0] #x: x[1] is to get the MMR score from the tuple (index, score)
        selected_indices.append(best_idx)
        selected.append(chunks[best_idx])

    return selected


def build_context(
    query: str,
    reranked_chunks: list,
    max_chunks: int = 5,
    max_chars: int = 3500
):
    unique_chunks = deduplicate(reranked_chunks)

    selected_chunks = mmr_select(
        unique_chunks,
        query,
        max_chunks=max_chunks
    )

    context_blocks = []
    total_chars = 0

    for chunk in selected_chunks:
        block = (
            f"[Source: {chunk['metadata']['source']}, "
            f"Page: {chunk['metadata'].get('page')}]\n"
            f"{chunk['text']}\n"
        )

        if total_chars + len(block) > max_chars:
            break

        context_blocks.append(block)
        total_chars += len(block)

    return "\n---\n".join(context_blocks)


if __name__ == "__main__":
    from src.retriever.hybrid_retriever import hybrid_retrieve
    from src.retriever.reranker import rerank

    query = "Explain how credit underwriting works"

    candidates = hybrid_retrieve(query, top_k=20, filters={"type": "pdf"})
    reranked = rerank(query, candidates, top_k=10)

    context = build_context(query, reranked)

    print("\n===== FINAL CONTEXT =====\n")
    print(context)
