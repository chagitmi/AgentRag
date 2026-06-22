
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
You are a strict classification system for a business office AI assistant.

Your job is to classify the user's request into EXACTLY one route.

You MUST return ONLY valid JSON.

Available routes:

1. logo
Use when the user asks for:
- logo
- company branding
- company image
- brand file

Examples:
"תציג לי לוגו"
"I need the company logo"

-------------------

2. signature
Use when the user wants to:
- send an email
- attach email signature
- create email footer
- send message to customer by email

Examples:
"שלח מייל ללקוח"
"אני צריכה חתימה למייל"
"I need email signature"

-------------------

3. business_card
Use when the user asks for:
- business card
- visiting card
- contact card

Examples:
"תביא לי כרטיס ביקור"

-------------------

4. official_letter
Use when the user wants:
- formal document
- quotation
- proposal
- official company document
- price offer

Examples:
"תיצור מסמך רשמי"
"אני צריכה הצעת מחיר"

-------------------

Important rules:

If the request mentions EMAIL → ALWAYS choose signature.

If the request mentions QUOTE / OFFER / PROPOSAL → choose official_letter.

Return ONLY JSON:

{{
  "route": "<route>",
  "confidence": <number>,
  "asset_query": "<short english query for embedding search>"
}}

User request:

{user_request}
Return also an asset_query that will be used for vector search.
"""      
       logger.info("Sending request to OpenAI Router")

       response = self.client.responses.create(
            model=OPENAI_MODEL,
            input=prompt
        )

       text = response.output_text.strip()

       try:
            result = json.loads(text)
       except Exception as e:
            logger.error(f"JSON parsing error: {e}")

            return {
             "route": "unknown",
             "confidence": 0.0
         }
        
       logger.info(f"Raw model output: {text}")

       return result