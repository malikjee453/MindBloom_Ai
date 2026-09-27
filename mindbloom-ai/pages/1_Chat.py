import streamlit as st
import base64
from pathlib import Path

from agents.orchestrator import respond
from core.session import init_session
from core.ui import render_header


# ---------------------------------------------------------
# Jameel Noori Nastaleeq Urdu Font
# ---------------------------------------------------------

FONT_PATH = (
    Path(__file__).resolve().parent.parent
    / "assets"
    / "fonts"
    / "JameelNooriNastaleeq.ttf"
)


def load_urdu_font():
    if not FONT_PATH.exists():
        return

    font_data = base64.b64encode(
        FONT_PATH.read_bytes()
    ).decode("utf-8")

    st.markdown(
        f"""
        <style>
        @font-face {{
            font-family: 'Jameel Noori Nastaleeq';
            src: url(data:font/ttf;base64,{font_data})
                 format('truetype');
            font-weight: normal;
            font-style: normal;
        }}

        .urdu-response {{
            font-family: 'Jameel Noori Nastaleeq' !important;
            direction: rtl;
            text-align: right;
            font-size: 22px;
            line-height: 2.1;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# Detect Urdu text
# ---------------------------------------------------------

def contains_urdu(text):
    urdu_chars = (
        "اآبپتٹثجچحخدڈذرڑزژسشصضطظعغفقکگلمنںوہھءیے"
    )

    return any(char in text for char in urdu_chars)


# ---------------------------------------------------------
# Initialize
# ---------------------------------------------------------

load_urdu_font()

init_session()

render_header(
    "MindBloom AI",
    "Supportive conversations",
    "Engr. Mubashir Malik",
)


# ---------------------------------------------------------
# Previous messages
# ---------------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        content = message["content"]

        if (
            message["role"] == "assistant"
            and contains_urdu(content)
        ):
            st.markdown(
                f'<div class="urdu-response">{content}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(content)


# ---------------------------------------------------------
# Chat input
# ---------------------------------------------------------

prompt = st.chat_input("What's on your mind?")


if prompt:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # -----------------------------------------------------
    # Generate assistant response
    # -----------------------------------------------------

    with st.chat_message("assistant"):

        try:

            with st.spinner("Thinking..."):
                answer, sources, route = respond(prompt)

        except Exception as e:

            answer = (
                "⚠️ I couldn't complete that request.\n\n"
                f"`{type(e).__name__}: {e}`"
            )

            sources = []

        # -------------------------------------------------
        # Display response
        # -------------------------------------------------

        if contains_urdu(answer):

            st.markdown(
                f'<div class="urdu-response">{answer}</div>',
                unsafe_allow_html=True,
            )

        else:

            st.markdown(answer)

        # -------------------------------------------------
        # RAG sources
        # -------------------------------------------------

        if sources:

            with st.expander("Knowledge sources"):

                for source in sources:

                    st.caption(
                        f"{source['filename']} — "
                        f"chunk {source['chunk_id']} "
                        f"(similarity {source['score']})"
                    )

    # -----------------------------------------------------
    # Save assistant response
    # -----------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )
