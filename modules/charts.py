import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def age_distribution(df):

    fig = px.histogram(
        df,
        x="Age",
        nbins=20,
        title="Age Distribution",
        template="plotly_white",
    )

    return fig


def bmi_distribution(df):

    fig = px.histogram(
        df,
        x="BMI",
        nbins=20,
        title="BMI Distribution",
        template="plotly_white",
    )

    return fig


def recovery_distribution(df):

    fig = px.histogram(
        df,
        x="Recovery_Days",
        nbins=20,
        title="Recovery Days Distribution",
        template="plotly_white",
    )

    return fig


def gender_chart(df):

    counts = df["Gender"].value_counts().reset_index()
    counts.columns = ["Gender", "Count"]

    fig = px.pie(
        counts,
        names="Gender",
        values="Count",
        hole=0.4,
        title="Gender Distribution",
    )

    return fig


def severity_chart(df):

    counts = df["Disease_Severity"].value_counts().reset_index()
    counts.columns = ["Severity", "Count"]

    fig = px.pie(
        counts,
        names="Severity",
        values="Count",
        hole=0.4,
        title="Disease Severity",
    )

    return fig


def treatment_chart(df):

    counts = df["Treatment_Group"].value_counts().reset_index()
    counts.columns = ["Treatment", "Count"]

    fig = px.bar(
        counts,
        x="Treatment",
        y="Count",
        text_auto=True,
        title="Treatment Groups",
        template="plotly_white",
    )

    return fig


def outcome_chart(df):

    counts = df["Outcome"].value_counts().reset_index()
    counts.columns = ["Outcome", "Count"]

    fig = px.bar(
        counts,
        x="Outcome",
        y="Count",
        text_auto=True,
        title="Treatment Outcome",
        template="plotly_white",
    )

    return fig


def adverse_chart(df):

    counts = df["Adverse_Event"].value_counts().reset_index()
    counts.columns = ["Adverse Event", "Count"]

    fig = px.bar(
        counts,
        x="Adverse Event",
        y="Count",
        text_auto=True,
        title="Adverse Events",
        template="plotly_white",
    )

    return fig


def correlation_heatmap(df):

    numeric = df.select_dtypes(include="number")

    corr = numeric.corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        title="Correlation Heatmap",
        aspect="auto",
    )

    return fig


def treatment_recovery(df):

    recovery = (
        df.groupby("Treatment_Group")["Recovery_Days"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        recovery,
        x="Treatment_Group",
        y="Recovery_Days",
        text_auto=".1f",
        title="Average Recovery Days by Treatment",
        template="plotly_white",
    )

    return fig