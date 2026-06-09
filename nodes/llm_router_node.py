import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from utils.logger_config import logger
from config import OPENAI_MODEL

load_dotenv()


class LLMRouterNode:

    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def route(self, user_request):

        prompt = f"""
You are a strict classification system for an AI agent.

You MUST follow these rules:
- Output ONLY valid JSON
- No explanations
- No extra text
- No markdown
- No code blocks

Allowed routes:
- logo
- signature
- business_card
- official_letter

User request:
{user_request}

Return EXACTLY in this format:
{{
  "route": "<one of the allowed routes>",
  "confidence": <number between 0 and 1>
}}

If you are unsure, still choose the closest route.
"""
        logger.info("Sending request to OpenAI Router")

        response = self.client.responses.create(
            model=OPENAI_MODEL,
            input=prompt
        )

        text = response.output_text.strip()

        try:
            result = json.loads(text)
        except Exception:
            # fallback אם ה־LLM לא החזיר JSON תקין
            return {
                "route": "unknown",
                "confidence": 0.0
            }
        
        logger.info(f"Raw model output: {text}")

        return result