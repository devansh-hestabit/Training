import asyncio

from autogen_agentchat.messages import TextMessage
from autogen_agentchat.agents import AssistantAgent

from config.llm_client import get_model_client

from memory.session_memory import create_session_memory
from memory.vector_store import create_vector_store
from memory.long_term import create_long_term_memory


def create_memory_agent(model_client):

    system_message = """
You are a memory-aware AI assistant.

You will receive:
1. Relevant past memories
2. Recent conversation context
3. Current user query

Use this information to generate better responses.

Rules:
- Use memory when relevant
- Be concise and accurate
"""

    return AssistantAgent(
        name="memory_agent",
        model_client=model_client,
        system_message=system_message,
    )


async def main():

    # Initialize components
    model_client = get_model_client()

    agent = create_memory_agent(model_client)

    session_memory = create_session_memory(max_messages=10)
    vector_store = create_vector_store()
    long_term_memory = create_long_term_memory()

    print("\n🧠 Memory Agent Ready (type 'exit' to quit)\n")

    while True:

        query = input("User: ")

        if query.lower() in ["exit", "quit", "close"]:
            break
        
        if query.lower() == "clear memory":
            long_term_memory.clear()
            vector_store.clear()
            session_memory.clear()
        
            print("🧠 All memory cleared!\n")
            continue

        # 1️⃣ Search vector memory
        similar_memories = vector_store.search(query)

        # 2️⃣ Get session context
        session_context = session_memory.get_context()

        # 3️⃣ Get long-term memory
        long_term = long_term_memory.get_all(limit=5)

        long_term_text = "\n".join([m[0] for m in long_term])

        # 4️⃣ Build final prompt
        final_prompt = f"""
RELEVANT MEMORY:
{similar_memories}

LONG TERM MEMORY:
{long_term_text}

SESSION CONTEXT:
{session_context}

USER QUERY:
{query}
"""

        # 5️⃣ Get response from LLM
        result = await agent.run(
            task=TextMessage(content=final_prompt, source="user")
        )

        response = result.messages[-1].content

        print("\nAssistant:", response, "\n")

        # 6️⃣ Store in session memory
        session_memory.add("user", query)
        session_memory.add("assistant", response)

        # 7️⃣ Store in vector memory
        vector_store.add(query)
        vector_store.add(response)

        # 8️⃣ Store summarized user facts
        if "i am" in query.lower() or "i prefer" in query.lower() or "i like" in query.lower():
            fact = await summarize_fact(model_client, query)
            long_term_memory.add(fact, "fact")

        # 9️⃣ Store summarized assistant responses
        if len(response) < 200:
            summary = await summarize_fact(model_client, response)
            long_term_memory.add(summary, "summary")

async def summarize_fact(model_client, text: str):
    summarizer = AssistantAgent(
        name="memory_summarizer",
        model_client=model_client,
        system_message="""
You extract important facts about the user.

Rules:
- Convert input into a short fact
- Focus on user preferences or important info
- Do NOT explain
- Output only the fact

Examples:

Input: I am interested in electronics sales
Output: User prefers electronics sales

Input: I like fashion products
Output: User prefers fashion products
"""
    )

    result = await summarizer.run(
        task=TextMessage(content=text, source="user")
    )

    return result.messages[-1].content.strip()


if __name__ == "__main__":
    asyncio.run(main())