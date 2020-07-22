import requests
from dotenv import load_dotenv
import os
# class apicallstock ():
#     def __init__(self):
#        self.baseURL='https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=VEZL8KVEL60VMXTT'
#       #  self.baseURL='https://jsonplaceholder.typicode.com/todos/1'
def get_stock_data(stockname):

    
    load_dotenv()
    APIKEY=os.environ.get("APIKEY")
    
    URL='https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={Stockname}&interval=5min&apikey={APIKEY}'
    baseURL=URL.format(Stockname=stockname.upper(),APIKEY=APIKEY)
    print(baseURL)
    resp=requests.get(baseURL)
    if resp.status_code == 200 :
        
        data=resp.json()
      #  print (data)
        metadata=data['Meta Data']
        time=metadata['3. Last Refreshed']
        stockvallatest=data["Time Series (5min)"]  
        return stockvallatest,time
      #  print (stockvallatest[time]['1. open'])
        
        # print (resp.json())
    else:
        print('GET Stock Data',format(resp.status_code))
