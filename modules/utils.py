import pandas as pd


REQUIRED_COLUMNS = [
    "Patient_ID",
    "Age",
    "Gender",
    "BMI",
    "Blood_Pressure",
    "Cholesterol",
    "Heart_Rate",
    "Diabetes",
    "Smoking",
    "Disease_Severity",
    "Treatment_Group",
    "Recovery_Days",
    "Adverse_Event",
    "Outcome",
    "Follow_Up"
]


def validate_dataset(df):
    """
    Validate uploaded dataset.
    Returns (True, message) if valid.
    """

    missing = []

    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            missing.append(col)

    if len(missing) > 0:
        return False, f"Missing Columns: {', '.join(missing)}"

    return True, "Dataset is valid."


def dataset_summary(df):

    summary = {

        "Rows": len(df),

        "Columns": len(df.columns),

        "Missing Values":
            int(df.isnull().sum().sum()),

        "Duplicate Rows":
            int(df.duplicated().sum()),

        "Recovered":
            int((df["Outcome"] == "Recovered").sum()),

        "Not Recovered":
            int((df["Outcome"] == "Not Recovered").sum()),

        "Adverse Events":
            int((df["Adverse_Event"] == "Yes").sum())

    }

    return summary


def percentage(part, whole):

    if whole == 0:
        return 0

    return round((part / whole) * 100, 2)


def recovery_rate(df):

    recovered = (
        df["Outcome"] == "Recovered"
    ).sum()

    return percentage(
        recovered,
        len(df)
    )


def adverse_rate(df):

    adverse = (
        df["Adverse_Event"] == "Yes"
    ).sum()

    return percentage(
        adverse,
        len(df)
    )


def average_age(df):

    return round(
        df["Age"].mean(),
        1
    )


def average_bmi(df):

    return round(
        df["BMI"].mean(),
        1
    )


def average_recovery(df):

    return round(
        df["Recovery_Days"].mean(),
        1
    )


def treatment_counts(df):

    return (
        df["Treatment_Group"]
        .value_counts()
        .to_dict()
    )


def severity_counts(df):

    return (
        df["Disease_Severity"]
        .value_counts()
        .to_dict()
    )