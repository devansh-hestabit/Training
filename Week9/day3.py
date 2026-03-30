import asyncio
import json
from autogen_agentchat.messages import TextMessage
from config.llm_client import get_model_client
from autogen_agentchat.agents import AssistantAgent
from tools.file_agent import create_file_agent
from tools.code_executor import create_code_executor
from tools.db_agent import create_db_agent

def clean_code(code: str):
    code = code.strip()

    #remove ```
    if code.startswith("```"):
        code = code.split("```")[1]
        if code.startswith("python"):
            code = code[len("python"):]

    code = code.replace("```", "").strip()
    return code

def create_tool_orchestrator(model_client):

    system_message = """
You are a Tool Planner Agent.

Your job is ONLY to decide which tools should be used.

Available tools:

file_agent
- reads csv or txt files

code_executor
- executes python code
- performs analysis

db_agent
- runs SQL queries
- REQUIRED FORMAT:
  {"tool":"db_agent","db":"database.db","query":"SQL query"}

Rules:
1. DO NOT generate Python code.
2. DO NOT generate explanations.
3. ONLY return a JSON tool plan.
4. Always follow the format below.
5. Always include exact file names in tasks when files are created or modified.

Output format:

{
 "steps":[
   {"tool":"file_agent","input":"filename.csv"},
   {"tool":"code_executor","task":"describe analysis task"}
 ]
}
"""
    return AssistantAgent(
        name="tool_orchestrator",
        model_client=model_client,
        system_message=system_message,
    )

async def generate_python_code(model_client, task, file_data):

    generator = AssistantAgent(
        name="code_generator",
        model_client=model_client,
        system_message="""
You generate Python code to analyze datasets.

Rules:
1. The dataset is already loaded by the file agent.
2. The dataset is available as variable `file_data`.
3. Access rows using: file_data["rows"]
4. Convert to pandas DataFrame:

df = pd.DataFrame(file_data["rows"])

5. NEVER call pd.read_csv().
6. NEVER recreate the dataset manually.
7. Only operate on the provided dataset.
8. Always print the results.
9. If task involves creating or modifying a dataset, ALWAYS save it to a CSV file with appropriate name.

Output ONLY python code.
"""
    )

    prompt = f"""
Task: {task}

Dataset preview:
{file_data}

Write python code to complete the task.
"""

    result = await generator.run(
        task=TextMessage(content=prompt, source="tool")
    )
    return result.messages[-1].content

async def main():

    model_client = get_model_client()
    orchestrator = create_tool_orchestrator(model_client)
    file_agent = create_file_agent()
    code_executor = create_code_executor()
    db_agent = create_db_agent()
    query = input("Enter request: ")

    plan_result = await orchestrator.run(
        task=TextMessage(content=query, source="user")
    )

    plan_text = plan_result.messages[-1].content
    print("\n TOOL PLAN \n")
    print(plan_text)

    # Clean LLM response
    plan_text = plan_text.strip()

    # Remove markdown code fences if present
    if plan_text.startswith("```"):
        plan_text = plan_text.split("```")[1]
        if plan_text.startswith("json"):
            plan_text = plan_text[4:]
        plan_text = plan_text.strip()
    plan = json.loads(plan_text)

    file_data = None
    final_output = None

    for step in plan["steps"]:

        tool = step["tool"]
        if tool == "file_agent":

            file_path = step["input"]
            print(f"\nRunning FILE_AGENT on {file_path}\n")

            file_data = file_agent.read_file(file_path)
            if isinstance(file_data, str) and file_data.startswith("ERROR"):
                print("\n FILE ERROR \n")
                print(file_data)
        
                final_output = file_data
                break

            print("File loaded")
            if isinstance(file_data, dict):

                columns = ", ".join(file_data["columns"])
                rows = file_data["rows"][:10]

                formatted_rows = "\n".join(
        [", ".join(str(v) for v in row.values()) for row in rows]
    )
                final_output = f"""
Columns: {columns}
Total Rows: {file_data['row_count']}

First 10 Rows:
{formatted_rows}
"""
        elif tool == "code_executor":
            task = step["task"]
            print("\nGenerating Python Code...\n")
            python_code = await generate_python_code(
                model_client,
                task,
                file_data
            )
            python_code = clean_code(python_code)
            print(" GENERATED CODE \n")
            print(python_code)

            final_output = code_executor.run_code(
                python_code,
                context={"file_data": file_data}
            )
            print("\n CODE OUTPUT \n")
            print(final_output)

        elif tool == "db_agent":
            db_path = step["db"]
            query = step["query"]
            db_agent.connect(db_path)
            result = db_agent.execute_query(query)
            print("\n DB OUTPUT \n")
            print(result)
            final_output = result

    print("\n FINAL RESULT \n")
    print(final_output)

if __name__ == "__main__":
    asyncio.run(main())