from autogen_agentchat.agents import AssistantAgent


def create_analyst_agent(model_client):

    system_message = """
You are an Analyst Agent.

Your job:
- Analyze data or situations
- Extract insights
- Provide business or strategic recommendations

Rules:
- Focus on insights, not raw data
- Be concise but meaningful
- Give 3-5 key insights only
- Keep it short
"""

    return AssistantAgent(
        name="analyst_agent",
        model_client=model_client,
        system_message=system_message,
    )