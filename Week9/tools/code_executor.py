import io
import sys
import traceback


def clean_code(code: str) -> str:

    code = code.strip()

    if code.startswith("```"):
        parts = code.split("```")
        if len(parts) >= 2:
            code = parts[1]

    if code.lower().startswith("python"):
        code = code[len("python"):]

    return code.strip()


class CodeExecutor:
    def __init__(self):
        self.exec_globals = {} #stores variables/functions created during execution

    def run_code(self, code: str, context: dict | None = None) -> str:

        if context:
            self.exec_globals.update(context)

        old_stdout = sys.stdout
        buffer = io.StringIO()
        sys.stdout = buffer  #redirects print() output into memory instead of console

        try:
            code = clean_code(code)

            self.exec_globals["__name__"] = "__main__"
            exec(code, self.exec_globals)

            output = buffer.getvalue()

            if not output.strip():
                output = "[No output returned from code execution]"   

        except Exception:
            output = traceback.format_exc()

        finally:

            sys.stdout = old_stdout

        return output


def create_code_executor():
    return CodeExecutor()