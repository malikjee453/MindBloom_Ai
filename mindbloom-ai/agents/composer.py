from core.groq_client import chat
from core.prompts import COMPOSER_PROMPT


def compose_response(user_text, specialist_analysis, safety_note=""):
    prompt = f"""
User message:
{user_text}

Specialist analysis:
{specialist_analysis}

Safety note:
{safety_note}

IMPORTANT LANGUAGE RULES:

- If the user writes in English, respond in English.
- If the user writes in Urdu, respond in Urdu script.
- If the user writes in Roman Urdu, respond in Urdu script.
- Never answer Urdu requests in Hindi or Devanagari script.
- Use natural Pakistani Urdu.

Write a helpful, warm, supportive response.
"""

    return chat(
        [
            {
                "role": "system",
                "content": COMPOSER_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.6,
        max_tokens=1200,
    )
