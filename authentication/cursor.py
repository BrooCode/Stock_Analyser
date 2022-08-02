import mysql.connector

def cursor():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Origin19",
    database="authentication"
    )

    mycursor = mydb.cursor()
    return mydb,mycursor

