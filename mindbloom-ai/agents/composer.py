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

STRICT RESPONSE LENGTH:

- Maximum 100 words.
- Prefer 40–80 words.
- Usually use only 2–4 short paragraphs.
- Do NOT write an essay.
- Do NOT give long explanations.
- Do NOT repeat the user's question.
- Give only the most useful advice.
- Give at most 2 practical suggestions.
- Ask at most ONE short follow-up question.
- If the answer can be given in 2–3 sentences, stop there.
- Do not add extra information just to make the response longer.

IMPORTANT:
The response must feel like a short, natural conversation with a supportive friend.

LANGUAGE:

- English input → English response.
- Urdu script input → Pakistani Urdu script.
- Roman Urdu input → Pakistani Urdu script.
- If Urdu is requested → completely Urdu script.
- NEVER use Hindi/Devanagari.

Now write ONLY the final response.
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
        max_tokens=180,
    )
