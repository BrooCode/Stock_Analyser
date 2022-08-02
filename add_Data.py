from cv2 import add
import cursor as connect
import csv
import pandas as pd
from datetime import datetime
import bhavdata as bhav

mydb,mycursor = connect.cursor()

def update_date(my_date):
    d = datetime.strptime(my_date, "%d-%b-%Y")
    return d.strftime("%Y-%m-%d")

def add_Data():
    data = pd.read_csv ('data-1658343111480.csv')
    df = pd.DataFrame(data)
    # print(df)

    for row in df.itertuples(index=False):
        # if row[13]==' -' or row[14]==' -':
        #     continue
        # if row[1]==' EQ':
        #     date = row[2]
        #     row[2] = update_date(date[1:])
        mycursor.execute('''INSERT INTO stock_Analysis("symbol","series","timestamp","open","high","low","close","prev_close","volume","val_inlakh","wap","total_trades","created_at") VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',  tuple(row[1:]))
        # break
        # mydb.commit()

    mydb.commit()

def add_avg_data():
    avg_dict = bhav.calculate_avg()
    mycursor.execute('''SELECT symbol FROM stock_analysis WHERE "timestamp" IN (SELECT DISTINCT "timestamp" FROM stock_analysis WHERE symbol IN (SELECT DISTINCT  symbol FROM stock_analysis WHERE "timestamp" = '2018-04-20' ) ORDER BY "timestamp" DESC LIMIT 200) ''')
    mycursor.execute('''INSERT INTO stock_avg_analysis(symbol,avg5,avg10,avg50,avg100,avg200) VALUES (%s,%s,%s,%s,%s,%s) ''',avg_dict)


