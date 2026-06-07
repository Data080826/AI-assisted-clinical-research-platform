# services/gaps.py

from services.openai_service import ask_ai


def find_research_gaps(
    summary,
    api_key
):

    prompt = f"""
You are a clinical research expert.

Based on this literature summary:

{summary}

Identify:

1. Major knowledge gaps
2. Understudied populations
3. Unanswered clinical questions
4. Potential future research topics

Rank each gap by:

- Clinical Impact (1-10)
- Novelty (1-10)
- Feasibility (1-10)
"""

    return ask_ai(
        prompt,
        api_key
    )
