from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext


def create_answer_agent(model_client):

    system_message = """
You are the Answer Agent.

Input: a summary from the Summarizer Agent.

Your job:
- Generate the final answer for the user.
- Explain the topic clearly.

Rules:
- Use only the provided summary.
- Do NOT ask questions.
- Do NOT request more information.

Output format:

FINAL ANSWER
<clear explanation>
"""

    context = BufferedChatCompletionContext(buffer_size=10)

    return AssistantAgent(
        name="answer_agent",
        model_client=model_client,
        system_message=system_message,
        model_context=context,
    )