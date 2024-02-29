from flask import (
            Flask,
                request,
                )

from calculator.calculator import Calculator

app = Flask(__name__)

@app.route('/api/add', methods=['POST'])
def add():
    return operation('add', 2)
app.run(host='0.0.0.0', port=8080)
