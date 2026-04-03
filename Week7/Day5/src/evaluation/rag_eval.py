from typing import List, Dict
import re

def normalize(text: str) -> set:
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]", "", text)
    return set(text.split())

def context_match_score(answer: str, context_chunks: List[str]) -> float:
    if not context_chunks:
        return 0.0

    answer_tokens = normalize(answer)
    context_tokens = set()

    for chunk in context_chunks:
        context_tokens |= normalize(chunk)

    if not answer_tokens:
        return 0.0

    overlap = answer_tokens & context_tokens
    return len(overlap) / len(answer_tokens)

def faithfulness_score(answer: str, context_chunks: List[str]) -> float:
    score = context_match_score(answer, context_chunks)
    if score > 0.6:
        return 1.0
    elif score > 0.3:
        return 0.7
    elif score > 0.1:
        return 0.4
    else:
        return 0.1

def confidence_score(answer: str, context_chunks: List[str]) -> float:

    faith = faithfulness_score(answer, context_chunks)
    length_bonus = min(len(answer.split()) / 100, 0.3)
    return round(min(faith + length_bonus, 1.0), 2)

def needs_refinement(answer: str, context_chunks: List[str]) -> bool:
    return faithfulness_score(answer, context_chunks) < 0.5

def evaluate_answer(
    question: str,
    answer: str,
    context_chunks: List[str]
) -> Dict:
    context_score = context_match_score(answer, context_chunks)
    faithfulness = faithfulness_score(answer, context_chunks)
    confidence = confidence_score(answer, context_chunks)

    return {
        "context_match_score": round(context_score, 2),
        "faithfulness_score": round(faithfulness, 2),
        "confidence_score": confidence,
        "needs_refinement": needs_refinement(answer, context_chunks)
    }