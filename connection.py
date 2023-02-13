import psycopg2
from psycopg2 import Error


def connect():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user="user",
                                    password="password",
                                    host="localhost",
                                    port="8888",
                                    database="database")

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    return cursor

