
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

def getStarFromTitle(title):
    star = db.movies.find_one({'title':title})['star']
    return star

def getTitlesFromTitle(title):
    star = getStarFromTitle(title)
    movies = list(db.movies.find({'star':star}))
    title = []
    for movie in movies:
        title.append(movie['title'])
    return title

for title in getTitlesFromTitle('매트릭스'):
    print(title)