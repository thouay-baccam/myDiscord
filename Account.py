import os
from dotenv import load_dotenv

import mysql.connector

class Account:
    def __init__(self, username):
        self.username = username

    def connect(self): ## REPETITION, A FIX!!
        load_dotenv(dotenv_path="pass.env")

        db_connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
            database=os.getenv("DB_DATABASE")
        )
        return db_connection

    def get_role(self):
        db_connection = self.connect()
        cursor = db_connection.cursor()

        # TEMPORAIREMENT ID
        cursor.execute(f"SELECT role FROM account WHERE username={self.username}")
        role = cursor.fetchall()[0][0]

        cursor.close()
        db_connection.close()
        
        return role