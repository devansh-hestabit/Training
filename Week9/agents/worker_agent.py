from autogen_agentchat.agents import AssistantAgent


def create_worker_agent(model_client):

    system_message = """
You are a Worker Agent.

Your job:
- Execute a specific task assigned by the planner.
- Provide detailed information for that task.

Rules:
- Focus only on the assigned task.
- Do not generate final answers.
- Return useful analysis or explanation.

Output format:

WORK RESULT
- finding
- finding
"""

    return AssistantAgent(
        name="worker_agent",
        model_client=model_client,
        system_message=system_message,
    )