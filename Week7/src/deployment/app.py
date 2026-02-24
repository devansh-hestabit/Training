from typing import Dict, List, Optional
from groq import Groq
from src.memory.memory_store import get_conversation, add_message
from src.evaluation.rag_eval import evaluate_answer
from src.retriever.hybrid_retriever import hybrid_retrieve
from src.retriever.reranker import rerank
from src.pipelines.context_builder import build_context
from src.pipelines.sql_pipeline import sql_qa_pipeline
from src.pipelines.image_pipeline import image_search
from src.logging.chat_logger import log_interaction, build_log_entry

client = Groq()
def _generate_llm_answer(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content.strip()

def ask_text(
    session_id: str,
    question: str,
    filters: dict | None = None,
    mode: Optional[str] = None
) -> Dict:

    history = get_conversation(session_id, mode=mode)

    candidates = hybrid_retrieve(
        query=question,
        top_k=10,
        filters=filters
    )

    reranked = rerank(question, candidates, top_k=5)
    context = build_context(question, reranked)

    prompt = f"""
Conversation History:
{history}

Context:
{context}

Answer strictly using the context.
If the answer is not in the context, say "I don't know".

Question:
{question}
"""
    answer = _generate_llm_answer(prompt)

    eval_result = evaluate_answer(
        question=question,
        answer=answer,
        context_chunks=[c["text"] for c in reranked]
    )
    if eval_result["needs_refinement"]:
        refine_prompt = f"""
The previous answer may be inaccurate.
Context:
{context}

Question:
{question}

Provide a more faithful answer grounded strictly in the context.
"""
        answer = _generate_llm_answer(refine_prompt)

    add_message(session_id, "user", question, mode=mode)
    add_message(session_id, "assistant", answer, mode=mode)
    log_interaction(
    build_log_entry(
        session_id=session_id,
        mode=mode or "text",
        user_input=question,
        output=answer,
        confidence=eval_result["confidence_score"],
        faithfulness=eval_result["faithfulness_score"],
        refined=eval_result["needs_refinement"]
    )
)

    return {
        "answer": answer,
        "confidence": eval_result["confidence_score"],
        "faithfulness": eval_result["faithfulness_score"]
    }

def ask_sql(
    session_id: str,
    files: List[str],
    question: str,
    mode: Optional[str] = None
) -> Dict:

    result = sql_qa_pipeline(files, question)
    add_message(session_id, "user", question, mode=mode)
    add_message(session_id, "assistant", result["summary"], mode=mode)

    log_interaction(
        build_log_entry(
            session_id=session_id,
            mode=mode or "sql",
            user_input=question,
            output=result.get("summary", "")
        )
    )

    return result   

def ask_image(
    session_id: str,
    query: str,
    mode: Optional[str] = None
) -> dict:

    result = image_search(query)
    add_message(session_id, "user", query, mode=mode)
    add_message(session_id, "assistant", result.get("description", ""), mode=mode)
    log_interaction(
    build_log_entry(
        session_id=session_id,
        mode=mode or "image",
        user_input=query,
        output=result.get("description", "")
    )
)
    return result