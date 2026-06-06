# -----------------------------------
# IMPORTS
# -----------------------------------

from services.openai_service import (
    ask_ai
)

# -----------------------------------
# STUDY DESIGN GENERATOR
# -----------------------------------

def generate_study_design(
    research_question
):
    """
    Generate a clinical study design
    from a research question.
    """

    prompt = f"""
You are a clinical research expert.

Using the following research question:

{research_question}

Generate:

1. Recommended Study Design

2. Study Population

3. Inclusion Criteria

4. Exclusion Criteria

5. Exposure Definition

6. Comparator

7. Primary Outcome

8. Secondary Outcomes

9. Statistical Analysis Plan

10. Potential Limitations
"""

    return ask_ai(prompt)
