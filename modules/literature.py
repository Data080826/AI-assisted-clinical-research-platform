from services.openai_service import ask_ai


def generate_literature_summary(papers):

    literature_text = ""

    for paper in papers:

        literature_text += f"""
Title: {paper['Title']}
Journal: {paper['Journal']}
PMID: {paper['PMID']}

Abstract:
{paper.get('Abstract', 'No abstract available')}

------------------------------------
"""

    prompt = f"""
You are an expert clinical research scientist.

Review the provided papers.

Return your analysis in markdown using:

## Literature Overview

## Major Findings

## Areas of Agreement

## Areas of Disagreement

## Current Limitations

## Knowledge Gaps

## Future Research Directions

Papers:

{literature_text}
"""

    return ask_ai(prompt)
