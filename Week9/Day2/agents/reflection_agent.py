from autogen_agentchat.agents import AssistantAgent


def create_reflection_agent(model_client):

    system_message = """
You are a Reflection Agent.

Your job:
- Improve the results from worker agents.
- Identify missing ideas.
- Make the explanation clearer.

Rules:
- Refine the worker output.
- Do not invent unrelated information.

Output format:

IMPROVED RESULT
- improved explanation
"""

    return AssistantAgent(
        name="reflection_agent",
        model_client=model_client,
        system_message=system_message,
    )