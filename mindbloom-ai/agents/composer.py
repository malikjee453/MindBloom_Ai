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

IMPORTANT RESPONSE STYLE:

- Keep the answer SHORT and conversational.
- Usually answer in 3–6 short paragraphs or bullet points.
- Aim for approximately 80–150 words.
- Do NOT write an essay or lecture.
- Give only the most useful points.
- Avoid repeating the user's question.
- Avoid unnecessary background information.
- Use simple, natural language.
- Be warm, empathetic, and human.
- Give one or two practical suggestions rather than a long list.
- If a question can be answered in 2–4 sentences, do that.
- Ask a short follow-up question when it would help continue the conversation.
- Do not overwhelm the user with too much information.
- If the user asks for detailed information, you may provide more detail.

IMPORTANT LANGUAGE RULES:

- If the user writes in English, respond in English.
- If the user writes in Urdu, respond in Urdu script.
- If the user writes in Roman Urdu, respond in Urdu script.
- If the user asks for Urdu, respond completely in Urdu script.
- Never answer an Urdu request in Hindi or Devanagari.
- Never use Hindi/Devanagari characters when Urdu is requested.
- Use natural Pakistani Urdu.

Write the final response now.
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
    )
