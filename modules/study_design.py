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
    research_question,
    study_type
):
    """
    Generate a clinical study design
    from a research question.
    """

    prompt = f"""
You are a clinical research methodologist.

Using the following research question:

{research_question}

First determine the most appropriate study design from:

- Retrospective Cohort Study
- Prospective Cohort Study
- Case-Control Study
- Cross-Sectional Study
- Randomized Clinical Trial

Explain why the selected design is best.

Then generate:

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

11. Database Requirements

12. Suggested TriNetX/Epic Cosmos Cohort Definition
"""

    return ask_ai(prompt)
