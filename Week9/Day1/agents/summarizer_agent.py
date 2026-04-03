from autogen_agentchat.agents import AssistantAgent
from autogen_core.model_context import BufferedChatCompletionContext


def create_summarizer_agent(model_client):

    system_message = """
You are a Summarizer Agent.

Input: research notes from the Research Agent.

Your job:
- Extract the most important ideas.
- Remove redundant information.
- Create a short structured summary.

Rules:
- Do NOT add new information.
- Do NOT answer the user.

Output format:

SUMMARY
- key idea
- key idea
- key idea
"""

    context = BufferedChatCompletionContext(buffer_size=10)

    return AssistantAgent(
        name="summarizer_agent",
        model_client=model_client,
        system_message=system_message,
        model_context=context,
    )