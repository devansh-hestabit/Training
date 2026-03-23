# /nexus_ai/agents/validator.py

from autogen_agentchat.agents import AssistantAgent


def create_validator_agent(model_client):

    system_message = """
You are a Validator Agent.

Your job:
- Verify correctness and completeness
- Ensure the answer fully solves the user query

Rules:
- If correct → confirm briefly
- If incorrect → point out issues
- Do NOT rewrite fully
"""

    return AssistantAgent(
        name="validator_agent",
        model_client=model_client,
        system_message=system_message,
    )