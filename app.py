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

    with st.spinner("Searching PubMed..."):

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
