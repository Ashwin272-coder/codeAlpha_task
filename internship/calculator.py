from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Basic calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# API routes
@app.route('/api/add', methods=['GET'])
def api_add():
    try:
        # Ensure both x and y are provided and are valid numbers
        x = request.args.get('x')
        y = request.args.get('y')

        if x is None or y is None:
            return jsonify({"error": "Missing parameters x or y."}), 400

        x = float(x)
        y = float(y)

        result = add(x, y)
        return jsonify({"operation": "addition", "x": x, "y": y, "result": result})
    
    except (ValueError, TypeError) as e:
        return jsonify({"error": "Invalid input, please provide valid numbers for x and y."}), 400


@app.route('/api/subtract', methods=['GET'])
def api_subtract():
    try:
        x = request.args.get('x')
        y = request.args.get('y')

        if x is None or y is None:
            return jsonify({"error": "Missing parameters x or y."}), 400

        x = float(x)
        y = float(y)

        result = subtract(x, y)
        return jsonify({"operation": "subtraction", "x": x, "y": y, "result": result})
    
    except (ValueError, TypeError) as e:
        return jsonify({"error": "Invalid input, please provide valid numbers for x and y."}), 400


@app.route('/api/multiply', methods=['GET'])
def api_multiply():
    try:
        x = request.args.get('x')
        y = request.args.get('y')

        if x is None or y is None:
            return jsonify({"error": "Missing parameters x or y."}), 400

        x = float(x)
        y = float(y)

        result = multiply(x, y)
        return jsonify({"operation": "multiplication", "x": x, "y": y, "result": result})
    
    except (ValueError, TypeError) as e:
        return jsonify({"error": "Invalid input, please provide valid numbers for x and y."}), 400


@app.route('/api/divide', methods=['GET'])
def api_divide():
    try:
        x = request.args.get('x')
        y = request.args.get('y')

        if x is None or y is None:
            return jsonify({"error": "Missing parameters x or y."}), 400

        x = float(x)
        y = float(y)

        result = divide(x, y)
        return jsonify({"operation": "division", "x": x, "y": y, "result": result})
    
    except (ValueError, TypeError) as e:
        return jsonify({"error": "Invalid input, please provide valid numbers for x and y."}), 400

# Serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
