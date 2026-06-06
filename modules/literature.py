# services/literature.py

from services.openai_service import ask_ai


def generate_literature_summary(papers):

    literature_text = ""

    for paper in papers:
        literature_text += (
            f"Title: {paper['Title']}\n"
        )

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

    return ask_ai(prompt)
