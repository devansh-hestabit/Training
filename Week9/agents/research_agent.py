from transformers import pipeline


class ResearchAgent:

    def __init__(self):

        self.model = pipeline(
            "text-generation",
            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            max_new_tokens=300
        )

        self.memory = []
        self.memory_limit = 10

        self.system_prompt = """
You are a Research Agent.

Your job is to gather detailed factual information
about a given topic.

Rules:
- Provide research notes
- Provide facts and explanations
- DO NOT summarize
- DO NOT give a final answer
"""

    def update_memory(self, message):

        self.memory.append(message)

        if len(self.memory) > self.memory_limit:
            self.memory.pop(0)

    def research(self, topic):

        prompt = f"""
{self.system_prompt}

Topic:
{topic}

Research Notes:
"""

        response = self.model(prompt)[0]["generated_text"]

        self.update_memory(topic)

        return response
