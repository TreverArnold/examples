from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/404")
def get_aborted():
    abort(404)

@app.route("/add")
def multiply_numbers():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)

    if num1 is not None and num2 is not None:
        result = num1 + num2
        return str(result)
    else:
        return "Invalid input, both numg and numh should be provided as query parameters."

@app.route("/reverse")
def reverse_text():
    txt = request.args.get('txt')
    if txt is not None:
        reversed_txt = txt[::-1]
        return reversed_txt
    else:
        return "Please provide a 'txt' parameter."
