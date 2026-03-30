from autogen_agentchat.agents import AssistantAgent


def create_planner(model_client):

    system_message = """
You are the Orchestrator Planner.

Your job:
- Break the user's request into smaller independent tasks.
- Ensure tasks can be executed in parallel by worker agents.

Rules:
- Create 2 to 4 tasks maximum.
- Each task must be:
  - Independent (no dependency on other tasks)
  - Clear and specific
  - Actionable for a worker agent
- Do NOT solve the problem.
- Do NOT provide explanations or answers.

Output format (strict):

TASK PLAN
1. <task 1>
2. <task 2>
3. <task 3>
"""

    return AssistantAgent(
        name="planner_agent",
        model_client=model_client,
        system_message=system_message,
    )