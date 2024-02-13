import mysql.connector

discord = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "CV&$i7mx$oZDrq",
    database = "discord"
)
cursor = discord.cursor()
cursor.execute("SELECT username, status FROM account")
result = cursor.fetchall()
cursor.close()
discord.close()
print(result)