import pandas as pd
from db_connection import get_connection


def load_jobs():

    df = pd.read_csv("data/jobs_dataset.csv")

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO jobs (job_title, skills, domain, experience)
            VALUES (%s, %s, %s, %s)
            """,
            (row["job_title"], row["skills"], row["domain"], row["experience"])
        )

    conn.commit()

    cursor.close()
    conn.close()

    print("All jobs inserted successfully")


if __name__ == "__main__":
    load_jobs()