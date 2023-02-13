import mysql.connector

from helper import champion_names, release_year


# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="loldle"
)

# Create a cursor
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM champions")

for row in mycursor:
    print(row)

