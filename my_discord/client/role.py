# role.py

# Standard library
import os

# Third-party libraries
import mysql.connector
from dotenv import load_dotenv


class Role:
    def __init__(self, db_connection, username):
        self.db_connection = db_connection
        self.username = username

    def get_role(self):
        cursor = self.db_connection.cursor()

        cursor.execute(
            f"SELECT role FROM account "
            f"WHERE username= '{self.username}'"
        )
        role = cursor.fetchall()[0][0]
        cursor.close()
        
        return role

    def set_role(self, role):
        cursor = self.db_connection.cursor()

        cursor.execute(
            f"UPDATE account SET role = '{role}' "
            f"WHERE username = '{self.username}'"
        )
        self.db_connection.commit()

        cursor.close()