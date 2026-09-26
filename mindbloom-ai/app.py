import streamlit as st
from core.config import APP_NAME, APP_TAGLINE, BUILDER
from core.session import init_session
from core.ui import render_header, render_disclaimer

st.set_page_config(page_title=APP_NAME, page_icon="🌱", layout="wide")
init_session()
render_header(APP_NAME, APP_TAGLINE, BUILDER)
render_disclaimer()
st.title("Welcome to MindBloom AI 🌱")
st.write("A supportive AI companion for reflection, emotional skills, habits, fears, and evidence-informed self-help.")
c1, c2, c3 = st.columns(3)
with c1:
    st.subheader("💬 Talk")
    st.write("Use Chat for supportive conversations.")
with c2:
    st.subheader("🧠 Explore")
    st.write("Work through discomforts, habits, and fears.")
with c3:
    st.subheader("📚 Learn")
    st.write("Upload trusted books and documents for RAG.")
st.info("Start with Chat in the sidebar. Add GROQ_API_KEY to Streamlit secrets before using AI features.")
