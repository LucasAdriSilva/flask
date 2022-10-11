from flask import Flask, jsonify
import os

app = Flask(__name__)

if __name__ == '__main__':
    port = int(os.getenv('PORT'), '5000')
    app.run(host='0.0.0.0', port = port)


@app.route('/')
def index():
    return "Choo Choo": "Welcome to your Flask app 🚅"


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
