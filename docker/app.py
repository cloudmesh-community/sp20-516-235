from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/student/yasir')
def yasir_information():
    data = {
        'firstname': 'yasir',
        'lastname': 'Alibadi',
        'university': 'Indiana University',
        'email': 'yasir@example.com'
        }
    return jsonify(**data)
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=80)

