from collections import deque

class SessionMemory:

    def __init__(self, max_messages: int = 10):
        self.max_messages = max_messages
        self.memory = deque(maxlen=max_messages)

    def add(self, role: str, content: str):

        self.memory.append({
            "role": role,
            "content": content
        })

    def get_context(self):

        context = ""

        for msg in self.memory:
            context += f"{msg['role'].upper()}: {msg['content']}\n"

        return context.strip()

    def clear(self):

        self.memory.clear()

    def get_all(self):
        return list(self.memory)


def create_session_memory(max_messages: int = 10):

    return SessionMemory(max_messages=max_messages)