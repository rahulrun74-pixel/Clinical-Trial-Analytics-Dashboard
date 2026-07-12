import pandas as pd


def generate_insights(df):

    insights = []

    # -----------------------------
    # Recovery Rate
    # -----------------------------

    recovery_rate = (
        (df["Outcome"] == "Recovered").mean()
        * 100
    )

    if recovery_rate >= 90:

        insights.append(
            "✅ Excellent overall recovery rate."
        )

    elif recovery_rate >= 75:

        insights.append(
            "🟡 Recovery rate is acceptable but could be improved."
        )

    else:

        insights.append(
            "🔴 Low recovery rate detected. Review treatment strategy."
        )

    # -----------------------------
    # Adverse Events
    # -----------------------------

    adverse_rate = (
        (df["Adverse_Event"] == "Yes").mean()
        * 100
    )

    if adverse_rate > 20:

        insights.append(
            "⚠ High adverse event rate observed."
        )

    else:

        insights.append(
            "✅ Adverse event rate is within acceptable limits."
        )

    # -----------------------------
    # Average Age
    # -----------------------------

    age = df["Age"].mean()

    if age > 60:

        insights.append(
            "Older patient population may require longer recovery monitoring."
        )

    # -----------------------------
    # BMI
    # -----------------------------

    bmi = df["BMI"].mean()

    if bmi > 28:

        insights.append(
            "Higher average BMI may influence treatment outcome."
        )

    # -----------------------------
    # Best Treatment
    # -----------------------------

    success = (
        df.groupby("Treatment_Group")["Outcome"]
        .apply(lambda x: (x == "Recovered").mean())
    )

    best = success.idxmax()

    insights.append(
        f"🏆 Best performing treatment: {best}"
    )

    # -----------------------------
    # Worst Treatment
    # -----------------------------

    worst = success.idxmin()

    insights.append(
        f"📉 Lowest performing treatment: {worst}"
    )

    # -----------------------------
    # Average Recovery
    # -----------------------------

    recovery_days = df["Recovery_Days"].mean()

    insights.append(
        f"Average recovery time is {recovery_days:.1f} days."
    )

    # -----------------------------
    # Diabetes
    # -----------------------------

    diabetes = (
        (df["Diabetes"] == "Yes").mean()
        * 100
    )

    insights.append(
        f"{diabetes:.1f}% of patients have diabetes."
    )

    # -----------------------------
    # Smoking
    # -----------------------------

    smoking = (
        (df["Smoking"] == "Yes").mean()
        * 100
    )

    insights.append(
        f"{smoking:.1f}% of patients are smokers."
    )

    return insights