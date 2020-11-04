from debt.dept_filter import fetchTargetDeptLsit
from flask import Flask
from flask import render_template

import sys
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/depts')
def filterDepts():
    deptList = fetchTargetDeptLsit();
    return 'Hello depts'

@app.route('/deptList')
def deptsPage():
    deptList = fetchTargetDeptLsit()
    return render_template('deptListPage.html',deptList=deptList)

if __name__ == '__main__':
    #http://119.45.213.124/
    #app.run(host="127.0.0.1", port=5000, debug=True)
    #10.36.208.222
    app.run(host="0.0.0.0", port=5000, debug=True)
