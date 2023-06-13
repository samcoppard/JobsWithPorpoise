import keyring
import psycopg2
from psycopg2.extras import DictCursor

def get_psql_password():
    """ Fetch PSQL password, stored locally in MacOS Keychain """
    
    postgres_password = keyring.get_password(
        "login", "postgres_password")
    
    return postgres_password


def connect_to_psql_database():
    """ Establish a connection to the local PSQL database """
    
    conn = psycopg2.connect(
        database="jobs_with_porpoise",
        user="postgres",
        password=get_psql_password(),
        host="localhost"
    )

    # Create a cursor object (necessary to execute SQL queries and fetch results from the database)
    # Using DictCursor means we can pull data from the database as a list of dictionaries,
    # (rather than a list of tuples), so we can extract individual attributes more easily
    cursor = conn.cursor(cursor_factory=DictCursor)
    
    #Return the connection and cursor objects
    return conn, cursor


def close_psql_connection(conn, cursor):
    """ Commit any changes made and close the PSQL connection """

    conn.commit()
    cursor.close()
    conn.close()

