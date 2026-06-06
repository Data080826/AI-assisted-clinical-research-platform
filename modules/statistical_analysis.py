# -----------------------------------
# IMPORTS
# -----------------------------------

import pandas as pd

from scipy.stats import (
    ttest_ind
)

# -----------------------------------
# DESCRIPTIVE STATISTICS
# -----------------------------------

def descriptive_statistics(df):
    """
    Generate descriptive statistics
    for numerical variables.
    """

    return df.describe().transpose()

# -----------------------------------
# CATEGORICAL SUMMARY
# -----------------------------------

def categorical_summary(df):
    """
    Generate counts and percentages
    for categorical variables.
    """

    summaries = {}

    categorical_cols = df.select_dtypes(
        include=["object", "category"]
    ).columns

    for col in categorical_cols:

        counts = (
            df[col]
            .value_counts(dropna=False)
            .reset_index()
        )

        counts.columns = [
            col,
            "Count"
        ]

        counts["Percent"] = (
            counts["Count"]
            / counts["Count"].sum()
            * 100
        ).round(2)

        summaries[col] = counts

    return summaries

# -----------------------------------
# T TEST
# -----------------------------------

def compare_groups(
    df,
    outcome,
    group
):

    if outcome not in df.columns:

        return {
            "error":
            f"Outcome column '{outcome}' not found."
        }

    if group not in df.columns:

        return {
            "error":
            f"Group column '{group}' not found."
        }

    groups = df[group].dropna().unique()

    if len(groups) != 2:

        return {
            "error":
            "Group variable must contain exactly two groups."
        }

    group1 = df[
        df[group] == groups[0]
    ][outcome].dropna()

    group2 = df[
        df[group] == groups[1]
    ][outcome].dropna()

    t_stat, p_value = ttest_ind(
        group1,
        group2,
        equal_var=False
    )

    return {
        "group1": str(groups[0]),
        "group2": str(groups[1]),
        "mean1": round(group1.mean(), 2),
        "mean2": round(group2.mean(), 2),
        "p_value": round(p_value, 4)
    }
