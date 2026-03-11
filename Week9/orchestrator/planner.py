from autogen_agentchat.agents import AssistantAgent


def create_planner(model_client):

    system_message = """
You are the Orchestrator Planner.

Your job:
- Break the user's request into smaller tasks.
- Assign tasks to worker agents.

Rules:
- Identify 2-4 steps required to solve the problem.

Output format:

TASK PLAN
1. step
2. step
3. step
"""

    return AssistantAgent(
        name="planner_agent",
        model_client=model_client,
        system_message=system_message,
    )