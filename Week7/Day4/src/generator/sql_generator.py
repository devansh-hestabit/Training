from groq import Groq
client = Groq()

def generate_sql(
    question: str,
    schema_text: str,
    model: str = "llama-3.3-70b-versatile"
) -> str:
    prompt = f"""
You are an expert SQL analyst.

Database schema:
{schema_text}

Rules:
- Generate ONLY one SQL query
- Query must start with SELECT
- Do NOT use DELETE, UPDATE, INSERT, DROP, ALTER
- Use only tables and columns from the schema
- No explanations, comments, or markdown

Question:
{question}
"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    sql = response.choices[0].message.content.strip()
    return sql