import pandas as pd


def calculate_metrics(df):

    total_patients = len(df)

    avg_age = round(df["Age"].mean(), 1)

    avg_bmi = round(df["BMI"].mean(), 1)

    avg_recovery = round(
        df["Recovery_Days"].mean(),
        1
    )

    recovery_rate = round(
        (
            df["Outcome"]
            .eq("Recovered")
            .mean()
        ) * 100,
        1
    )

    adverse_rate = round(
        (
            df["Adverse_Event"]
            .eq("Yes")
            .mean()
        ) * 100,
        1
    )

    diabetes_rate = round(
        (
            df["Diabetes"]
            .eq("Yes")
            .mean()
        ) * 100,
        1
    )

    smoking_rate = round(
        (
            df["Smoking"]
            .eq("Yes")
            .mean()
        ) * 100,
        1
    )

    return {

        "Total Patients": total_patients,

        "Average Age": avg_age,

        "Average BMI": avg_bmi,

        "Average Recovery Days": avg_recovery,

        "Recovery Rate": recovery_rate,

        "Adverse Event Rate": adverse_rate,

        "Diabetes Rate": diabetes_rate,

        "Smoking Rate": smoking_rate

    }


def gender_distribution(df):

    return (
        df["Gender"]
        .value_counts()
        .reset_index()
        .rename(
            columns={
                "index": "Gender",
                "Gender": "Count"
            }
        )
    )


def severity_distribution(df):

    return (
        df["Disease_Severity"]
        .value_counts()
        .reset_index()
        .rename(
            columns={
                "index": "Severity",
                "Disease_Severity": "Count"
            }
        )
    )


def treatment_distribution(df):

    return (
        df["Treatment_Group"]
        .value_counts()
        .reset_index()
        .rename(
            columns={
                "index": "Treatment",
                "Treatment_Group": "Count"
            }
        )
    )


def treatment_success(df):

    success = (
        df.groupby("Treatment_Group")["Outcome"]
        .apply(
            lambda x:
            (
                x == "Recovered"
            ).mean() * 100
        )
        .reset_index()
    )

    success.columns = [
        "Treatment_Group",
        "Success_Rate"
    ]

    return success


def age_summary(df):

    return {

        "Minimum Age":
        int(df["Age"].min()),

        "Maximum Age":
        int(df["Age"].max()),

        "Average Age":
        round(df["Age"].mean(), 1)

    }


def bmi_summary(df):

    return {

        "Minimum BMI":
        round(df["BMI"].min(), 1),

        "Maximum BMI":
        round(df["BMI"].max(), 1),

        "Average BMI":
        round(df["BMI"].mean(), 1)

    }