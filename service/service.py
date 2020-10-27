from flask import Flask

import sys
from hello_python.dept import *

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/depts')
def filterDepts():
    debt.dept_filter

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)