import cursor as connect

mydb,mycursor = connect.cursor()

def drop(table_name):
    query = "DROP TABLE "+str(table_name)
    mycursor.execute(query)

def show_all_tables(): #return list containing all tables
    mycursor.execute("SHOW tables")
    myresult = mycursor.fetchall()
    return myresult

def create_table():
    query = "CREATE TABLE users (username VARCHAR(255),name VARCHAR(255), password VARCHAR(255), number VARCHAR(10))"
    mycursor.execute(query)


def show():
    mycursor.execute("SELECT * FROM users") 
    myresult = mycursor.fetchall() #We use the fetchall() method, which fetches all rows from the last executed statement.
    return myresult

# create_table()
# drop("users")
print(show())