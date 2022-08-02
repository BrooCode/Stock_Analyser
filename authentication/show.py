import cursor as connect

mydb,mycursor = connect.cursor()


mycursor.execute("SELECT * FROM users") 

myresult = mycursor.fetchall() #We use the fetchall() method, which fetches all rows from the last executed statement.

for x in myresult:
  print(x)
