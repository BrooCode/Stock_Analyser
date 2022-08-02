import cursor as connect

mydb,mycursor = connect.cursor()


def login(un,ps):

    query = "SELECT name FROM users WHERE username = %s AND password =  %s"
    mycursor.execute(query, (un, ps))
    user = mycursor.fetchone()

    if(user):
        return "Loged In"
    else:
        return "Either password or username is incorrect"

# print(login("rahul4758",12345))
