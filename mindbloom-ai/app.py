import streamlit as st

st.set_page_config(
    page_title="MindBloom AI",
    page_icon="🌱",
)

st.title("🌱 MindBloom AI")
st.success("Visibility test")
st.write("This page should be completely clear and readable.")

st.code(f"Streamlit version: {st.__version__}")

st.stop()
