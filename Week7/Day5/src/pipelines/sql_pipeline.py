import sqlite3 
import pandas as pd 
from groq import Groq
from Week7.Day5.src.utils.file_loader import load_files_to_sqlite
from Week7.Day5.src.utils.schema_loader import load_schema, format_schema_for_llm
from Week7.Day5.src.generator.sql_generator import generate_sql

client = Groq()

FORBIDDEN_KEYWORDS = [
    "DROP", "DELETE", "INSERT", "UPDATE", "ALTER",
    "TRUNCATE", "REPLACE", "ATTACH", "DETACH"
]

def validate_sql(sql: str) -> None:
    sql_upper = sql.upper()

    if not sql_upper.startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed.")

    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in sql_upper:
            raise ValueError(f"Unsafe SQL detected: {keyword}")


def execute_sql(sql: str, db_path: str) -> pd.DataFrame:

    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(sql, conn)
    conn.close()
    return df


def summarize_result(df: pd.DataFrame) -> str:

    preview = df.head(20).to_markdown(index=False)

    prompt = f"""
You are a data analyst.

Summarize the following SQL query result in clear business language.
Highlight key insights, totals, trends, or comparisons if visible.

Result Table:
{preview}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3 #temperature is for creativity
    )
    return response.choices[0].message.content.strip()

def sql_qa_pipeline(files: list[str], question: str) -> dict:

    db_path = load_files_to_sqlite(files)
    schema = load_schema(db_path)
    schema_text = format_schema_for_llm(schema)
    sql = generate_sql(question, schema_text)
    validate_sql(sql)
    df = execute_sql(sql, db_path)
    summary = summarize_result(df)
    return {
        "generated_sql": sql,
        "dataframe": df,
        "summary": summary
    }