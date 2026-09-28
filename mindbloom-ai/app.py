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
    font-family:
        "Trebuchet MS",
        "Segoe UI",
        Arial,
        sans-serif;

    font-size: 3.25rem;
    font-weight: 900;
    letter-spacing: -2.8px;
    line-height: 1;

    background: linear-gradient(
        135deg,
        #173B2D 0%,
        #2F7655 48%,
        #5A9E78 100%
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.mb-ai {
    color: #D28B35;
    font-family:
        "Segoe UI",
        Arial,
        sans-serif;

    font-size: 1rem;
    font-weight: 800;
    letter-spacing: 1.5px;

    vertical-align: super;
    margin-left: 6px;

    -webkit-text-fill-color: #D28B35;
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
    background: linear-gradient(
        135deg,
        #2F7655,
        #438B66
    );

    color: white;
    border: none;
    border-radius: 14px;

    font-size: 1.05rem;
    font-weight: 700;

    padding: 0.85rem 2.2rem;

    min-height: 56px;
    min-width: 260px;

    box-shadow:
        0 8px 20px rgba(47, 118, 85, 0.22);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

div.stButton > button:hover {
    background: linear-gradient(
        135deg,
        #286648,
        #397A59
    );

    color: white;

    transform: translateY(-2px);

    box-shadow:
        0 12px 25px rgba(47, 118, 85, 0.30);
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
        'Find your discomforts, habits, addictions, and fears here and get advise to overcome them.'
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
