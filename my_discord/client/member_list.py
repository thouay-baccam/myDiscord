# MemberList.py
import mysql.connector

class MemberList:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_usernames(self):
        # Query the database to get all usernames
        cursor = self.db_connection.cursor()
        select_query = "SELECT username FROM account"
        cursor.execute(select_query)
        result = cursor.fetchall()
        cursor.close()

        # Convert the result to a list of usernames
        usernames = [row[0] for row in result]
        return usernames
