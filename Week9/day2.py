import asyncio

from autogen_agentchat.messages import TextMessage

from config.llm_client import get_model_client

from orchestrator.planner import create_planner
from agents.worker_agent import create_worker_agent
from agents.reflection_agent import create_reflection_agent
from agents.validator import create_validator_agent


async def main():

    model_client = get_model_client()

    planner = create_planner(model_client)
    worker = create_worker_agent(model_client)
    reflection = create_reflection_agent(model_client)
    validator = create_validator_agent(model_client)

    query = input("Enter your question: ")

    plan_result = await planner.run(
        task=TextMessage(content=query, source="user")
    )

    plan = plan_result.messages[-1].content
    print("\n--- PLAN ---\n")
    print(plan)

    worker_result = await worker.run(
        task=TextMessage(content=plan, source="planner")
    )

    worker_output = worker_result.messages[-1].content
    print("\n--- WORKER OUTPUT ---\n")
    print(worker_output)

    reflection_result = await reflection.run(
        task=TextMessage(content=worker_output, source="worker")
    )

    reflection_output = reflection_result.messages[-1].content
    print("\n--- REFLECTION ---\n")
    print(reflection_output)

    validator_result = await validator.run(
        task=TextMessage(content=reflection_output, source="reflection")
    )

    final_answer = validator_result.messages[-1].content
    print("\n--- FINAL ANSWER ---\n")
    print(final_answer)

if __name__ == "__main__":
    asyncio.run(main())