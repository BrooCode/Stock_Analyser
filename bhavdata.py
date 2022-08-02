from numpy import size
import cursor as connect

mydb,mycursor = connect.cursor()

def avg(stock_name,days,dict):
    if(size(dict[stock_name])<days):
        return 0
    else:
        return sum(dict[stock_name][-days:])/days

def calculate_avg():
    dict = {}
    mycursor.execute('''SELECT symbol,wap FROM stock_analysis WHERE "timestamp" IN (SELECT DISTINCT "timestamp" FROM stock_analysis WHERE symbol IN (SELECT DISTINCT  symbol FROM stock_analysis WHERE "timestamp" = '2018-04-20' ) ORDER BY "timestamp" DESC LIMIT 200) ''')

    stock_symbol = mycursor.fetchall()


    for con in stock_symbol:
        if con[0] not in dict:
            dict[con[0]] = []
        dict[con[0]].append((con[1]))

    avg_dict = {}
    days = [5,10,50,100]
    count = 0
    for con in stock_symbol:
        if con[0] not in avg_dict:
            avg_dict[con[0]] = []
        for i in range(len(days)):
            avg_dict[con[0]].append(avg(con[0],days[i],dict))
        count = count + 1
        if(count==5):
            break


    return avg_dict