from core.groq_client import chat
from core.prompts import SPECIALIST_PROMPTS
def run_specialist(route,user_text,context=""):
    system=SPECIALIST_PROMPTS.get(route,SPECIALIST_PROMPTS["GENERAL_EMOTIONAL_SUPPORT"])
    return chat([{"role":"system","content":system},{"role":"user","content":f"User message:\n{user_text}\n\nKnowledge context:\n{context}"}],temperature=.45,max_tokens=1000)
SPECIALIST_PROMPTS = {
    "MENTAL_DISCOMFORT": MENTAL_DISCOMFORT_PROMPT,
    "ADDICTION": ADDICTION_PROMPT,
    "FEAR": FEAR_PROMPT,
    "GENERAL": GENERAL_PROMPT,
    "GENERAL_EMOTIONAL_SUPPORT": GENERAL_PROMPT,
}
