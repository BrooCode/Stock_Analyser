import cursor as connect

mydb,mycursor = connect.cursor()

def add_user(uname,name,password,mob_num):
    sql = "INSERT INTO users (username,name, password,number) VALUES (%s, %s,%s,%s)"
    val = (uname,name, password,mob_num)
    mycursor.execute(sql, val)
    mydb.commit()
    return "user_added"

# add_user("zaid123","Mohd Zaid",12345,7834916023)