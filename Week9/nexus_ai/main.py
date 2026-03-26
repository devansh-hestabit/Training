import asyncio
import json
import re
import os
from datetime import datetime

from autogen_agentchat.messages import TextMessage

from nexus_ai.config import create_config

from nexus_ai.agents.planner import create_planner_agent
from nexus_ai.agents.researcher import create_researcher_agent
from nexus_ai.agents.coder import create_coder_agent
from nexus_ai.agents.analyst import create_analyst_agent
from nexus_ai.agents.critic import create_critic_agent
from nexus_ai.agents.optimizer import create_optimizer_agent
from nexus_ai.agents.validator import create_validator_agent
from nexus_ai.agents.reporter import create_reporter_agent
from tools.code_executor import CodeExecutor
from tools.db_agent import DBAgent

MAX_CONTEXT = 2000


def log(message: str):
    os.makedirs("logs", exist_ok=True)
    with open("logs/nexus.log", "a") as f:
        f.write(f"{datetime.now()} | {message}\n")


def extract_json(text):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return json.loads(match.group())
    raise ValueError("Invalid planner output")


async def run_nexus(query):

    config = create_config()
    model_client = config.get_model()

    planner = create_planner_agent(model_client)
    researcher = create_researcher_agent(model_client)
    coder = create_coder_agent(model_client)
    analyst = create_analyst_agent(model_client)
    critic = create_critic_agent(model_client)
    optimizer = create_optimizer_agent(model_client)
    validator = create_validator_agent(model_client)
    reporter = create_reporter_agent(model_client)

    agent_map = {
        "researcher": researcher,
        "coder": coder,
        "analyst": analyst
    }

    code_executor = CodeExecutor()
    db_agent_tool = DBAgent()

    log(f"USER QUERY: {query}")

    try:
        print("\nPlanning...\n")

        plan_result = await planner.run(
            task=TextMessage(content=query, source="user")
        )

        plan_text = plan_result.messages[-1].content
        log(f"PLAN RAW: {plan_text}")

        plan = extract_json(plan_text)

        steps = plan["steps"]
        use_reflection = plan.get("reflection", False)

        print("EXECUTION PLAN:\n")
        unsafe_detected = False 
        for i, step in enumerate(steps, 1):
            tool = step.get("tool", "none")
            print(f"{i}. [{step['agent'].upper()}] → {step['task']} (tool: {tool})")

        print(f"\n Reflection Enabled: {use_reflection}")
        print("-" * 60)

        context = query
        for i, step in enumerate(steps, 1):

            agent_name = step["agent"]
            task = step["task"]
            tool_name = step.get("tool")

            agent = agent_map.get(agent_name)

            if not agent:
                continue

            print(f"\n⚙️ Step {i}: {agent_name.upper()} running...")
            print(f"📝 Task: {task}\n")
            step_input = f"""
Context:
{context[-1000:]}

Task:
{task}
"""

            result = await agent.run(
                task=TextMessage(content=step_input, source="planner")
            )

            agent_output = result.messages[-1].content

            print(f" AGENT OUTPUT:\n{agent_output}\n")
            if tool_name == "file_agent" and "import" in agent_output:
                print(" Switching to code_executor (detected Python code)")
                tool_name = "code_executor"

            tool_output = None

            if tool_name is None and any(k in agent_output for k in ["import ", "def ", "pd."]):
                tool_name = "code_executor"
            
            if tool_name == "code_executor":
                print("Executing Python Code...\n")
                dangerous_keywords = [
                    "torch", "transformers", "huggingface", "AutoModel",
                ]

                if any(k in agent_output.lower() for k in dangerous_keywords):
                    print("Blocked unsafe ML execution")
                    tool_output = "BLOCKED_UNSAFE_EXECUTION"
                    unsafe_detected = True
                else:
                    tool_output = code_executor.run_code(agent_output)
            
                # self healing
                retry_count = 0
                max_retries = 2
            
                while (not unsafe_detected) and "Traceback" in str(tool_output) and retry_count < max_retries:
                
                    print("Error detected. Attempting to fix...\n")
            
                    fix_prompt = f"""
            The following Python code failed:
            
            CODE:
            {agent_output}
            
            ERROR:
            {tool_output}
            
            Fix the code so it runs correctly.
            
            Rules:
            - Return ONLY corrected Python code
            - Do NOT explain
            """
            
                    fix_result = await coder.run(
                        task=TextMessage(content=fix_prompt, source="debugger")
                    )
            
                    agent_output = fix_result.messages[-1].content
            
                    print("RETRYING WITH FIXED CODE...\n")
            
                    tool_output = code_executor.run_code(agent_output)
            
                    retry_count += 1

            elif tool_name == "db_agent":
                print("Querying Database...\n")
                tool_output = db_agent_tool.query(agent_output)

            if unsafe_detected:
                final_output = "[SKIPPED: Unsafe execution blocked]"
            else:
                final_output = tool_output if tool_output else agent_output

            print(f"FINAL STEP OUTPUT:\n{final_output}\n")

            log(f"{agent_name.upper()} OUTPUT: {final_output}")

            if not unsafe_detected:
                context += f"\n[{agent_name.upper()}]\n{final_output}"

            if len(context) > MAX_CONTEXT:
                context = context[-MAX_CONTEXT:]

            print("-" * 60)

        if unsafe_detected:
            use_reflection = False

        if use_reflection:

            print("\n🧪 Reflection Phase Enabled\n")

            critique = (await critic.run(
                task=TextMessage(content=context[-1000:], source="system")
            )).messages[-1].content

            print("CRITIQUE:\n", critique, "\n")

            validation = (await validator.run(
                task=TextMessage(content=context[-1000:], source="critic")
            )).messages[-1].content

            print(" VALIDATION:\n", validation, "\n")

            if "IMPROVE" in validation.upper():

                optimized = (await optimizer.run(
                    task=TextMessage(
                        content=f"""
Improve the following WITHOUT removing content:

{context[-1000:]}

Critique:
{critique}
""",
                        source="validator"
                    )
                )).messages[-1].content

                print("IMPROVEMENTS:\n", optimized, "\n")


                context += f"\n[IMPROVEMENTS]\n{optimized}"


        print("\nGenerating Final Report...\n")

        report_input = f"""
        You are given execution logs from multiple agents.

        Your job:
        - Extract only useful insights
        - Remove raw logs, code, and noise
        - Present a clean final answer

        CONTENT:
        {context}
        """

        report_result = await reporter.run(
            task=TextMessage(content=report_input, source="system")
        )

        final_output = report_result.messages[-1].content

        print("FINAL OUTPUT READY\n")

        log(f"FINAL OUTPUT: {final_output}")

        return final_output

    except Exception as e:
        log(f"ERROR: {str(e)}")
        return f"Error: {str(e)}"

async def main():

    print("\n NEXUS AI READY (type 'exit' to quit)\n")

    while True:

        query = input("User: ")

        if query.lower() in ["exit", "quit"]:
            break

        result = await run_nexus(query)

        print("\nNEXUS AI:\n", result, "\n")

if __name__ == "__main__":
    asyncio.run(main())