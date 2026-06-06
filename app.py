import streamlit as st

st.set_page_config(
    page_title="Clinical Research Copilot",
    page_icon="📚",
    layout="wide"
)

st.title("Clinical Research Copilot")

page = st.sidebar.radio(
    "Navigation",
    [
        "Literature Search",
        "Gap Finder",
        "Research Question",
        "Study Design"
    ]
)

st.write("Selected:", page)
