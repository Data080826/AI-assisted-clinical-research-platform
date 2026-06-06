# -----------------------------------
# IMPORTS
# -----------------------------------

import pandas as pd

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
