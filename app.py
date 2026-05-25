from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    password = os.environ.get('PASSWORD', '')
    return jsonify({"valid": data.get("password") == password})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
