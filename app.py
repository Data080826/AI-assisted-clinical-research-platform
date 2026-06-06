# -----------------------------------
# IMPORTS
# -----------------------------------

import streamlit as st

from services.ncbi import (
    search_pubmed,
    fetch_pubmed_details
)

from services.literature import (
    generate_literature_summary
)

from services.gaps import (
    find_research_gaps
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
# SESSION STATE
# -----------------------------------

if "papers" not in st.session_state:
    st.session_state.papers = []

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "gaps" not in st.session_state:
    st.session_state.gaps = ""
    
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

    st.session_state.summary = ""
    st.session_state.gaps = ""

    if research_topic:

        with st.spinner("Searching PubMed..."):

            pmids = search_pubmed(
                research_topic,
                max_results=10
            )

            st.session_state.papers = (
                fetch_pubmed_details(pmids)
            )

    else:

        st.warning(
            "Please enter a research topic."
        )

# -----------------------------------
# DISPLAY PAPERS
# -----------------------------------

if st.session_state.papers:

    papers = st.session_state.papers

    st.success(
        f"Found {len(papers)} papers"
    )

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

if st.session_state.papers:

    if st.button("🧠 Summarize Literature"):

        with st.spinner(
            "Analyzing literature..."
        ):

            st.session_state.summary = (
                generate_literature_summary(
                    st.session_state.papers
                )
            )
# -----------------------------------
# DISPLAY SUMMARY
# -----------------------------------

if st.session_state.summary:

    st.subheader(
        "AI Literature Summary"
    )

    st.markdown(
        st.session_state.summary
    )
    
# -----------------------------------
# KNOWLEDGE GAP FINDER
# -----------------------------------

if st.session_state.summary:

    if st.button("🔍 Find Research Gaps"):

        with st.spinner(
            "Identifying knowledge gaps..."
        ):

            st.session_state.gaps = (
                find_research_gaps(
                    st.session_state.summary
                )
            )


# -----------------------------------
# DISPLAY KNOWLEDGE GAPS
# -----------------------------------

if st.session_state.gaps:

    st.subheader(
        "🔍 Research Opportunities"
    )

    st.markdown(
        st.session_state.gaps
    )


