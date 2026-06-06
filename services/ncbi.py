# -----------------------------------
# IMPORTS
# -----------------------------------

from Bio import Entrez
import streamlit as st

# -----------------------------------
# NCBI CONFIGURATION
# -----------------------------------

Entrez.email = st.secrets["NCBI_EMAIL"]
Entrez.api_key = st.secrets["NCBI_API_KEY"]

# -----------------------------------
# PUBMED SEARCH
# -----------------------------------

def search_pubmed(
    query,
    max_results=10
):

    handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=max_results
    )

    record = Entrez.read(handle)

    handle.close()

    return record["IdList"]

# -----------------------------------
# PUBMED DETAILS
# -----------------------------------

from Bio import Entrez


def fetch_pubmed_details(pmids):

    if not pmids:
        return []

    handle = Entrez.efetch(
        db="pubmed",
        id=",".join(pmids),
        rettype="abstract",
        retmode="xml"
    )

    records = Entrez.read(handle)

    handle.close()

    papers = []

    for article in records["PubmedArticle"]:

        article_data = article["MedlineCitation"]["Article"]

        title = article_data.get(
            "ArticleTitle",
            ""
        )

        journal = article_data["Journal"].get(
            "Title",
            ""
        )

        pmid = str(
            article["MedlineCitation"]["PMID"]
        )

        abstract = ""

        if "Abstract" in article_data:

            abstract_parts = article_data[
                "Abstract"
            ].get(
                "AbstractText",
                []
            )

            abstract = " ".join(
                str(part)
                for part in abstract_parts
            )

        papers.append(
            {
                "Title": str(title),
                "Journal": str(journal),
                "PMID": pmid,
                "Abstract": abstract
            }
        )

    return papers
