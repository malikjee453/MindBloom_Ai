import streamlit as st

st.set_page_config(
    page_title="MindBloom AI",
    page_icon="🌱",
    layout="wide",
)

st.title("🌱 MindBloom AI")

st.success("App loaded successfully.")

st.write("If this page is bright and readable, Streamlit itself is working correctly.")

st.write("Now checking whether the app remains in a running state...")

st.stop()
