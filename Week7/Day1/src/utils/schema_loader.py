import sqlite3
from pathlib import Path

def load_schema(db_path: str) -> dict:

    db_path = Path(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table'
        AND name NOT LIKE 'sqlite_%';
    """)
    tables = [row[0] for row in cursor.fetchall()]

    schema = {}

    for table in tables:
        cursor.execute(f"PRAGMA table_info({table});")
        columns = cursor.fetchall()

        schema[table] = [
            {
                "name": col[1],
                "type": col[2],
                "primary_key": bool(col[5])
            }
            for col in columns
        ]
    conn.close()
    return schema

def format_schema_for_llm(schema: dict) -> str:
    lines = ["Database Schema:\n"]

    for table, columns in schema.items():
        lines.append(f"Table: {table}")
        for col in columns:
            pk = "PRIMARY KEY" if col["primary_key"] else ""
            lines.append(f"- {col['name']} ({col['type']}) {pk}")
        lines.append("")  

    return "\n".join(lines)