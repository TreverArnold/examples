from flask import Flask, request, abort, jsonify, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reverse', methods=['POST'])
def reverse():
    try:
        data = request.get_json()
        text = data['text']
        reversed_text = text[::-1]
        return jsonify({'reversed_text': reversed_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
