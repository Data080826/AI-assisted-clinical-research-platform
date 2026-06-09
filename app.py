# -----------------------------------
# IMPORTS
# -----------------------------------

import streamlit as st

from openai import OpenAI

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
    page_title="Research Copilot",
    page_icon="📚",
    layout="wide"
)

# ----------------------------
# HERO BANNER
# ----------------------------

st.markdown("""
<style>

.hero-container{
    padding:30px;
    border-radius:20px;
    text-align:center;

    background: linear-gradient(
        135deg,
        #071A2E 0%,
        #0B2545 50%,
        #1E3A8A 100%
    );

    margin-bottom:25px;
}

.hero-title{
    font-size: clamp(2.2rem, 5vw, 5rem);
    font-weight:700;
    letter-spacing:6px;

    background: linear-gradient(
        90deg,
        #00C6FF,
        #5B7FFF,
        #8B5CF6,
        #D946EF,
        #00C6FF
    );

    background-size:300% auto;

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;

    animation: gradientMove 8s linear infinite;
}

.hero-subtitle{
    color:#d1d5db;
    font-size:1.15rem;
    margin-top:10px;
    margin-bottom:20px;
}

.badge{
    display:inline-block;
    padding:8px 16px;
    margin:5px;
    border-radius:20px;
    background:rgba(255,255,255,0.12);
    color:white;
    font-size:0.9rem;
}

@keyframes gradientMove {
    0% {background-position:0% center;}
    100% {background-position:300% center;}
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-container">

<div class="hero-title">
🧬 RESEARCH COPILOT
</div>

<div class="hero-subtitle">
Transform research questions into literature reviews,study designs, 
statistical analyses, and publication-ready insights.
</div>

<span class="badge">🔬 Literature Review</span>
<span class="badge">🧪 Study Design</span>
<span class="badge">📈 Statistical Analysis</span>
<span class="badge">🤖 AI Assistant</span>

</div>
""", unsafe_allow_html=True)


# ----------------------------
# REST OF APP
# ----------------------------
st.sidebar.title("Navigation")

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "api_key_active" not in st.session_state:
    st.session_state.api_key_active = None
    
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

if "df" not in st.session_state:
    st.session_state.df = None

# -----------------------------------
# SIDEBAR
# -----------------------------------
with st.sidebar:

    # -----------------------------------
    # USER API KEY
    # -----------------------------------

    st.markdown("""
    Enter your OpenAI API key
    to enable Real AI responses
    """)

    with st.form("api_key_form"):

        user_api_key = st.text_input(
            "",
            type="password",
            placeholder="sk-...",
            help="Your API key is never stored"
        )

        submitted = st.form_submit_button(
            "🔑 Activate API Key"
        )

        if submitted:

            if not user_api_key:

                st.warning(
                    "Please enter an API key."
                )

            else:

                try:

                    client = OpenAI(
                        api_key=user_api_key
                    )

                    # Verify key
                    client.models.list()

                    st.session_state.api_key_active = (
                        user_api_key
                    )

                    st.success(
                        "✅ API Key Verified"
                    )

                except Exception as e:

                    st.error(
                        f"❌ Invalid API key: {str(e)}"
                    )

    if st.session_state.api_key_active:

        st.success(
            "🟢 OpenAI Connected"
        )

        if st.button(
            "❌ Disconnect API Key"
        ):

            st.session_state.api_key_active = None
            st.rerun()

    else:

        st.info(
            "🔴 OpenAI Not Connected"
        )

    st.markdown(
        "[Get your API key from OpenAI Platform](https://platform.openai.com/api-keys)"
    )

    st.write("---")
    
# -----------------------------------
# API KEY REQUIRED
# -----------------------------------

if not st.session_state.api_key_active:

    st.warning(
        "🔑 Please activate your OpenAI API key in the sidebar to use the app."
    )

    st.stop()

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

        if not st.session_state.api_key_active:
            st.warning(
                "Please activate your OpenAI API key first."
            )
            st.stop()

        with st.spinner(
            "Analyzing literature..."
        ):

            st.session_state.summary = (
                generate_literature_summary(
                    st.session_state.papers,
                    st.session_state.api_key_active
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
                    st.session_state.summary,
                    st.session_state.api_key_active
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
                    st.session_state.gaps,
                    st.session_state.api_key_active
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
                   st.session_state.research_question,
                   study_type,
                   st.session_state.api_key_active
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
# RESET DATASET STATE
# -----------------------------------

if uploaded_file is None:

    st.session_state.dataset_report = ""

    if "outcome_variable" in st.session_state:
        del st.session_state["outcome_variable"]

    if "group_variable" in st.session_state:
        del st.session_state["group_variable"]
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
    if uploaded_file is None:

        st.session_state.df = None
        st.session_state.dataset_report = ""

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

if uploaded_file and st.session_state.dataset_report:

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

    outcome = st.selectbox(
    "Outcome Variable",
    numeric_cols,
    key="outcome_variable"
)
    group_cols = []

    for col in df.columns:

        if col == outcome:
            continue

        unique_values = (
            df[col]
            .dropna()
            .nunique()
        )

        if unique_values == 2:

            group_cols.append(col)
        
 

    # -----------------------------------
    # BINARY GROUP VARIABLES
    # -----------------------------------

    if not group_cols:

        st.warning(
            "No binary group variables found. "
            "A T-test requires a grouping variable "
            "with exactly two unique values."
        )

    else:

        group = st.selectbox(
            "Group Variable",
            group_cols,
            key="group_variable"
        )
    
    st.info(
    """
    Outcome Variable:
    Continuous numeric variable

    Group Variable:
    Binary variable with exactly two groups
    (e.g. Treatment vs Control)
    """
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
