# core/groq_client.py

import os
from groq import Groq

from core.config import GROQ_MODEL


_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def chat_completion(messages):
    response = _client.chat.completions.create(
        model=GROQ_MODEL,
        messages=messages,
        temperature=0.7,
    )

    return response.choices[0].message.content
