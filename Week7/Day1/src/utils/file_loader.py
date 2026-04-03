import pandas as pd
import sqlite3
from pathlib import Path


def load_files_to_sqlite(
    file_paths: list[str],
    db_dir: str = "src/data/sql",
    db_name: str = "sqlite.db"
) -> str:
    db_dir = Path(db_dir)
    db_dir.mkdir(parents=True, exist_ok=True)

    db_path = db_dir / db_name
    conn = sqlite3.connect(db_path)

    for file_path in file_paths:
        file_path = Path(file_path)
        table_name = file_path.stem.lower().replace(" ", "_")

        if file_path.suffix.lower() == ".csv":
            df = pd.read_csv(file_path)
            df = pd.read_csv(file_path)
            df.columns = (
                df.columns
                .str.strip()
                .str.lower()
                .str.replace(" ", "_")
                .str.replace(".", "_")
            )

        elif file_path.suffix.lower() in [".xls", ".xlsx"]:
            df = pd.read_excel(file_path)
            df.columns = (df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(".", "_"))       

        else:
            raise ValueError(
                f"Unsupported file type: {file_path.suffix}"
            )

        df.to_sql(
            name=table_name,
            con=conn,
            if_exists="replace",
            index=False
        )

    conn.close()
    return str(db_path)