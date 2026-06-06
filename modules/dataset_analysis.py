# -----------------------------------
# IMPORTS
# -----------------------------------

import pandas as pd

# -----------------------------------
# DATASET OVERVIEW
# -----------------------------------

def analyze_dataset(df):

    report = []

    report.append(
        f"Rows: {df.shape[0]}"
    )

    report.append(
        f"Columns: {df.shape[1]}"
    )

    report.append(
        "\nColumns:\n"
    )

    for col in df.columns:

        report.append(
            f"- {col} ({df[col].dtype})"
        )

    report.append(
        "\nMissing Values:\n"
    )

    missing = df.isnull().sum()

    for col, count in missing.items():

        if count > 0:

            report.append(
                f"- {col}: {count}"
            )

    return "\n".join(report)
