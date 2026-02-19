from src.retriever.hybrid_retriever import hybrid_retrieve
from src.retriever.reranker import rerank
from src.pipelines.context_builder import build_context

def run():
    print("Type your question (or 'exit' to quit)\n")

    while True:
        query = input("User Query: ").strip()

        if query.lower() in ["exit", "quit"]:
            print("\nExiting system.")
            break

        if not query:
            print("Please enter a valid query.")
            continue

        candidates = hybrid_retrieve(
            query=query,
            top_k=10,
            filters={"type": "pdf"}  
        )
        reranked = rerank(query, candidates, top_k=10)
        context = build_context(query, reranked)

        print("\nFINAL CONTEXT\n")
        print(context)

if __name__ == "__main__":
    run()
