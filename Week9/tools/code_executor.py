import io
import sys
import traceback

def clean_code(code: str):
    # remove markdown fences
    code = code.strip()

    if code.startswith("```"):
        code = code.split("```")[1]

    # remove possible language tag
    code = code.replace("python", "", 1)

    return code.strip()

class CodeExecutor:
    def __init__(self):
        self.exec_globals = {}
    def run_code(self, code: str, context: dict | None = None):
        if context:
            self.exec_globals.update(context)
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        try:
            code = clean_code(code)
            exec(code, self.exec_globals)
            output = buffer.getvalue()
            if output.strip() == "":
                output = "Code executed successfully."
        except Exception:
            output = traceback.format_exc()
        finally:
            sys.stdout = old_stdout
        return output
def create_code_executor():
    return CodeExecutor()