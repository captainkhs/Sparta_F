from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
   return  render_template('index.html')


@app.route('/mypage')
def mypage():  
   return 'This is My Page!'

@app.route('/test', methods=['GET']) #List임
def test_get():
    title = request.args['title_give'] # ==request.args.get('title_give')
    print(title)
    return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

@app.route('/test', methods=['POST'])
def test_post():
    title = request.form['title_give']
    print(title)
    return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)