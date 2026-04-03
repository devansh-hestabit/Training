import asyncio
from autogen_agentchat.messages import TextMessage
from Week9.Day5.config.llm_client import get_model_client
from Week9.Day1.agents.research_agent import create_research_agent
from Week9.Day1.agents.summarizer_agent import create_summarizer_agent
from Week9.Day1.agents.answer_agent import create_answer_agent

async def main():

    model_client = get_model_client()
    research_agent = create_research_agent(model_client)
    summarizer_agent = create_summarizer_agent(model_client)
    answer_agent = create_answer_agent(model_client)

    query = input("Enter your question: ")

    research_result = await research_agent.run(
        task=TextMessage(content=query, source="user")
    )

    research_text = research_result.messages[-1].content
    print("\n Research Agent \n")
    print(research_text)

    summary_result = await summarizer_agent.run(
        task=TextMessage(content=research_text, source="research_agent")
    )

    summary_text = summary_result.messages[-1].content
    print("\n Summary \n")
    print(summary_text)

    answer_result = await answer_agent.run(
        task=TextMessage(content=summary_text, source="summarizer_agent")
    )

    final_answer = answer_result.messages[-1].content
    print("\nFinal Answer\n")
    print(final_answer)

if __name__ == "__main__":
    asyncio.run(main())