import cursor as connect

mydb,mycursor = connect.cursor()

dict = {}
mycursor.execute('''SELECT symbol,high,low FROM stock_analysis WHERE "timestamp" IN (SELECT DISTINCT "timestamp" FROM stock_analysis WHERE symbol IN (SELECT DISTINCT  symbol FROM stock_analysis WHERE "timestamp" = '2018-04-20' ) ORDER BY "timestamp" DESC LIMIT 2) ''')
stock_symbol = mycursor.fetchall()

sum = 0

for con in stock_symbol:
    if con[0] not in dict:
        dict[con[0]] = []
    dict[con[0]].append(con[1])
    dict[con[0]].append(con[2])


for con in stock_symbol:
    try:
        sum = sum + (dict[con[0]][0] -  dict[con[0]][3])
    except:
        print(dict[con[0]])
        continue


