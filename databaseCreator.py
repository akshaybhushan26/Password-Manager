import mysql.connector

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="lakshay24",
  )

mycursor = db_connection.cursor()

# Creating a database
mycursor.execute("CREATE DATABASE IF NOT EXISTS passwordManager")

print("Database created successfully!!")