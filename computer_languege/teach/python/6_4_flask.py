# 6_4_flask.py
from flask import Flask, render_template
import random


app = Flask(__name__)

# static, templates

# https://www.google.com/
# https://www.google.com/search   ?   q=python
@app.route("/")
def index():
    return "hello, flask!!"


@app.route("/randoms")
def randoms():
    a = [random.randrange(100) for _ in range(10)]
    return str(a)


@app.route("/html")
def html():
    lotto = [random.randrange(45) + 1 for _ in range(6)]
    return render_template("sample.html", numbers=lotto)


if __name__ == '__main__':
    app.run(debug=True)






