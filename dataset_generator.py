import os
import random
import numpy as np
import pandas as pd

# -----------------------------
# Reproducibility
# -----------------------------
random.seed(42)
np.random.seed(42)

rows = 1000

patients = []

for i in range(rows):

    patient_id = f"PT{i+1:04d}"

    age = random.randint(18, 85)

    gender = random.choice(["Male", "Female"])

    bmi = round(np.random.normal(26, 4), 1)
    bmi = max(16, min(40, bmi))

    blood_pressure = int(np.random.normal(120 + (age-40)*0.4, 10))

    cholesterol = int(np.random.normal(180 + (age-40)*0.8, 20))

    heart_rate = random.randint(60, 100)

    diabetes = random.choices(
        ["Yes", "No"],
        weights=[25, 75]
    )[0]

    smoking = random.choices(
        ["Yes", "No"],
        weights=[30, 70]
    )[0]

    severity = random.choices(
        ["Mild", "Moderate", "Severe"],
        weights=[40, 40, 20]
    )[0]

    treatment = random.choice(
        ["Drug A", "Drug B", "Drug C"]
    )

    # -----------------------------
    # Recovery Days
    # -----------------------------

    recovery = random.randint(5, 12)

    if age > 60:
        recovery += random.randint(3, 8)

    if bmi > 30:
        recovery += 2

    if diabetes == "Yes":
        recovery += 3

    if severity == "Moderate":
        recovery += 4

    if severity == "Severe":
        recovery += 8

    if treatment == "Drug B":
        recovery -= 2

    recovery = max(recovery, 3)

    # -----------------------------
    # Adverse Events
    # -----------------------------

    adverse_probability = 0.05

    if severity == "Moderate":
        adverse_probability += 0.10

    if severity == "Severe":
        adverse_probability += 0.25

    if age > 65:
        adverse_probability += 0.10

    adverse = np.random.choice(
        ["Yes", "No"],
        p=[
            adverse_probability,
            1-adverse_probability
        ]
    )

    # -----------------------------
    # Outcome
    # -----------------------------

    outcome = "Recovered"

    if recovery > 25:
        outcome = "Not Recovered"

    followup = random.choices(
        [
            "Completed",
            "Ongoing",
            "Lost"
        ],
        weights=[
            85,
            10,
            5
        ]
    )[0]

    patients.append([
        patient_id,
        age,
        gender,
        bmi,
        blood_pressure,
        cholesterol,
        heart_rate,
        diabetes,
        smoking,
        severity,
        treatment,
        recovery,
        adverse,
        outcome,
        followup
    ])

columns = [

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

df = pd.DataFrame(
    patients,
    columns=columns
)

os.makedirs("data", exist_ok=True)

df.to_csv(
    "data/clinical_trial_data.csv",
    index=False
)

print(df.head())

print()

print("Dataset Created Successfully")

print(df.shape)