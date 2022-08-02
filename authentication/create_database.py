import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Origin19"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE authentication")