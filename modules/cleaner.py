import pandas as pd


def clean_data(df):
    """
    Clean clinical trial dataset.
    """

    # --------------------------
    # Remove duplicate rows
    # --------------------------
    df = df.drop_duplicates()

    # --------------------------
    # Remove duplicate Patient IDs
    # --------------------------
    df = df.drop_duplicates(subset="Patient_ID")

    # --------------------------
    # Fill missing numerical values
    # --------------------------
    numeric_cols = [
        "Age",
        "BMI",
        "Blood_Pressure",
        "Cholesterol",
        "Heart_Rate",
        "Recovery_Days"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())

    # --------------------------
    # Fill missing categorical values
    # --------------------------
    categorical_cols = [
        "Gender",
        "Diabetes",
        "Smoking",
        "Disease_Severity",
        "Treatment_Group",
        "Adverse_Event",
        "Outcome",
        "Follow_Up"
    ]

    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].mode()[0])

    # --------------------------
    # Fix impossible values
    # --------------------------
    if "Age" in df.columns:
        df["Age"] = df["Age"].clip(18, 100)

    if "BMI" in df.columns:
        df["BMI"] = df["BMI"].clip(15, 45)

    if "Blood_Pressure" in df.columns:
        df["Blood_Pressure"] = df["Blood_Pressure"].clip(70, 220)

    if "Cholesterol" in df.columns:
        df["Cholesterol"] = df["Cholesterol"].clip(80, 400)

    if "Heart_Rate" in df.columns:
        df["Heart_Rate"] = df["Heart_Rate"].clip(40, 180)

    if "Recovery_Days" in df.columns:
        df["Recovery_Days"] = df["Recovery_Days"].clip(1, 120)

    # --------------------------
    # Remove extra spaces
    # --------------------------
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    return df


def dataset_quality(df):
    """
    Returns quality statistics.
    """

    return {
        "Rows": len(df),
        "Columns": len(df.columns),
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum()),
        "Duplicate Patient IDs": int(df["Patient_ID"].duplicated().sum()),
    }