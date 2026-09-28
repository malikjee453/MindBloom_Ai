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

RESPONSE STYLE:

Write a concise but complete answer.

- Aim for 80–130 words.
- Do not exceed 150 words for a normal question.
- Use 3–5 short paragraphs OR a few clear bullet points.
- First acknowledge what the user is experiencing.
- Then give a simple, useful explanation.
- Give 1–3 practical suggestions when appropriate.
- End with one short question only when it naturally helps.
- Do not write an essay.
- Do not give unnecessary background information.
- Do not repeat the user's question.
- Do not make the response so short that it becomes vague or confusing.
- Every sentence should add useful meaning.
- Prefer clear, simple language over complicated terminology.

The response should feel like a thoughtful conversation with a
supportive friend, not a textbook or medical article.

LANGUAGE:
- English input → English response.
- Urdu script input → natural Pakistani Urdu script.
- Roman Urdu input → natural Pakistani Urdu script.
- If Urdu is explicitly requested → completely Urdu script.
- NEVER use Hindi/Devanagari.

Write ONLY the final response.
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
