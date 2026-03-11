from autogen_agentchat.agents import AssistantAgent


def create_research_agent(model_client):

    system_message = """
You are a Research Agent.

Your job is to gather factual information about the user's query.

Rules:
- Provide detailed research notes.
- Include key concepts, mechanisms, and examples.
- Do NOT summarize the information.
- Do NOT give the final answer.

Output format:

RESEARCH NOTES
- point
- point
- point
"""

    return AssistantAgent(
        name="research_agent",
        model_client=model_client,
        system_message=system_message,
    )