from transformers import pipeline


class AnswerAgent:
    def __init__(self):

        self.model = pipeline(
            "text-generation",
            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            max_new_tokens=200
        )

        self.memory = []
        self.memory_limit = 10

        self.system_prompt = """
You are an Answer Agent.

Your job is to produce the final clear answer
for the user using the provided summary.

Rules:
- Provide a clear explanation
- Use the summary information
- Do not repeat research notes
"""

    def update_memory(self, message):

        self.memory.append(message)

        if len(self.memory) > self.memory_limit:
            self.memory.pop(0)

    def answer(self, summary):

        prompt = f"""
{self.system_prompt}

Summary:
{summary}

Final Answer:
"""

        response = self.model(prompt)[0]["generated_text"]

        self.update_memory("answer generated")

        return response