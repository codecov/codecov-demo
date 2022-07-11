'''
CODE-TESTING NOTES

1. TEST ADDITION  (adds 1 & 2 for result 3):
WINDOWS: curl -d "{\"x\": 1, \"y\": 2}" -H "Content-Type: application/json" http://localhost:8080/api/add
LINUX: curl -d '{"x": 1, "y": 2}' -H 'Content-Type: application/json' http://localhost:8080/api/add

2. RUN TESTS:
WINDOWS: python -m pytest
LINUX: pytest

3. CHECK COVERAGE
$ coverage run my_program.py arg1 arg2 (run without args to specify one file, e.g., calculator.py only
$ coverage report -m ; shows the following:

Name            Stmts   Miss  Cover   Missing
---------------------------------------------
app.py             22     16    27%   29, 33, 37, 39-46, 49-58
calculator.py      11      6    45%   3, 6, 9, 12-14
---------------------------------------------
TOTAL              33     22    33%

4.CREATE HTML REPORT

coverage html -d coverage_html
'''

from flask import (
    Flask,
    request,
)

from calculator import Calculator

app = Flask(__name__)

@app.route('/api/add', methods=['POST'])
def add():
    return operation('add', 2)

@app.route('/api/subtract', methods=['POST'])
def subtract():
    return operation('subtract', 2)

@app.route('/api/multiply', methods=['POST'])
def multiply():
    return operation('multiply', 2)

@app.route('/api/divide', methods=['POST'])
def divide():
    return operation('divide', 2)

def operation(method, num_factors):
    factors = []
    if num_factors == 2:
        factors.append(float(request.json.get('x')))
        factors.append(float(request.json.get('y')))

    return str(getattr(Calculator, method)(*factors))


app.run(host='0.0.0.0', port=8080)
