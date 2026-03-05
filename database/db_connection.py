import psycopg2


def get_connection():

    connection = psycopg2.connect(
        host="localhost",
        database="jobs_db",
        user="postgres",
        password="postgres"
    )

    return connection