from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    #form 데이터 읽어오기

    # title = request.form['title']
    # author = request.form['author']
    # review = request.form['review']

    #mongodb 저장하기
    # review_dict = {
    #     'title' : title,
    #     'author' : author,         
    #     'review' : review
    # }
    # db.reviews.insert_one(review_dict)

    #성공여부 반환하기
    return jsonify({'result':'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})


@app.route('/reviews', methods=['GET'])
def read_reviews():

    # stored_reviews = list(db.reviews.find())
    # reviews = []

    # for stored_review in stored_reviews:
    #     reviews.append({
    #         'title' : stored_review['title'],
    #         'author' : stored_review['author'],
    #         'review' : stored_review['review']
    #     })
    # print(reviews)

    return jsonify({'result':'success', 'reviews': reviews, 'msg' : '리뷰가 성공적으로 출력되었습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)