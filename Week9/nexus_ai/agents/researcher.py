# /nexus_ai/agents/researcher.py

from autogen_agentchat.agents import AssistantAgent


def create_researcher_agent(model_client):

    system_message = """
You are a Research Agent.

Your job:
- Gather relevant knowledge
- Explain concepts clearly
- Provide structured insights

Rules:
- Be concise (max 5 bullet points)
- No long explanations
- Do NOT write code
- Focus only on research and explanation
"""

    return AssistantAgent(
        name="researcher_agent",
        model_client=model_client,
        system_message=system_message,
    )