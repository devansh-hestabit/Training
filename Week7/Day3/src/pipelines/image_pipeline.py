# src/pipelines/image_pipeline.py

from groq import Groq
from src.retriever.image_search import text_to_image

client = Groq()


def _describe_image_with_llm(query: str, metadata: dict) -> str:
    """
    Generate a natural language description for the retrieved image.
    """

    prompt = f"""
You are a vision assistant.

User searched for: "{query}"

Image metadata:
{metadata}

Describe what the image most likely contains in clear, natural language.
Do not invent details beyond what the metadata implies.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()


def image_search(query: str) -> dict:
    """
    Product-style image search.
    Returns ONLY ONE best image + LLM description.
    """

    results = text_to_image(query, top_k=1)

    if not results:
        return {
            "image_path": None,
            "description": "No relevant image found."
        }

    best = results[0]

    description = _describe_image_with_llm(
        query=query,
        metadata=best.get("metadata", {})
    )

    return {
        "image_id": best["image_id"],
        "image_path": best["image_path"],
        "score": best["score"],
        "description": description
    }