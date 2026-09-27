import streamlit as st
import base64
from pathlib import Path
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


load_urdu_font()
def contains_urdu(text):
    urdu_chars = (
        "اآبپتٹثجچحخدڈذرڑزژسشصضطظعغفقکگلمنںوہھءیے"
    )

    return any(char in text for char in urdu_chars)
from agents.orchestrator import respond
from core.session import init_session
from core.ui import render_header
init_session(); render_header("MindBloom AI","Supportive conversations","Engr. Mubashir Malik")
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])
prompt=st.chat_input("What's on your mind?")
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):st.markdown(prompt)
    with st.chat_message("assistant"):

         if contains_urdu(response):
        st.markdown(
            f'<div class="urdu-response">{response}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(response)
        try:
            with st.spinner("Thinking..."): answer,sources,route=respond(prompt)
        except Exception as e:
            answer=f"⚠️ I couldn't complete that request.\n\n`{type(e).__name__}: {e}`"; sources=[]
        st.markdown(answer)
        if sources:
            with st.expander("Knowledge sources"):
                for s in sources:st.caption(f"{s['filename']} — chunk {s['chunk_id']} (similarity {s['score']})")
    st.session_state.messages.append({"role":"assistant","content":answer})
