import os

from dotenv import load_dotenv
from openai import OpenAI

from config import OPENAI_MODEL

load_dotenv()


class LLMResponseNode:

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def generate_response(
        self,
        user_request,
        route_result,
        worker_result
    ):

        prompt = f"""
You are a helpful business assistant.

User request:
{user_request}

Router result:
{route_result}

Worker result:
{worker_result}

Generate a short friendly response in Hebrew.
"""

        response = self.client.responses.create(
            model=OPENAI_MODEL,
            input=prompt
        )

        return response.output_text