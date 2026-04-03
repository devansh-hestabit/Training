import sqlite3
from datetime import datetime

class LongTermMemory:

    def __init__(self, db_path: str = "memory/long_term.db"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            type TEXT,
            timestamp TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add(self, content: str, memory_type: str = "fact"):

        query = """
        INSERT INTO memory (content, type, timestamp)
        VALUES (?, ?, ?)
        """

        self.conn.execute(query, (
            content,
            memory_type,
            datetime.utcnow().isoformat()
        ))

        self.conn.commit()

    def get_all(self, limit: int = 10):

        query = """
        SELECT content, type, timestamp
        FROM memory
        ORDER BY id DESC
        LIMIT ?
        """

        cursor = self.conn.execute(query, (limit,))
        return cursor.fetchall()
    
    def clear(self):
        self.conn.execute("DELETE FROM memory")
        self.conn.commit()

    def search(self, keyword: str):

        query = """
        SELECT content FROM memory
        WHERE content LIKE ?
        ORDER BY id DESC
        """

        cursor = self.conn.execute(query, (f"%{keyword}%",))
        return [row[0] for row in cursor.fetchall()]

    def close(self):
        self.conn.close()


def create_long_term_memory():
    return LongTermMemory()