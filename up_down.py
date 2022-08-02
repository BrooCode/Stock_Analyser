import cursor as connect

mydb,mycursor = connect.cursor()

def fun(symbol):
    mycursor.execute('''SELECT symbol,low,high FROM stock_analysis WHERE "timestamp" IN (SELECT DISTINCT "timestamp" FROM stock_analysis WHERE symbol IN (SELECT DISTINCT  symbol FROM stock_analysis WHERE "timestamp" = '2018-04-20' ) ORDER BY "timestamp" DESC LIMIT 10) ''')

    stock_symbol = mycursor.fetchall()

    low_high = {}

    h_max=0
    l_min=20110020
    print(stock_symbol[0])

    # low_high = ["last 10 days highest","last 10 days lowest"]

    for con in stock_symbol:
        if con[0] not in low_high:
            low_high[con[0]] = [0,0]
        low_high[con[0]][0]=(max(h_max,con[2]))
        low_high[con[0]][1]=(min(l_min,con[1]))


    mycursor.execute('''SELECT symbol,low,high FROM stock_analysis WHERE "timestamp" IN (SELECT DISTINCT "timestamp" FROM stock_analysis WHERE symbol IN (SELECT DISTINCT  symbol FROM stock_analysis WHERE "timestamp" = '2018-04-20' ) ORDER BY "timestamp" DESC LIMIT 1) ''')

    current = mycursor.fetchall()

    c_high=0
    c_low=0
    for con in current:
        if con[0]==symbol:
            c_high = con[2]
            c_low = con[1]
    print("chigh : " +str(c_high))
    print("clow : " +str(c_low))
    return low_high[symbol],c_high,c_low

print(fun('20MICRONS'))
