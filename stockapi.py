import requests
from dotenv import load_dotenv
import os
# class apicallstock ():
#     def __init__(self):
#        self.baseURL='https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=VEZL8KVEL60VMXTT'
#       #  self.baseURL='https://jsonplaceholder.typicode.com/todos/1'
def get_fundamental_stockdata(stockname='IBM'):
  URL='https://www.alphavantage.co/query?function=OVERVIEW&symbol={stockname}&apikey={APIKEY}'
  load_dotenv()
  APIKEY=os.environ.get("APIKEY")
  OverviewURL=URL.format(stockname=stockname.upper(),APIKEY=APIKEY)
  resp=requests.get(OverviewURL)
  if resp.status_code == 200 : 
    data=resp.json()
    # print (data)
    return data 

def get_stock_data(stockname='IBM'):

    
    load_dotenv()
    APIKEY=os.environ.get("APIKEY")
    
    URL='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={Stockname}&apikey={APIKEY}'
    DailyURL=URL.format(Stockname=stockname.upper(),APIKEY=APIKEY)
    resp=requests.get(DailyURL)
    if resp.status_code == 200 :
        
        data=resp.json()
        # print (data)
        metadata=data['Meta Data']
        time=metadata['3. Last Refreshed']
        stockvallatest=data["Time Series (Daily)"]  
        return stockvallatest,time
    else:
        print('GET Stock Data',format(resp.status_code))
