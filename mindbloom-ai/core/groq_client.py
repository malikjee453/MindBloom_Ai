import os
from groq import Groq

from core.config import GROQ_MODEL


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def chat(messages, temperature=0.7, **kwargs):
    """
    Send a chat request to Groq.

    **kwargs is accepted so existing MindBloom AI agents
    can pass options such as max_tokens without causing
    a Python argument error.
    """

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=messages,
        temperature=temperature,
        **kwargs,
    )

    return response.choices[0].message.content
