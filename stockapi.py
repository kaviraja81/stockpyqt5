import requests
from dotenv import load_dotenv
import os
#### This program is used to make API calls to Alpha Vantage to get the daily prices and the fundamental summary
### get_fundamental_stockdata function is used to get summary of the fundamental details of the stock
### get_stock_data is the API call to get the daily prices of the stock 
class apicallstock ():
    def __init__(self):
      load_dotenv()
      self.APIKEY=os.environ.get("APIKEY")
      self.fundURL='https://www.alphavantage.co/query?function=OVERVIEW&symbol={stockname}&apikey={APIKEY}'
      self.dailyURL='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={Stockname}&apikey={APIKEY}'

    def get_fundamental_stockdata(self,stockname='IBM'):
      OverviewURL=self.fundURL.format(stockname=stockname.upper(),APIKEY=self.APIKEY)
      resp=requests.get(OverviewURL)
      if resp.status_code == 200 : 
        data=resp.json()
        return data
      else :
        print("Error returning data from API") 

    def get_stock_data(self,stockname='IBM'):

        DailyURL=self.dailyURL.format(Stockname=stockname.upper(),APIKEY=self.APIKEY)
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
