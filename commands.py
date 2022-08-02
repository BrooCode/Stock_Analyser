import cursor as connect
import pandas as pd

mydb,mycursor = connect.cursor()

def drop(table_name):
    query = "DROP TABLE "+str(table_name)
    mycursor.execute(query)


def show_all_tables(): #return list containing all tables
    mycursor.execute("SHOW tables")
    myresult = mycursor.fetchall()
    return myresult

def create_table(query):
    mycursor.execute(query)

def alter_datatype():
    mycursor.execute("ALTER TABLE stock_analysis MODIFY COLUMN DATE1 VARCHAR(20);")
    mydb.commit()


def show():
    mycursor.execute("SELECT * FROM stock_analysis") 
    myresult = mycursor.fetchall() #We use the fetchall() method, which fetches all rows from the last executed statement.
    return myresult

def describe(table_name):
    query = "DESC "+str(table_name)
    mycursor.execute(query)
    indexList = mycursor.fetchall()
    print(indexList)

def delete_all():
    mycursor.execute("DELETE FROM stock_analysis")
    mydb.commit()


query = """CREATE TABLE stock_analysis (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(50),
    series varchar(20),
    "timestamp" DATE,
    "open" NUMERIC,
    high NUMERIC,
    low NUMERIC,
    "close" NUMERIC,
    prev_close NUMERIC,
    volume NUMERIC,
    val_inlakh NUMERIC,
    wap NUMERIC,
    total_trades NUMERIC,
    created_at DATE

);"""


# print(show_all_tables())
# create_table(query)
# describe("stock_analysis")
# drop("stock_analysis")
print((show()))
# delete_all()
# alter_datatype()

# df = pd.DataFrame(show())
# df.to_csv('bhavdata-01012020-15072022.csv')

