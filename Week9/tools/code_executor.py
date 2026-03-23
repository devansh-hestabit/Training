import io
import sys
import traceback


def clean_code(code: str) -> str:
    """
    Cleans LLM-generated code by removing markdown fences
    and language tags.
    """
    code = code.strip()

    # Remove markdown ``` blocks
    if code.startswith("```"):
        parts = code.split("```")
        if len(parts) >= 2:
            code = parts[1]

    # Remove optional 'python' tag
    if code.lower().startswith("python"):
        code = code[len("python"):]

    return code.strip()


class CodeExecutor:
    def __init__(self):
        # Persistent execution environment
        self.exec_globals = {}

    def run_code(self, code: str, context: dict | None = None) -> str:
        """
        Executes Python code safely and captures stdout.
        """

        # Inject external context if provided
        if context:
            self.exec_globals.update(context)

        old_stdout = sys.stdout
        buffer = io.StringIO()
        sys.stdout = buffer

        try:
            code = clean_code(code)

            # Execute code
            exec(code, self.exec_globals)

            # Capture output
            output = buffer.getvalue()

            # If nothing printed, return explicit message
            if not output.strip():
                output = "[No output returned from code execution]"

        except Exception:
            output = traceback.format_exc()

        finally:
            # Restore stdout
            sys.stdout = old_stdout

        return output


def create_code_executor():
    return CodeExecutor()