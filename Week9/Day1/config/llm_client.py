import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()


def get_model_client():
    return OpenAIChatCompletionClient(
        model="llama-3.3-70b-versatile",
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.2,
        model_info={
            "vision": False, # no images
            "function_calling": True,
            "json_output": True,
            "structured_output": True,
            "family": "llama3",
        },
    )