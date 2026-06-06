# -----------------------------------
# IMPORTS
# -----------------------------------

import streamlit as st

from services.ncbi import (
    search_pubmed,
    fetch_pubmed_details
)

from services.openai_service import (
    ask_ai
)

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Clinical Research Copilot",
    page_icon="📚",
    layout="wide"
)

# -----------------------------------
# PAGE TITLE
# -----------------------------------

st.title("📚 Clinical Research Copilot")

# -----------------------------------
# RESEARCH TOPIC INPUT
# -----------------------------------

research_topic = st.text_input(
    "Enter a research topic",
    placeholder="Semaglutide chronic kidney disease"
)

# -----------------------------------
# PUBMED SEARCH
# -----------------------------------

if st.button("Search Literature"):

    if research_topic:

        with st.spinner(
            "Searching PubMed..."
        ):

            pmids = search_pubmed(
                research_topic,
                max_results=10
            )

            papers = fetch_pubmed_details(
                pmids
            )

        st.success(
            f"Found {len(papers)} papers"
        )

        # -----------------------------------
        # DISPLAY PAPERS
        # -----------------------------------

        for paper in papers:

            st.markdown(
                f"### {paper['Title']}"
            )

            st.write(
                f"Journal: {paper['Journal']}"
            )

            st.write(
                f"Date: {paper['Date']}"
            )

            st.write(
                f"PMID: {paper['PMID']}"
            )

            st.divider()

        # -----------------------------------
        # AI LITERATURE SUMMARY
        # -----------------------------------

        literature_text = ""

        for paper in papers:

            literature_text += (
                f"Title: {paper['Title']}\n"
            )

        if st.button(
            "🧠 Summarize Literature"
        ):

            with st.spinner(
                "Analyzing literature..."
            ):

                prompt = f"""
                Review these scientific papers.

                Generate:

                1. Literature Overview
                2. Major Findings
                3. Current Limitations
                4. Knowledge Gaps
                5. Future Research Directions

                Papers:

                {literature_text}
                """

                summary = ask_ai(
                    prompt
                )

            st.subheader(
                "AI Literature Summary"
            )

            st.markdown(
                summary
            )

    else:

        st.warning(
            "Please enter a research topic."
        )
