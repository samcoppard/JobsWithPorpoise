import keyring
import psycopg2
from psycopg2.extras import DictCursor

def get_psql_password():
    # Fetch your personal access token, stored in MacOS Keychain
    postgres_password = keyring.get_password(
        "login", "postgres_password")
    return postgres_password

def connect_to_psql_database():
    #Establish the connection
    conn = psycopg2.connect(
        database="jobs_with_porpoise",
        user="postgres",
        password=get_psql_password(),
        host="localhost"
    )

    # Create a cursor object (necessary to execute SQL queries and fetch results from the database)
    # Using the DictCursor cursor allows us to pull data from the database as a list of dictionaries, rather than as a list of tuples, so we can extract individual attributes more easily / readably
    cursor = conn.cursor(cursor_factory=DictCursor)
    
    #Return the connection and cursor objects
    return conn, cursor

def close_psql_connection(conn, cursor):
    # Commit any changes made
    conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

