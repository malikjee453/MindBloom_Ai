import os
from functools import lru_cache
from groq import Groq
from .config import GROQ_MODEL

def _api_key():
    key = os.getenv("GROQ_API_KEY", "").strip()
    if key: return key
    try:
        import streamlit as st
        return str(st.secrets.get("GROQ_API_KEY", "")).strip()
    except Exception: return ""

@lru_cache(maxsize=1)
def get_client():
    key = _api_key()
    if not key: raise RuntimeError("GROQ_API_KEY is missing. Add it to Streamlit secrets.")
    return Groq(api_key=key)

def chat(messages, temperature=0.4, max_tokens=1200, model=None):
    r = get_client().chat.completions.create(model=model or GROQ_MODEL, messages=messages, temperature=temperature, max_tokens=max_tokens)
    return r.choices[0].message.content or ""
