import os
import pandas as pd
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)


def export_csv(df):

    path = os.path.join(
        REPORT_FOLDER,
        "clinical_trial_report.csv"
    )

    df.to_csv(path, index=False)

    return path


def export_excel(df):

    path = os.path.join(
        REPORT_FOLDER,
        "clinical_trial_report.xlsx"
    )

    df.to_excel(
        path,
        index=False,
        engine="openpyxl"
    )

    return path


def export_pdf(df):

    path = os.path.join(
        REPORT_FOLDER,
        "clinical_trial_report.pdf"
    )

    doc = SimpleDocTemplate(path)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>Clinical Trial Analytics Report</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            f"Total Patients : {len(df)}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Recovered : {(df['Outcome']=='Recovered').sum()}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Not Recovered : {(df['Outcome']=='Not Recovered').sum()}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Average Age : {df['Age'].mean():.1f}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Average BMI : {df['BMI'].mean():.1f}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Average Recovery Days : {df['Recovery_Days'].mean():.1f}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Adverse Events : {(df['Adverse_Event']=='Yes').sum()}",
            styles["BodyText"]
        )
    )

    doc.build(story)

    return path