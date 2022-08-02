import os
from datetime import date, timedelta
import requests
import add_Data as insert

def download(url):
    try:
        response = requests.get(url, timeout=5)
        with open('bhavdata.csv', 'wb') as f:
            f.write(response.content)
        return 1
    except :
        return 0


# download("https://archives.nseindia.com/products/content/sec_bhavdata_full_01012020.csv")

start_date = date(2022, 6, 1) 
end_date = date(2022, 7, 15)

delta = end_date - start_date

for i in range(delta.days + 1):
    day = str(start_date + timedelta(days=i))
    date = day
    day=day.replace("-","")
    f=day[6:8]+day[4:6]+day[0:4]
    url = "https://archives.nseindia.com/products/content/sec_bhavdata_full_" + str(f) + ".csv"
    flag = download(url)
    if flag==1:
        insert.add_Data()
        print("Data downloaded for Date : " +str(date))
    else:
        print("Data not available for Date : " +str(date))

