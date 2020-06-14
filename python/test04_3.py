from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
start_date = '2004-08-19'
end_date = '2020-04-17'
google_data = data.DataReader('GOOGL','yahoo', start_date, end_date)

print(google_data)
# print(google_data[0:1])
# print(googles.iloc[0].to_dict())
# for google in len(google_data):
#     print(google)
    
    # date = i['Date']
    # name = i['itemname']
    # value = i['nowVal']

    # stock = {
    #     'code' : code,
    #     'name' : name,
    #     'value' : value
    # }
    # db.stocks.insert_one(stock)  
    # print(stock)
    # print(code, name, value)

