# -----------------------------------
# IMPORTS
# -----------------------------------

import streamlit as st

from services.ncbi import (
    search_pubmed,
    fetch_pubmed_details
)

from modules.literature import (
    generate_literature_summary
)

from modules.gaps import (
    find_research_gaps
)

from modules.question_builder import (
    generate_research_question
)
from modules.study_design import (
    generate_study_design
)

from modules.dataset_analysis import (
    analyze_dataset
)

from modules.statistical_analysis import (
    descriptive_statistics,
    categorical_summary,
    compare_groups
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

if "research_question" not in st.session_state:
    st.session_state.research_question = ""

if "study_design" not in st.session_state:
    st.session_state.study_design = ""

if "dataset_report" not in st.session_state:
    st.session_state.dataset_report = ""    
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
            f"Date: {paper.get('Date', 'Not available')}"
        )

        st.write(
            f"PMID: {paper['PMID']}"
        )

        with st.expander("📄 View Abstract"):

            st.write(
                paper.get(
                    "Abstract",
                    "Abstract not available"
                )
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

# -----------------------------------
# RESEARCH QUESTION GENERATOR
# -----------------------------------

if st.session_state.gaps:

    if st.button(
        "🎯 Generate Research Question"
    ):

        with st.spinner(
            "Generating research question..."
        ):

            st.session_state.research_question = (
                generate_research_question(
                    st.session_state.gaps
                )
            )

# -----------------------------------
# DISPLAY RESEARCH QUESTION
# -----------------------------------

if st.session_state.research_question:

    st.subheader(
        "🎯 Research Question"
    )

    st.markdown(
        st.session_state.research_question
    )
# -----------------------------------
# STUDY TYPE
# -----------------------------------

study_type = st.selectbox(
    "Preferred Study Type",
    [
        "Auto Select",
        "Retrospective Cohort",
        "Prospective Cohort",
        "Case-Control",
        "Cross-Sectional",
        "Randomized Trial"
    ]
    )
# -----------------------------------
# STUDY DESIGN GENERATOR
# -----------------------------------

if st.session_state.research_question:

    if st.button(
        "📋 Generate Study Design"
    ):

        with st.spinner(
            "Designing study..."
        ):

            st.session_state.study_design = (
                generate_study_design(
                    st.session_state.research_question
                )
            )

# -----------------------------------
# DISPLAY STUDY DESIGN
# -----------------------------------

if st.session_state.study_design:

    st.subheader(
        "📋 Study Design"
    )

    st.markdown(
        st.session_state.study_design
    )
# -----------------------------------
# DATASET UPLOAD
# -----------------------------------

st.header(
    "📊 Dataset Analysis"
)

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv", "xlsx"]
)
# -----------------------------------
# LOAD DATA
# -----------------------------------

if uploaded_file:

    import pandas as pd

    if uploaded_file.name.endswith(
        ".csv"
    ):

        df = pd.read_csv(
            uploaded_file
        )

    else:

        df = pd.read_excel(
            uploaded_file
        )

    st.dataframe(
        df.head()
    )

# -----------------------------------
# DATASET REPORT
# -----------------------------------

if uploaded_file:

    if st.button(
        "Analyze Dataset"
    ):

        report = analyze_dataset(
            df
        )

        st.session_state.dataset_report = (
            report
        )

# -----------------------------------
# DISPLAY REPORT
# -----------------------------------

if st.session_state.dataset_report:

    st.subheader(
        "Dataset Overview"
    )

    st.text(
        st.session_state.dataset_report
    )
# -----------------------------------
# STATISTICAL ANALYSIS
# -----------------------------------

if uploaded_file:

    if st.button(
        "📈 Generate Statistics"
    ):

        st.subheader(
            "Descriptive Statistics"
        )

        stats = descriptive_statistics(
            df
        )

        st.dataframe(
            stats
        )

        st.subheader(
            "Categorical Variables"
        )

        categories = categorical_summary(
            df
        )

        for variable, table in categories.items():

            st.markdown(
                f"### {variable}"
            )

            st.dataframe(
                table
            )
# -----------------------------------
# GROUP COMPARISON
# -----------------------------------

if uploaded_file:

    st.subheader(
        "Group Comparison (T-Test)"
    )

    numeric_cols = list(
        df.select_dtypes(
            include="number"
        ).columns
    )

    group_cols = list(
        df.columns
    )

    outcome = st.selectbox(
        "Outcome Variable",
        numeric_cols
    )

    group = st.selectbox(
        "Group Variable",
        group_cols
    )

    if st.button(
        "Run T-Test"
    ):

        results = compare_groups(
            df,
            outcome,
            group
        )

        if "error" in results:

            st.error(
                results["error"]
            )

        else:

            st.write(
                f"Group 1: {results['group1']}"
            )

            st.write(
                f"Mean: {results['mean1']}"
            )

            st.write(
                f"Group 2: {results['group2']}"
            )

            st.write(
                f"Mean: {results['mean2']}"
            )

            st.write(
                f"P-value: {results['p_value']}"
            )
