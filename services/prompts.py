SUMMARY_PROMPT = """
Review the literature below.

Provide:

1. Main findings
2. Areas of agreement
3. Limitations
4. Future directions

Literature:
{literature}
"""

GAP_PROMPT = """
Based on the literature summary below:

Identify 5 research gaps.

Rank them by:

- Novelty
- Clinical impact
- Feasibility

Summary:
{summary}
"""

QUESTION_PROMPT = """
Using the following gap:

Generate:

- PICO question
- Hypothesis
- Primary outcome
- Secondary outcomes

Gap:
{gap}
"""

STUDY_PROMPT = """
Using the research question below:

Recommend:

- Study design
- Inclusion criteria
- Exclusion criteria
- Exposure
- Comparator
- Outcomes

Question:
{question}
"""
