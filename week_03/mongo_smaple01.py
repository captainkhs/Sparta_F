from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta 

# all_users = list(db.users.find())
# print(all_users)

condition_uses = list(db.users.find({'age':21}))
print(condition_uses)
print(condition_uses[0])
print(condition_uses[0]['name'])


db.users.delete_one({'name':'bobby'})