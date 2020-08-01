# stockchartpyqt5
This python program is used to create a frontend with PyQT5. Stock Fundamental data and daily stock prices of data is shown on the PYQT5 UI screen. A screen snapshot is attached . 

# stock.ui
I used Pyqt5 designer to include the labels and buttons. The program stock.ui is from QT5 designer app

# stock.py 
The stock.py program takes in the stock name as input and based on the stock name, the stockapi program is called to get the stock details from Alpha Vantage API. I chose Alpha Vantage API as it was free. 
The stock.py program gets the results from stockapi and the function insert_table and insert_fundamental_data is used to update the screen with the updated details

# stockapi.py
In the stockapi.py program, there are 2 API calls, one function is used to get fundametal stock details like Market Capitalisation and EPS. The other function is used to get the daily prices of the stock. 


 
![Screen Snapshot Stock Details](stock.png)