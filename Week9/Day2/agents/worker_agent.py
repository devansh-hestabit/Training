from autogen_agentchat.agents import AssistantAgent


def create_worker_agent(model_client):

    system_message = """
You are a Worker Agent.

Your job:
- Execute ONE specific task assigned by the planner.
- Provide detailed findings for that task only.

Rules:
- Focus strictly on the given task.
- Do NOT solve the full user problem.
- Do NOT reference other tasks.
- Do NOT generate a final answer.
- Keep output structured and concise.

Output format (strict):

WORK RESULT
- Finding 1
- Finding 2
- Finding 3
"""

    return AssistantAgent(
        name="worker_agent",
        model_client=model_client,
        system_message=system_message,
    )