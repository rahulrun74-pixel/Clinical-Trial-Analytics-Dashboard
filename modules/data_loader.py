import os
import pandas as pd

DEFAULT_PATH = "data/clinical_trial_data.csv"


def load_data(uploaded_file=None):
    """
    Load clinical trial dataset.

    Priority:
    1. Uploaded CSV
    2. Default dataset
    """

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df

    if os.path.exists(DEFAULT_PATH):
        df = pd.read_csv(DEFAULT_PATH)
        return df

    raise FileNotFoundError(
        "clinical_trial_data.csv not found in data folder."
    )


def get_dataset_info(df):
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum()),
    }