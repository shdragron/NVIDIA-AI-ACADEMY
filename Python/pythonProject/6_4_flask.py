# 6_4_flask.py

# 서버 종류: 운영서버,개발서버
# 운영서버: 실제 사용 서버
# 개발서버: 실제와 유사한 개발을 위한 서버

from random import random

import test

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "hello flask"

@app.route("/randoms")
def randoms():
    a = [random.randint(0,100) for i in range(100)]
    return a

if __name__ == "__main__":
    app.run(debug=True)

# print(__name__) # 유일한 이름





