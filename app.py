from flask import Flask, request, jsonify
import os
import uuid
import time

app = Flask(__name__)

active_sessions = {}

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    password = os.environ.get('PASSWORD', '')
    if data.get("password") == password:
        token = str(uuid.uuid4())
        active_sessions[token] = time.time()
        return jsonify({"valid": True, "session": token})
    return jsonify({"valid": False})

@app.route('/ping', methods=['POST'])
def ping():
    data = request.json
    session = data.get("session")
    if session in active_sessions:
        active_sessions[session] = time.time()
        return jsonify({"valid": True})
    return jsonify({"valid": False})

@app.route('/renew', methods=['POST'])
def renew():
    password = os.environ.get('PASSWORD', '')
    if not password:
        return jsonify({"valid": False})
    new_token = str(uuid.uuid4())
    active_sessions[new_token] = time.time()
    return jsonify({"valid": True, "session": new_token})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
