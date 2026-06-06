from Bio import Entrez
import streamlit as st

Entrez.email = st.secrets["NCBI_EMAIL"]
Entrez.api_key = st.secrets["NCBI_API_KEY"]


def search_pubmed(query, max_results=10):

    handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=max_results
    )

    record = Entrez.read(handle)
    handle.close()

    return record["IdList"]


def fetch_pubmed_details(pmids):

    if not pmids:
        return []

    handle = Entrez.esummary(
        db="pubmed",
        id=",".join(pmids)
    )

    records = Entrez.read(handle)
    handle.close()

    papers = []

    for item in records:

        papers.append(
            {
                "Title": item.get("Title", ""),
                "Journal": item.get("FullJournalName", ""),
                "Date": item.get("PubDate", ""),
                "PMID": item.get("Id", "")
            }
        )

    return papers
