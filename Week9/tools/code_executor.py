import io
import sys
import traceback


class CodeExecutor:
    """
    Code Executor Tool Agent

    Responsibilities:
    - Execute arbitrary Python code
    - Capture stdout output
    - Return execution result or error

    The orchestrator decides:
    - what code to run
    - what data to pass
    """

    def __init__(self):
        # Isolated execution environment
        self.exec_globals = {}

    def run_code(self, code: str, context: dict | None = None):
        """
        Execute Python code dynamically.

        Parameters
        ----------
        code : str
            Python code to execute

        context : dict
            Optional variables injected into execution environment
        """

        if context:
            self.exec_globals.update(context)

        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()

        try:
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
    """
    Factory function for tool creation
    """
    return CodeExecutor()