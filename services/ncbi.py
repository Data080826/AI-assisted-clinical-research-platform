from Bio import Entrez

def search_pubmed(query, max_results=20):

    handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=max_results
    )

    record = Entrez.read(handle)

    return record["IdList"]
