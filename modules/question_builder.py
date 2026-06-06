# -----------------------------------
# IMPORTS
# -----------------------------------

from services.openai_service import (
    ask_ai
)

# -----------------------------------
# RESEARCH QUESTION GENERATOR
# -----------------------------------

def generate_research_question(
    knowledge_gaps
):
    """
    Generate a research question
    from identified knowledge gaps.
    """

    prompt = f"""
You are a clinical research expert.

Using the following research gaps:

{knowledge_gaps}

Generate:

1. Primary Research Question

2. PICO Framework

3. Hypothesis

4. Primary Outcome

5. Secondary Outcomes

6. Recommended Study Design
"""

    return ask_ai(prompt)
