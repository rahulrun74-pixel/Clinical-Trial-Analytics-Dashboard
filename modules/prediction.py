import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)


def train_models(df):

    data = df.copy()

    # -----------------------------
    # Encode categorical columns
    # -----------------------------

    encoders = {}

    categorical = [
        "Gender",
        "Diabetes",
        "Smoking",
        "Disease_Severity",
        "Treatment_Group"
    ]

    for col in categorical:

        le = LabelEncoder()

        data[col] = le.fit_transform(data[col])

        encoders[col] = le

    target = LabelEncoder()

    data["Outcome"] = target.fit_transform(
        data["Outcome"]
    )

    # -----------------------------
    # Features
    # -----------------------------

    X = data[
        [
            "Age",
            "BMI",
            "Blood_Pressure",
            "Cholesterol",
            "Heart_Rate",
            "Gender",
            "Diabetes",
            "Smoking",
            "Disease_Severity",
            "Treatment_Group"
        ]
    ]

    y = data["Outcome"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # -----------------------------
    # Random Forest
    # -----------------------------

    rf = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    rf.fit(
        X_train,
        y_train
    )

    pred = rf.predict(X_test)

    prob = rf.predict_proba(X_test)[:, 1]

    metrics = {

        "Accuracy":
        accuracy_score(y_test, pred),

        "Precision":
        precision_score(y_test, pred),

        "Recall":
        recall_score(y_test, pred),

        "F1":
        f1_score(y_test, pred),

        "ROC_AUC":
        roc_auc_score(y_test, prob)

    }

    cm = confusion_matrix(
        y_test,
        pred
    )

    return {

        "model": rf,

        "metrics": metrics,

        "confusion_matrix": cm,

        "X_test": X_test,

        "y_test": y_test,

        "probabilities": prob,

        "encoders": encoders,

        "target_encoder": target

    }


def feature_importance(model):

    importance = pd.DataFrame({

        "Feature": [

            "Age",
            "BMI",
            "Blood_Pressure",
            "Cholesterol",
            "Heart_Rate",
            "Gender",
            "Diabetes",
            "Smoking",
            "Disease_Severity",
            "Treatment_Group"

        ],

        "Importance":
        model.feature_importances_

    })

    importance = importance.sort_values(
        by="Importance",
        ascending=False
    )

    return importance