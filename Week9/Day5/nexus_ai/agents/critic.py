# /nexus_ai/agents/critic.py

from autogen_agentchat.agents import AssistantAgent


def create_critic_agent(model_client):

    system_message = """
You are a Critic Agent.

Your job:
- Identify weaknesses in the given output
- Point out missing details, errors, or inconsistencies

Rules:
- Be critical but constructive
- Do NOT rewrite the answer
- Only provide critique
"""

    return AssistantAgent(
        name="critic_agent",
        model_client=model_client,
        system_message=system_message,
    )