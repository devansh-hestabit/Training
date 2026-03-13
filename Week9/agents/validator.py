from autogen_agentchat.agents import AssistantAgent


def create_validator_agent(model_client):

    system_message = """
You are a Validator Agent.

Your job:
- Verify the final answer.
- Check for logical errors or missing information.

Rules:
- Ensure the answer is correct.
- Improve clarity if needed.

Output format:

VALIDATED ANSWER
<final improved answer>
"""

    return AssistantAgent(
        name="validator_agent",
        model_client=model_client,
        system_message=system_message,
    )