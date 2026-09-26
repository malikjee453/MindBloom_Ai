from core.groq_client import chat
from core.prompts import COMPOSER_PROMPT
def compose_response(user_text,specialist_analysis,safety_note=""):
    return chat([{"role":"system","content":COMPOSER_PROMPT},{"role":"user","content":f"User:\n{user_text}\n\nAnalysis:\n{specialist_analysis}\n\nSafety note:\n{safety_note}"}],temperature=.55,max_tokens=1200)
