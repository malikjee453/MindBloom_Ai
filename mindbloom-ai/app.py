import streamlit as st

st.set_page_config(
    page_title="MindBloom AI",
    page_icon="🌱",
    layout="wide",
)

st.markdown(
    """
    <style>

    /* Completely remove opacity/filter effects */
    * {
        opacity: 1 !important;
        filter: none !important;
    }

    html,
    body {
        opacity: 1 !important;
        filter: none !important;
        background: white !important;
    }

    [data-testid="stApp"],
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stAppViewBlockContainer"] {
        opacity: 1 !important;
        filter: none !important;
        background: white !important;
    }

    .main,
    .block-container {
        opacity: 1 !important;
        filter: none !important;
    }

    p,
    h1,
    h2,
    h3,
    div,
    span,
    label {
        opacity: 1 !important;
        filter: none !important;
        color: #111111 !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

st.title("MindBloom AI")

st.markdown(
    """
    <h2 style="color:#111111 !important;">
        This is a visibility test
    </h2>

    <p style="color:#111111 !important; font-size:20px;">
        If you can read this clearly, the problem is in the
        MindBloom homepage styling.
    </p>

    <div style="
        background:#eeeeee;
        padding:25px;
        border-radius:12px;
        color:#111111 !important;
        font-size:22px;
    ">
        BLACK TEST TEXT — THIS SHOULD BE CLEARLY VISIBLE.
    </div>
    """,
    unsafe_allow_html=True,
)

st.success("Visibility test completed.")
