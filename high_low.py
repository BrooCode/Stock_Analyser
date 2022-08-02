import cursor as connect

mydb,mycursor = connect.cursor()

dict = {}
mycursor.execute('''SELECT symbol,high,low FROM stock_analysis WHERE "timestamp" IN (SELECT DISTINCT "timestamp" FROM stock_analysis WHERE symbol IN (SELECT DISTINCT  symbol FROM stock_analysis WHERE "timestamp" = '2018-04-20' ) ORDER BY "timestamp" DESC LIMIT 30) ''')
stock_symbol = mycursor.fetchall()


for con in stock_symbol:
    if con[0] not in dict:
        dict[con[0]] = [0,282380]
    dict[con[0]][0]=max(dict[con[0]][0],con[1])
    dict[con[0]][1]=min(dict[con[0]][1],con[2])



def avg(stock_name):return dict[stock_name]

print(avg('ITC'))
