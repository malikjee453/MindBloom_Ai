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
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------
# Session
# ---------------------------------------------------------

init_session()


# ---------------------------------------------------------
# Professional MindBloom UI
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* =====================================================
       GLOBAL
       ===================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 85% 5%,
                rgba(91, 154, 117, 0.10),
                transparent 28%
            ),
            radial-gradient(
                circle at 5% 90%,
                rgba(91, 154, 117, 0.07),
                transparent 25%
            ),
            #F7F9F7;
    }

    .main .block-container {
        max-width: 1120px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }


    /* =====================================================
       BRAND HEADER
       ===================================================== */

    .mindbloom-brand {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 8px;
    }

    .mindbloom-logo {
        font-size: 3.2rem;
        line-height: 1;
    }

    .mindbloom-name {
        font-family: Inter, -apple-system, BlinkMacSystemFont,
                     "Segoe UI", sans-serif;
        font-size: 3.15rem;
        font-weight: 800;
        letter-spacing: -2px;
        color: #17231D;
        line-height: 1;
    }

    .mindbloom-ai {
        font-size: 1.15rem;
        font-weight: 500;
        letter-spacing: 1px;
        color: #3F8060;
        margin-left: 5px;
        vertical-align: super;
    }

    .brand-tagline {
        font-size: 1.05rem;
        color: #66756D;
        margin-top: 12px;
        margin-bottom: 6px;
    }

    .brand-builder {
        font-size: 0.82rem;
        color: #8A9790;
        margin-bottom: 2.2rem;
    }


    /* =====================================================
       HERO
       ===================================================== */

    .hero {
        position: relative;
        overflow: hidden;
        background:
            linear-gradient(
                135deg,
                #EAF4ED 0%,
                #F4F8F5 52%,
                #FFFFFF 100%
            );
        border: 1px solid #DCE9E0;
        border-radius: 24px;
        padding: 42px 44px;
        margin-bottom: 30px;
        box-shadow: 0 10px 35px rgba(23, 35, 29, 0.06);
    }

    .hero::after {
        content: "🌱";
        position: absolute;
        right: 40px;
        bottom: -18px;
        font-size: 8rem;
        opacity: 0.08;
        transform: rotate(-8deg);
    }

    .hero-eyebrow {
        display: inline-block;
        background: #DCEFE3;
        color: #397052;
        padding: 7px 13px;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.7px;
        text-transform: uppercase;
        margin-bottom: 16px;
    }

    .hero-title {
        font-size: 2.55rem;
        font-weight: 800;
        color: #17231D;
        letter-spacing: -1px;
        line-height: 1.15;
        margin-bottom: 12px;
    }

    .hero-title span {
        color: #3F8060;
    }

    .hero-text {
        max-width: 720px;
        color: #5D6D64;
        font-size: 1.05rem;
        line-height: 1.75;
        margin-bottom: 25px;
    }


    /* =====================================================
       FEATURE CARDS
       ===================================================== */

    .section-label {
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 700;
        color: #779084;
        margin-top: 30px;
        margin-bottom: 14px;
    }

    .feature-card {
        background: rgba(255, 255, 255, 0.88);
        border: 1px solid #E0E9E3;
        border-radius: 20px;
        padding: 27px 25px;
        min-height: 190px;
        box-shadow: 0 7px 24px rgba(23, 35, 29, 0.045);
        transition: all 0.2s ease;
    }

    .feature-card:hover {
        border-color: #BFD8C7;
        box-shadow: 0 12px 30px rgba(23, 35, 29, 0.08);
        transform: translateY(-2px);
    }

    .feature-icon {
        font-size: 2rem;
        margin-bottom: 12px;
    }

    .feature-title {
        font-size: 1.2rem;
        font-weight: 750;
        color: #1D2B24;
        margin-bottom: 8px;
    }

    .feature-text {
        color: #697870;
        font-size: 0.92rem;
        line-height: 1.65;
    }


    /* =====================================================
       BOTTOM MESSAGE
       ===================================================== */

    .closing-card {
        margin-top: 30px;
        background: #17231D;
        border-radius: 20px;
        padding: 25px 30px;
        color: white;
        box-shadow: 0 10px 30px rgba(23, 35, 29, 0.12);
    }

    .closing-title {
        font-size: 1.15rem;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .closing-text {
        color: #C8D6CE;
        font-size: 0.9rem;
        line-height: 1.6;
    }


    /* =====================================================
       BUTTON
       ===================================================== */

    div.stButton > button {
        background: #3F8060;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.65rem 1.4rem;
        font-weight: 700;
        font-size: 0.95rem;
        box-shadow: 0 5px 15px rgba(63, 128, 96, 0.22);
    }

    div.stButton > button:hover {
        background: #326B4F;
        color: white;
        border: none;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {
        background: #F0F5F1;
        border-right: 1px solid #DFE8E1;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }


    /* =====================================================
       DISCLAIMER
       ===================================================== */

    div[data-testid="stExpander"] {
        border-radius: 14px;
        border-color: #DDE6DF;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Brand
# ---------------------------------------------------------

st.markdown(
    """
    <div class="mindbloom-brand">
        <div class="mindbloom-logo">🌱</div>

        <div class="mindbloom-name">
            MindBloom
            <span class="mindbloom-ai">AI</span>
        </div>
    </div>

    <div class="brand-tagline">
        A supportive AI companion for emotional growth, habits, and fears.
    </div>

    <div class="brand-builder">
        Built by: Engr. Mubashir Malik
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Wellbeing disclaimer
# ---------------------------------------------------------

render_disclaimer()


# ---------------------------------------------------------
# Hero
# ---------------------------------------------------------

st.markdown(
    """
    <div class="hero">

        <div class="hero-eyebrow">
            Your space to reflect & grow
        </div>

        <div class="hero-title">
            Welcome to <span>MindBloom</span>
        </div>

        <div class="hero-text">
            A calm, supportive space to understand your thoughts,
            work through difficult emotions, build healthier habits,
            and face fears — one step at a time.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Start conversation button
# ---------------------------------------------------------

if st.button("💬  Start a conversation", type="primary"):

    st.switch_page("pages/1_Chat.py")


# ---------------------------------------------------------
# Features
# ---------------------------------------------------------

st.markdown(
    '<div class="section-label">Explore MindBloom</div>',
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3, gap="large")


with c1:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">💬</div>

            <div class="feature-title">
                Talk
            </div>

            <div class="feature-text">
                Have a supportive conversation about what's
                on your mind. Reflect, express, and explore
                your feelings without judgment.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with c2:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">🧠</div>

            <div class="feature-title">
                Explore
            </div>

            <div class="feature-text">
                Work through emotional discomforts, fears,
                habits, and addictive patterns with practical
                reflection and evidence-informed guidance.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


with c3:

    st.markdown(
        """
        <div class="feature-card">

            <div class="feature-icon">📚</div>

            <div class="feature-title">
                Learn
            </div>

            <div class="feature-text">
                Upload trusted books and documents and let
                MindBloom use your knowledge library with
                retrieval-augmented generation.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# Closing message
# ---------------------------------------------------------

st.markdown(
    """
    <div class="closing-card">

        <div class="closing-title">
            🌿 Small steps can create meaningful change.
        </div>

        <div class="closing-text">
            You don't have to figure everything out at once.
            Start with one thought, one question, or one small step.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)
