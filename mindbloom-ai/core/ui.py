import streamlit as st


# ---------------------------------------------------------
# MindBloom AI — Global UI Components
# ---------------------------------------------------------

def render_header(name, tagline, builder):
    """
    Render the consistent MindBloom AI brand header.
    """

    st.markdown(
        f"""
        <div class="mb-brand-header">

            <div class="mb-brand-row">

                <div class="mb-brand-logo">
                    🌱
                </div>

                <div class="mb-brand-name">
                    MindBloom
                    <span class="mb-brand-ai">AI</span>
                </div>

            </div>

            <div class="mb-brand-tagline">
                {tagline}
            </div>

            <div class="mb-brand-builder">
                Built by: {builder}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # Global styling for pages that use render_header()
    st.markdown(
        """
        <style>

        /* ================================================
           MINDBLOOM GLOBAL BRAND
           ================================================ */

        .mb-brand-header {
            margin-bottom: 1.8rem;
        }

        .mb-brand-row {
            display: flex;
            align-items: center;
            gap: 13px;
        }

        .mb-brand-logo {
            font-size: 2.65rem;
            line-height: 1;
        }

        .mb-brand-name {
            font-family:
                Inter,
                -apple-system,
                BlinkMacSystemFont,
                "Segoe UI",
                sans-serif;

            font-size: 2.55rem;
            font-weight: 800;
            letter-spacing: -1.8px;
            line-height: 1;
            color: #17231D;
        }

        .mb-brand-ai {
            font-size: 0.95rem;
            font-weight: 600;
            letter-spacing: 1.2px;
            color: #3F8060;
            margin-left: 5px;
            vertical-align: super;
        }

        .mb-brand-tagline {
            margin-top: 12px;
            color: #66756D;
            font-size: 0.98rem;
            line-height: 1.5;
        }

        .mb-brand-builder {
            margin-top: 5px;
            color: #8A9790;
            font-size: 0.78rem;
        }


        /* ================================================
           GENERAL APP COLORS
           ================================================ */

        .stApp {
            background:
                radial-gradient(
                    circle at 90% 0%,
                    rgba(91, 154, 117, 0.07),
                    transparent 28%
                ),
                #F7F9F7;
        }

        .main .block-container {
            max-width: 1120px;
            padding-top: 2.2rem;
            padding-bottom: 4rem;
        }


        /* ================================================
           SIDEBAR
           ================================================ */

        section[data-testid="stSidebar"] {
            background: #F0F5F1;
            border-right: 1px solid #DFE8E1;
        }

        section[data-testid="stSidebar"] .block-container {
            padding-top: 1.8rem;
        }


        /* ================================================
           BUTTONS
           ================================================ */

        div.stButton > button {
            border-radius: 11px;
            border: 1px solid #C9DDD0;
            font-weight: 650;
            transition: all 0.18s ease;
        }

        div.stButton > button:hover {
            border-color: #3F8060;
            color: #2F6F57;
        }


        /* ================================================
           EXPANDERS
           ================================================ */

        div[data-testid="stExpander"] {
            border: 1px solid #DCE6DF;
            border-radius: 14px;
            background: rgba(255, 255, 255, 0.72);
        }


        /* ================================================
           INPUTS
           ================================================ */

        div[data-baseweb="input"] {
            border-radius: 11px;
        }

        textarea {
            border-radius: 11px !important;
        }


        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# Wellbeing Disclaimer
# ---------------------------------------------------------

def render_disclaimer():

    with st.expander("🌿  Important wellbeing note"):

        st.markdown(
            """
            <div style="
                color: #5D6D64;
                line-height: 1.7;
                font-size: 0.92rem;
            ">
                MindBloom AI provides general emotional-support
                and educational information. It is not a replacement
                for a qualified professional or emergency service.
            </div>
            """,
            unsafe_allow_html=True,
        )
