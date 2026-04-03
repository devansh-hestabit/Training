import os
import csv


class FileAgent:

    def __init__(self):
        self.supported_types = [".txt", ".csv"]

    def read_file(self, file_path: str):
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

    def _convert_value(self, value):

        try:
            return int(value)
        except:
            pass

        try:
            return float(value)
        except:
            pass
        
        return value
    
    
    def _read_csv(self, file_path: str):
        rows = []
    
        with open(file_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file) #convert each row into dictionary
    
            for row in reader:
                converted_row = {
                    key: self._convert_value(value)
                    for key, value in row.items()
                }
                rows.append(converted_row)
    
        return {
            "columns": reader.fieldnames,
            "row_count": len(rows),
            "rows": rows[:20]  # preview
        }


def create_file_agent():

    return FileAgent()