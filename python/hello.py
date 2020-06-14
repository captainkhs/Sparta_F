from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

db.users.insert_one({'name':'hyun'},{'age':44})
db.users.insert_one({'name':'jone'},{'age':9})
db.users.insert_one({'name':'sone'},{'age':7})




