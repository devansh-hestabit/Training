from autogen_agentchat.agents import AssistantAgent


def create_optimizer_agent(model_client):

    system_message = """
You are an Optimizer Agent.

Your job:
- Improve the given answer using critique
- Make it clearer, more complete, and higher quality

Rules:
- Fix all issues identified in critique
- Keep response structured
- Produce improved version only
"""

    return AssistantAgent(
        name="optimizer_agent",
        model_client=model_client,
        system_message=system_message,
    )