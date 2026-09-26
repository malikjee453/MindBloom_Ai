import streamlit as st
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
        try:
            with st.spinner("Thinking..."): answer,sources,route=respond(prompt)
        except Exception as e:
            answer=f"⚠️ I couldn't complete that request.\n\n`{type(e).__name__}: {e}`"; sources=[]
        st.markdown(answer)
        if sources:
            with st.expander("Knowledge sources"):
                for s in sources:st.caption(f"{s['filename']} — chunk {s['chunk_id']} (similarity {s['score']})")
    st.session_state.messages.append({"role":"assistant","content":answer})
