from symtable import Symbol
import cursor as connect

mydb,mycursor = connect.cursor()

dict = {}

# mycursor.execute("SELECT SYMBOL FROM stock_analysis WHERE DATE1>' 01-Jan-2020' && DATE1<' 05-Jan-2020';")
# stock_symbol = mycursor.fetchall()
# for i in stock_symbol:
#     dict[i[0]]=0

mycursor.execute("SELECT SYMBOL, AVG_PRICE FROM stock_analysis WHERE DATE1>'2020-01-01' && DATE1<'2020-01-05';")
sym_avg = mycursor.fetchall()

# count = 0
# for con in sym_avg:
#     count = count + 1
#     temp = dict[con[0]]
#     dict[con[0]]=(temp + con[1])/count

# print(dict)

