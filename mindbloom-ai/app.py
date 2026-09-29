import streamlit as st

from core.config import APP_NAME, APP_TAGLINE, BUILDER
from core.session import init_session
from core.ui import render_disclaimer

st.set_page_config(
    page_title="MindBloom AI",
    page_icon="🌱",
    layout="wide",
)

init_session()


# =========================================================
# MIND BLOOM UI STYLING
# =========================================================

st.markdown(
    """
    <style>

    /* -----------------------------------------------------
       1. PREVENT STREAMLIT DIMMING / STALE ELEMENT OPACITY
       ----------------------------------------------------- */

    [data-testid="stAppViewBlockContainer"],
    [data-testid="stAppViewBlockContainer"] *,
    .element-container,
    [data-stale="true"],
    [data-stale="true"] * {
        opacity: 1 !important;
        filter: none !important;
        transition: none !important;
    }

    /* Prevent dimming while Streamlit is running */
    [data-testid="stApp"][data-test-script-state="running"] {
        opacity: 1 !important;
    }

    [data-testid="stApp"][data-test-script-state="running"]
    [data-testid="stAppViewContainer"] {
        opacity: 1 !important;
        filter: none !important;
    }


    /* -----------------------------------------------------
       2. MAIN PAGE
       ----------------------------------------------------- */

    [data-testid="stMain"] {
        opacity: 1 !important;
        filter: none !important;
    }

    [data-testid="stMain"] > div {
        opacity: 1 !important;
        filter: none !important;
    }

    .main .block-container {
        max-width: 1100px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }


    /* -----------------------------------------------------
       3. SIDEBAR
       ----------------------------------------------------- */

    section[data-testid="stSidebar"] {
        opacity: 1 !important;
        filter: none !important;
    }

    section[data-testid="stSidebarContent"] {
        opacity: 1 !important;
        filter: none !important;
    }

    section[data-testid="stSidebar"] a,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span {
        color: #40564b !important;
    }


    /* -----------------------------------------------------
       4. GENERAL TEXT
       ----------------------------------------------------- */

    .stMarkdown p,
    .stMarkdown li {
        color: #33483d;
    }

    [data-testid="stCaptionContainer"] {
        color: #5f7067 !important;
    }


    /* -----------------------------------------------------
       5. MINDBLOOM BRAND
       ----------------------------------------------------- */

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
    }


    /* -----------------------------------------------------
       6. TAGLINE / BUILDER
       ----------------------------------------------------- */

    .mb-tagline {
        color: #53675d !important;
        font-size: 1rem;
        margin-top: 10px;
    }

    .mb-builder {
        color: #66776e !important;
        font-size: 0.8rem;
        margin-top: 5px;
        margin-bottom: 28px;
    }


    /* -----------------------------------------------------
       7. WELCOME MESSAGE
       ----------------------------------------------------- */

    .mb-welcome {
        font-family:
            "Trebuchet MS",
            "Segoe UI",
            Arial,
            sans-serif;

        font-size: 2.15rem;
        font-weight: 800;
        letter-spacing: -1px;
        line-height: 1.25;

        background: linear-gradient(
            135deg,
            #173B2D 0%,
            #2F7655 50%,
            #5A9E78 100%
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;

        margin-top: 24px;
        margin-bottom: 12px;
    }


    /* -----------------------------------------------------
       8. FEATURE SECTIONS
       ----------------------------------------------------- */

    .mb-feature-title {
        color: #17231D !important;
        font-size: 1.35rem;
        font-weight: 700;
        margin-bottom: 6px;
    }

    .mb-feature-text {
        color: #4d6258 !important;
        line-height: 1.6;
    }


    /* -----------------------------------------------------
       9. START CONVERSATION BUTTON
       ----------------------------------------------------- */

    div.stButton > button {
        background: linear-gradient(
            135deg,
            #2F7655,
            #438B66
        ) !important;

        color: white !important;

        border: none !important;
        border-radius: 14px !important;

        min-height: 68px !important;
        min-width: 320px !important;

        padding: 12px 28px !important;

        box-shadow:
            0 8px 20px rgba(47, 118, 85, 0.22);

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }

    div.stButton > button p {
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: white !important;
        line-height: 1.2 !important;
        margin: 0 !important;
    }

    div.stButton > button:hover {
        background: linear-gradient(
            135deg,
            #286648,
            #397A59
        ) !important;

        color: white !important;

        transform: translateY(-2px);

        box-shadow:
            0 12px 26px rgba(47, 118, 85, 0.30);
    }


    /* -----------------------------------------------------
       10. DISCLAIMER
       ----------------------------------------------------- */

    div[data-testid="stExpander"] {
        border-radius: 12px;
        border-color: #DDE6DF;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="mb-brand">'
    '<div class="mb-logo">🌱</div>'
    '<div class="mb-name">MindBloom'
    '<span class="mb-ai">AI</span>'
    '</div>'
    '</div>'
    '<div class="mb-tagline">'
    'A supportive AI companion for emotional growth, habits, fears, '
    'and evidence-informed self-help.'
    '</div>'
    '<div class="mb-builder">'
    'Built by: Engr. Mubashir Malik'
    '</div>',
    unsafe_allow_html=True,
)


# =========================================================
# DISCLAIMER
# =========================================================

render_disclaimer()


# =========================================================
# WELCOME
# =========================================================

st.markdown(
    '<div class="mb-welcome">'
    'You are welcome to talk to me,<br>'
    'About anything you can\'t share with anyone.'
    '</div>',
    unsafe_allow_html=True,
)

st.write(
    "Type your question or share what is on your mind. "
    "You can ask me to answer in English or Urdu."
)


# =========================================================
# FEATURES
# =========================================================

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
        'Find your discomforts, habits, addictions, and fears '
        'here and get advice to overcome them.'
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
        'Upload books and documents and ask questions from them '
        'for short-term memory.'
        '</div>',
        unsafe_allow_html=True,
    )


# =========================================================
# START CONVERSATION
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

if st.button(
    "💬  Start a conversation",
    key="start_conversation",
):
    st.switch_page("pages/1_Chat.py")
