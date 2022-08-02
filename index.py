import cursor as connect

mydb,mycursor = connect.cursor()

mycursor.execute("CREATE INDEX stock_date ON stock_Analysis (SYMBOL,DATE1)")
mydb.commit()
