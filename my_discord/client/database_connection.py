# database_connection.py

# Standard library
import os

# Third-party libraries
import mysql.connector
from dotenv import load_dotenv


def db_connection():
    load_dotenv(dotenv_path="p.env")

    db_connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_DATABASE"),
    )
    return db_connection

