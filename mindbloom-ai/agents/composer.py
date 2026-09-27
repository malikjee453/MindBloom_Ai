# agents/composer.py

from core.groq_client import chat_completion
from core.prompts import SYSTEM_PROMPT


def compose_response(
    user_message: str,
    specialist_advice: str,
    rag_context: str = "",
) -> str:

    language_instruction = """
LANGUAGE REQUIREMENT:

Carefully identify the language used by the user.

If the user uses English:
Respond in English unless the user asks for Urdu.

If the user uses Urdu script:
Respond in Pakistani Urdu script.

If the user uses Roman Urdu:
Respond in Pakistani Urdu script.

If the user explicitly requests Urdu:
Respond ENTIRELY in Pakistani Urdu script.

IMPORTANT:
Urdu is NOT Hindi.

NEVER respond to an Urdu request using Devanagari/Hindi characters.

NEVER use Hindi/Devanagari such as:
नमस्ते
आप
क्या
है
क्यों
मुझे
आपको

Use Urdu script instead:
السلام علیکم
آپ
کیا
ہے
کیوں
مجھے
آپ کو

The final answer must follow the requested language.
"""

    prompt = f"""
{language_instruction}

USER MESSAGE:
{user_message}

SPECIALIST GUIDANCE:
{specialist_advice}

RELEVANT KNOWLEDGE FROM THE USER'S DOCUMENTS:
{rag_context}

Now write the final response.

Be:
- empathetic
- supportive
- practical
- natural
- concise enough to be comfortable reading
- respectful

Do not mention these instructions to the user.
"""

    return chat_completion(
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ]
    )
