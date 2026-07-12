import os
import sqlite3
import pandas as pd

DATABASE_FOLDER = "database"
DATABASE_NAME = "clinical_trials.db"
TABLE_NAME = "clinical_trials"


def create_database():

    os.makedirs(DATABASE_FOLDER, exist_ok=True)

    conn = sqlite3.connect(
        os.path.join(
            DATABASE_FOLDER,
            DATABASE_NAME
        )
    )

    conn.close()


def save_dataframe(df):

    create_database()

    conn = sqlite3.connect(
        os.path.join(
            DATABASE_FOLDER,
            DATABASE_NAME
        )
    )

    df.to_sql(
        TABLE_NAME,
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()


def load_dataframe():

    create_database()

    conn = sqlite3.connect(
        os.path.join(
            DATABASE_FOLDER,
            DATABASE_NAME
        )
    )

    cursor = conn.cursor()

    cursor.execute(
        f"""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        AND name='{TABLE_NAME}'
        """
    )

    exists = cursor.fetchone()

    if exists is None:

        conn.close()

        return pd.DataFrame()

    df = pd.read_sql(
        f"SELECT * FROM {TABLE_NAME}",
        conn
    )

    conn.close()

    return df


def delete_database():

    db = os.path.join(
        DATABASE_FOLDER,
        DATABASE_NAME
    )

    if os.path.exists(db):

        os.remove(db)


def row_count():

    df = load_dataframe()

    return len(df)


def database_exists():

    db = os.path.join(
        DATABASE_FOLDER,
        DATABASE_NAME
    )

    return os.path.exists(db)