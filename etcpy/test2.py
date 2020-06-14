import requests 
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

r = requests.get('https://finance.naver.com/api/sise/etfItemList.nhn')
rjson = r.json()

stocks = rjson['result']['etfItemList']
for i in stocks:
    code = i['itemcode']
    name = i['itemname']
    value = i['nowVal']

    stock = {
        'code' : code,
        'name' : name,
        'value' : value
    }
    db.stocks.insert_one(stock)  
    print(stock)
    print(code, name, value)











# if name == inputname :
#     print('code : %s name : %s value : %d' %(code, name, value))
# else:
# #     print('sorry')
# for etf in range(len(stocks)):
#     etf_name = etf['itemname']
#     etf_code = etf['itemcode']
#     etf_val = etf['nowVal']    

# if num == stock['name'] :
#     print(stock)
# else:
#     print('입력한 종목이 없습니다.')
    # if num == etf_name:
    #     print('code : %s name : %s value : %d' %(etf_code, etf_name,etf_val))
    # else:
    #     print('입력이 잘못 되었습니다.')
    #     break

# for i in range(len(stocks)):
#     stock = {
#         'code' : etf_code[i],
#         'name' : etf_name[i],
#         'value' : etf_val[i]
#     } 
    # db.stocks.insert_one(stock)
