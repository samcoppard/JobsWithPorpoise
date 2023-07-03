import psycopg2
from psycopg2.extras import DictCursor
import yaml


def connect_to_psql_database():
    """Establish a connection to the local PSQL database, and create a DictCursor object"""

    # Get the connection details from config.yaml
    with open("./JobsWithPorpoise/config.yaml", "r") as file:
        database_connection_details = yaml.safe_load(file)["database"]

    # Establish the connection
    conn = psycopg2.connect(
        database=database_connection_details["name"],
        user=database_connection_details["user"],
        password=database_connection_details["password"],
        host=database_connection_details["host"],
    )

    # Create a cursor object (to execute SQL queries and fetch results from the database)
    # Using DictCursor means we can pull data from the database as a list of dictionaries,
    # (rather than a list of tuples), so we can extract individual attributes more easily
    cursor = conn.cursor(cursor_factory=DictCursor)

    # Return the connection and cursor objects
    return conn, cursor


def close_psql_connection(conn, cursor):
    """Commit any changes made and close the PSQL connection"""

    conn.commit()
    cursor.close()
    conn.close()
