import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# msft = yf.Ticker("MSFT")
# ms = msft.info
# ms_history = msft.history(period='10d')

# symbol = ms['symbol']
# date = ms_history['Close'].index.values
# hvalue = ms_history['Close'].values

# for i in range(len(date)):
#     stock = {
#         'symbol' : symbol,
#         'date' : str(date[i])[0:10],
#         'value' : hvalue[i]
#     } 
#     db.stocks.insert_one(stock)
num = input()
name = yf.Ticker(num)
_name = name.info
_name_history = name.history(period='10d')

symbol = _name['symbol']
date = _name_history['Close'].index.values
hvalue = _name_history['Close'].values

for i in range(len(date)):
    stock = {
        'symbol' : symbol,
        'date' : str(date[i])[0:10],
        'value' : hvalue[i]
    } 
    db.stocks.insert_one(stock)

