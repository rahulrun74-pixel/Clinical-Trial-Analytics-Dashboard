import streamlit as st
import pandas as pd

from modules.prediction import (
    train_models,
    feature_importance
)
from modules.data_loader import load_data
from modules.cleaner import clean_data
from modules.analytics import calculate_metrics
from modules.database import (
    create_database,
    save_dataframe,
    load_dataframe,
)
from modules.utils import (
    validate_dataset,
    dataset_summary,
)
from modules.insights import generate_insights
from modules.report import (
    export_csv,
    export_excel,
    export_pdf
)

st.set_page_config(
    page_title="Clinical Trial Analytics Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

create_database()

if "df" not in st.session_state:
    st.session_state.df = clean_data(load_data())

df = st.session_state.df

st.title("🏥 Clinical Trial Data Analytics Dashboard")

st.caption(
    "Healthcare Analytics • Machine Learning • Clinical Intelligence"
)

st.divider()

st.sidebar.title("Clinical Trial Dashboard")

uploaded = st.sidebar.file_uploader(
    "Upload Clinical Trial CSV",
    type=["csv"]
)

if uploaded is not None:

    df = load_data(uploaded)

    valid, msg = validate_dataset(df)

    if valid:

        df = clean_data(df)

        st.session_state.df = df

        st.sidebar.success("Dataset Loaded")

    else:

        st.sidebar.error(msg)

df = st.session_state.df

st.sidebar.divider()

show_data = st.sidebar.checkbox(
    "Show Dataset",
    True
)

show_ml = st.sidebar.checkbox(
    "Machine Learning",
    True
)

show_charts = st.sidebar.checkbox(
    "Charts",
    True
)

st.sidebar.divider()

if st.sidebar.button("Save Database"):

    save_dataframe(df)

    st.sidebar.success("Saved Successfully")

if st.sidebar.button("Load Database"):

    loaded = load_dataframe()

    if len(loaded):

        st.session_state.df = loaded

        df = loaded

        st.sidebar.success("Loaded Successfully")

    else:

        st.sidebar.warning("Database Empty")

metrics = calculate_metrics(df)

st.subheader("Clinical Trial Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Patients",
    metrics["Total Patients"]
)

c2.metric(
    "Recovery Rate",
    f"{metrics['Recovery Rate']}%"
)

c3.metric(
    "Average Age",
    metrics["Average Age"]
)

c4.metric(
    "Average Recovery",
    f"{metrics['Average Recovery Days']} Days"
)

st.divider()

from modules.charts import (
    age_distribution,
    bmi_distribution,
    gender_chart,
    severity_chart,
    treatment_chart,
    outcome_chart,
    adverse_chart,
    recovery_distribution,
    correlation_heatmap,
    treatment_recovery
)

from modules.analytics import (
    gender_distribution,
    severity_distribution,
    treatment_distribution,
    treatment_success
)

# ==========================================================
# DATASET SUMMARY
# ==========================================================

summary = dataset_summary(df)

st.subheader("📋 Dataset Summary")

s1, s2, s3, s4 = st.columns(4)

s1.metric("Rows", summary["Rows"])
s2.metric("Columns", summary["Columns"])
s3.metric("Recovered", summary["Recovered"])
s4.metric("Adverse Events", summary["Adverse Events"])

st.divider()

# ==========================================================
# CHARTS
# ==========================================================

if show_charts:

    st.subheader("📊 Clinical Data Visualization")

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            age_distribution(df),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            bmi_distribution(df),
            use_container_width=True
        )

    col3, col4 = st.columns(2)

    with col3:
        st.plotly_chart(
            gender_chart(df),
            use_container_width=True
        )

    with col4:
        st.plotly_chart(
            severity_chart(df),
            use_container_width=True
        )

    col5, col6 = st.columns(2)

    with col5:
        st.plotly_chart(
            treatment_chart(df),
            use_container_width=True
        )

    with col6:
        st.plotly_chart(
            outcome_chart(df),
            use_container_width=True
        )

    st.plotly_chart(
        adverse_chart(df),
        use_container_width=True
    )

    st.plotly_chart(
        recovery_distribution(df),
        use_container_width=True
    )

    st.plotly_chart(
        treatment_recovery(df),
        use_container_width=True
    )

    st.plotly_chart(
        correlation_heatmap(df),
        use_container_width=True
    )

st.divider()

# ==========================================================
# ANALYTICS TABLES
# ==========================================================

st.subheader("📈 Clinical Analytics")

left, right = st.columns(2)

with left:

    st.markdown("### Gender Distribution")

    st.dataframe(
        gender_distribution(df),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### Disease Severity")

    st.dataframe(
        severity_distribution(df),
        use_container_width=True,
        hide_index=True
    )

with right:

    st.markdown("### Treatment Groups")

    st.dataframe(
        treatment_distribution(df),
        use_container_width=True,
        hide_index=True
    )

    st.markdown("### Treatment Success")

    success = treatment_success(df)

    success["Success_Rate"] = success["Success_Rate"].round(2)

    st.dataframe(
        success,
        use_container_width=True,
        hide_index=True
    )

st.divider()

# ==========================================================
# MACHINE LEARNING
# ==========================================================

if show_ml:

    st.subheader("🤖 Machine Learning Analysis")

    results = train_models(df)

    model = results["model"]

    metrics = results["metrics"]

    st.markdown("### Model Performance")

    m1, m2, m3, m4, m5 = st.columns(5)

    m1.metric(
        "Accuracy",
        f"{metrics['Accuracy']:.2%}"
    )

    m2.metric(
        "Precision",
        f"{metrics['Precision']:.2%}"
    )

    m3.metric(
        "Recall",
        f"{metrics['Recall']:.2%}"
    )

    m4.metric(
        "F1 Score",
        f"{metrics['F1']:.2%}"
    )

    m5.metric(
        "ROC-AUC",
        f"{metrics['ROC_AUC']:.2%}"
    )

    st.divider()

    # =====================================
    # FEATURE IMPORTANCE
    # =====================================

    importance = feature_importance(model)

    import plotly.express as px

    fig = px.bar(
        importance,
        x="Importance",
        y="Feature",
        orientation="h",
        text_auto=".3f",
        title="Feature Importance",
        template="plotly_white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================
    # CONFUSION MATRIX
    # =====================================

    st.subheader("Confusion Matrix")

    cm = results["confusion_matrix"]

    import plotly.figure_factory as ff

    fig = ff.create_annotated_heatmap(
        z=cm,
        x=["Predicted Negative","Predicted Positive"],
        y=["Actual Negative","Actual Positive"],
        colorscale="Blues"
    )

    fig.update_layout(
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # =====================================
    # PREDICT NEW PATIENT
    # =====================================

    st.subheader("🩺 Predict Patient Outcome")

    col1, col2 = st.columns(2)

    with col1:

        age = st.slider(
            "Age",
            18,
            85,
            45
        )

        bmi = st.slider(
            "BMI",
            15.0,
            40.0,
            25.0
        )

        bp = st.slider(
            "Blood Pressure",
            80,
            200,
            120
        )

        cholesterol = st.slider(
            "Cholesterol",
            100,
            350,
            180
        )

        heart = st.slider(
            "Heart Rate",
            50,
            140,
            80
        )

    with col2:

        gender = st.selectbox(
            "Gender",
            ["Male","Female"]
        )

        diabetes = st.selectbox(
            "Diabetes",
            ["No","Yes"]
        )

        smoking = st.selectbox(
            "Smoking",
            ["No","Yes"]
        )

        severity = st.selectbox(
            "Disease Severity",
            ["Mild","Moderate","Severe"]
        )

        treatment = st.selectbox(
            "Treatment",
            ["Drug A","Drug B","Drug C"]
        )

    if st.button("Predict Outcome"):

        enc = results["encoders"]

        patient = pd.DataFrame({

            "Age":[age],

            "BMI":[bmi],

            "Blood_Pressure":[bp],

            "Cholesterol":[cholesterol],

            "Heart_Rate":[heart],

            "Gender":[enc["Gender"].transform([gender])[0]],

            "Diabetes":[enc["Diabetes"].transform([diabetes])[0]],

            "Smoking":[enc["Smoking"].transform([smoking])[0]],

            "Disease_Severity":[enc["Disease_Severity"].transform([severity])[0]],

            "Treatment_Group":[enc["Treatment_Group"].transform([treatment])[0]]

        })

        pred = model.predict(patient)[0]

        outcome = results["target_encoder"].inverse_transform([pred])[0]

        if outcome == "Recovered":

            st.success(
                "✅ Predicted Outcome: Recovered"
            )

        else:

            st.error(
                "❌ Predicted Outcome: Not Recovered"
            )


# ==========================================================
# AI INSIGHTS
# ==========================================================

st.divider()

st.subheader("🧠 AI Clinical Insights")

insights = generate_insights(df)

for insight in insights:
    st.info(insight)

# ==========================================================
# EXPORT REPORTS
# ==========================================================

st.divider()

st.subheader("📄 Export Reports")

c1, c2, c3 = st.columns(3)

with c1:

    if st.button("Export CSV"):

        path = export_csv(df)

        st.success(f"Saved to {path}")

with c2:

    if st.button("Export Excel"):

        path = export_excel(df)

        st.success(f"Saved to {path}")

with c3:

    if st.button("Export PDF"):

        path = export_pdf(df)

        st.success(f"Saved to {path}")

# ==========================================================
# DATASET
# ==========================================================

if show_data:

    st.divider()

    st.subheader("📋 Clinical Trial Dataset")

    st.dataframe(
        df,
        use_container_width=True,
        height=450
    )

# ==========================================================
# DATASET INFORMATION
# ==========================================================

st.divider()

st.subheader("📊 Dataset Statistics")

stats = dataset_summary(df)

stats_df = pd.DataFrame({

    "Statistic": stats.keys(),

    "Value": stats.values()

})

st.dataframe(
    stats_df,
    hide_index=True,
    use_container_width=True
)

# ==========================================================
# ABOUT PROJECT
# ==========================================================

st.divider()

with st.expander("ℹ About This Dashboard"):

    st.markdown("""

## Clinical Trial Data Analytics Dashboard

A complete healthcare analytics application developed using Python.

### Features

- Clinical trial data cleaning
- Exploratory Data Analysis
- Interactive Plotly Dashboard
- Machine Learning Prediction
- SQLite Database
- AI Clinical Insights
- Report Generation
- CSV, Excel and PDF Export

### Technologies

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-Learn
- SQLite
- ReportLab

### Suitable For

- Healthcare Analytics
- Clinical Research
- Pharmaceutical Analytics
- Data Science Portfolio
- Biotechnology Students

""")

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
"""
<center>

## 🏥 Clinical Trial Data Analytics Dashboard

Developed using

**Python • Streamlit • Plotly • Scikit-Learn • SQLite**

Made by Rahul

© 2026

</center>
""",
unsafe_allow_html=True
)

