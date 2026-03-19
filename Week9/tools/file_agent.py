import os
import csv


class FileAgent:


    def __init__(self):
        self.supported_types = [".txt", ".csv"]

    def read_file(self, file_path: str):
        """
        Reads a file and returns its content.
        """

        if not os.path.exists(file_path):
            return f"ERROR: File '{file_path}' not found."

        extension = os.path.splitext(file_path)[1]

        if extension not in self.supported_types:
            return f"ERROR: Unsupported file type '{extension}'."

        if extension == ".txt":
            return self._read_txt(file_path)

        if extension == ".csv":
            return self._read_csv(file_path)

    def _read_txt(self, file_path: str):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def _read_csv(self, file_path: str):
        rows = []

        with open(file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                rows.append(row)

        return {
            "columns": reader.fieldnames,
            "row_count": len(rows),
            "rows": rows[:20]  # limit preview for safety
        }


def create_file_agent():
    """
    Factory method for consistency with your architecture.
    """
    return FileAgent()