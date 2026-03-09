from transformers import pipeline


class SummarizerAgent:

    def __init__(self):

        self.model = pipeline(
            "text-generation",
            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            max_new_tokens=200
        )

        self.memory = []
        self.memory_limit = 10

        self.system_prompt = """
You are a Summarizer Agent.

Your job is to convert research notes into a clear summary.

Rules:
- Keep the information accurate
- Compress the information
- Do NOT introduce new facts
- Do NOT answer the user's question
"""

    def update_memory(self, message):

        self.memory.append(message)

        if len(self.memory) > self.memory_limit:
            self.memory.pop(0)

    def summarize(self, research_notes):

        prompt = f"""
{self.system_prompt}

Research Notes:
{research_notes}

Summary:
"""

        response = self.model(prompt)[0]["generated_text"]

        self.update_memory("summary created")

        return response

