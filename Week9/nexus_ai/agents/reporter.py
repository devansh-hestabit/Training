# /nexus_ai/agents/reporter.py

from autogen_agentchat.agents import AssistantAgent


def create_reporter_agent(model_client):

    system_message = """
You are a professional AI report generator.

Your job:
- Extract ONLY final insights
- Remove:
  - logs
  - code
  - debug info
- Structure output:

OUTPUT FORMAT:

Summary:
...

Key Insights:
- ...

Results:
...

Do NOT include raw execution logs.
"""

    return AssistantAgent(
        name="reporter_agent",
        model_client=model_client,
        system_message=system_message,
    )