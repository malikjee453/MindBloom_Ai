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

RESPONSE LENGTH:
- Keep the response SHORT.
- Aim for 40–80 words.
- Maximum approximately 100 words.
- Use 2–4 short paragraphs.
- Give only the most useful information.
- Give at most 2 practical suggestions.
- Ask at most 1 short follow-up question.
- Do not write an essay.
- Do not repeat the user's question.
- Stop when the useful answer is complete.

LANGUAGE:
- English input → English.
- Urdu script input → Pakistani Urdu script.
- Roman Urdu input → Pakistani Urdu script.
- If Urdu is requested → completely Urdu script.
- Never use Hindi/Devanagari.

Write ONLY the final answer to the user.
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
        temperature=0.5,
    )
