from flask import (
    Flask,
    request,
)
import logging  # Add this import


from calculator.calculator import Calculator

app = Flask(__name__)
logger = logging.getLogger(__name__)



@app.route('/api/add', methods=['POST'])
def add():
    if not request.is_json:
        logger.error("Request is not JSON")
        return "Request must be JSON", 400
    
    if 'x' not in request.json or 'y' not in request.json:
        logger.error(f"Missing required fields. Received: {request.json}")
        return "Missing required fields x or y", 400

    logger.info(f"Received request with data: {request.json}")

    logger.log(logging.INFO, "Starting add operation")
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
        logger.log(logging.INFO, f"Factor 1: {factors[0]}")
        factors.append(float(request.json.get('y')))
        logger.log(logging.INFO, f"Factor 2: {factors[1]}")

    logger.log(logging.INFO, getattr(Calculator, method)(*factors))
    return str(getattr(Calculator, method)(*factors))


app.run(host='0.0.0.0', port=8080)