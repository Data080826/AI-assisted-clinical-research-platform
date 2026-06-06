import streamlit as st

st.set_page_config(
    page_title="Clinical Research Copilot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Clinical Research Copilot")

research_topic = st.text_input(
    "Enter a research topic",
    placeholder="Semaglutide chronic kidney disease"
)

if st.button("Search Literature"):

    st.write(
        f"Searching literature for: {research_topic}"
    )
