import streamlit as st

from core.config import APP_NAME, APP_TAGLINE, BUILDER
from core.session import init_session
from core.ui import render_disclaimer


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="MindBloom AI",
    page_icon="🌱",
    layout="wide",
)


# ---------------------------------------------------------
# Session
# ---------------------------------------------------------

init_session()


# ---------------------------------------------------------
# Professional but subtle styling
# ---------------------------------------------------------

st.markdown(
    """
<style>

.main .block-container {
    max-width: 1100px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Main brand */

.mb-brand {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 6px;
}

.mb-logo {
    font-size: 2.7rem;
    line-height: 1;
}

.mb-name {
    color: #17231D;
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 3rem;
    font-weight: 800;
    letter-spacing: -1.8px;
    line-height: 1;
}

.mb-ai {
    color: #3F8060;
    font-size: 1rem;
    font-weight: 600;
    letter-spacing: 1px;
    vertical-align: super;
    margin-left: 4px;
}

.mb-tagline {
    color: #66756D;
    font-size: 1rem;
    margin-top: 10px;
}

.mb-builder {
    color: #8A9790;
    font-size: 0.8rem;
    margin-top: 5px;
    margin-bottom: 28px;
}


/* Welcome heading */

.mb-welcome {
    color: #17231D;
    font-size: 2.25rem;
    font-weight: 750;
    letter-spacing: -0.8px;
    margin-top: 18px;
    margin-bottom: 8px;
}

.mb-welcome span {
    color: #3F8060;
}


/* Feature headings */

.mb-feature-title {
    color: #17231D;
    font-size: 1.35rem;
    font-weight: 700;
    margin-bottom: 6px;
}

.mb-feature-text {
    color: #66756D;
    line-height: 1.6;
}


/* Start button */

div.stButton > button {
    background: #3F8060;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 650;
    padding: 0.55rem 1.15rem;
}

div.stButton > button:hover {
    background: #326B4F;
    color: white;
}


/* Disclaimer */

div[data-testid="stExpander"] {
    border-radius: 12px;
    border-color: #DDE6DF;
}

</style>
""",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# MindBloom brand
# ---------------------------------------------------------

st.markdown(
    '<div class="mb-brand">'
    '<div class="mb-logo">🌱</div>'
    '<div class="mb-name">MindBloom'
    '<span class="mb-ai">AI</span>'
    '</div>'
    '</div>'
    '<div class="mb-tagline">'
    'A supportive AI companion for emotional growth, habits, and fears,and evidence-informed self-help.'
    '</div>'
    '<div class="mb-builder">'
    'Built by: Engr. Mubashir Malik'
    '</div>',
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Wellbeing note
# ---------------------------------------------------------

render_disclaimer()


# ---------------------------------------------------------
# Welcome
# ---------------------------------------------------------

st.markdown(
    '<div class="mb-welcome">'
    'You are welcome to chat with me, Any topic you cant share with anyone.'
    '</div>',
    unsafe_allow_html=True,
)


st.write(
    "Type your question or share what is on your mind. "
    "You can ask me to answer in English or Urdu."
)

# ---------------------------------------------------------
# Start conversation
# ---------------------------------------------------------

if st.button("💬  Start a conversation"):

    st.switch_page("pages/1_Chat.py")


# ---------------------------------------------------------
# Features
# ---------------------------------------------------------

c1, c2, c3 = st.columns(3)


with c1:

    st.markdown(
        '<div class="mb-feature-title">💬 Talk</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="mb-feature-text">'
        'Talk to me, I can help.'
        '</div>',
        unsafe_allow_html=True,
    )


with c2:

    st.markdown(
        '<div class="mb-feature-title">🧠 Explore</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="mb-feature-text">'
        'Find your discomforts, habits, and fears here.'
        '</div>',
        unsafe_allow_html=True,
    )


with c3:

    st.markdown(
        '<div class="mb-feature-title">📚 Learn</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="mb-feature-text">'
        'Upload books and documents and ask question from it, only for short term memory.'
        '</div>',
        unsafe_allow_html=True,
    )
