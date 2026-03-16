import sqlite3


class DBAgent:
    """
    Database Tool Agent

    Responsibilities:
    - Connect to SQLite databases
    - Execute arbitrary SQL queries
    - Return structured results

    The orchestrator decides:
    - which database to use
    - what query to execute
    """

    def __init__(self):
        self.connection = None

    def connect(self, db_path: str):
        """
        Connect to a SQLite database
        """
        try:
            self.connection = sqlite3.connect(db_path)
            return f"Connected to database: {db_path}"
        except Exception as e:
            return f"Database connection error: {str(e)}"

    def execute_query(self, query: str):
        """
        Execute a SQL query and return results
        """

        if self.connection is None:
            return "ERROR: No database connected."

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)

            # If query returns rows
            if query.strip().lower().startswith("select"):
                columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()

                results = []
                for row in rows:
                    results.append(dict(zip(columns, row)))

                return {
                    "columns": columns,
                    "row_count": len(results),
                    "rows": results[:50]  # safety limit
                }

            # For INSERT/UPDATE/DELETE
            else:
                self.connection.commit()
                return "Query executed successfully."

        except Exception as e:
            return f"SQL Execution Error: {str(e)}"

    def close(self):
        """
        Close database connection
        """
        if self.connection:
            self.connection.close()
            self.connection = None


def create_db_agent():
    """
    Factory function
    """
    return DBAgent()