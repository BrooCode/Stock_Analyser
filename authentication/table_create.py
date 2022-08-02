import cursor as connect

mydb,mycursor = connect.cursor()


mycursor.execute("CREATE TABLE users (name VARCHAR(255), password VARCHAR(255), number VARCHAR(10))")

