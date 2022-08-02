import cursor as connect

mydb,mycursor = connect.cursor()


def change_password(un,ps):

    query = "UPDATE users SET password = %s WHERE username = %s;"
    mycursor.execute(query, (ps, un))
    mydb.commit()
    return "Password Updated"

# change_password("rahul4758",4758)