import os
from flask import Flask
from flask import Response
from flask import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route("/version")
def version():
    return "helloworld 1.0.0\n"

@app.route('/cities.json')
def cities():
    data = {"cities" : ["Amsterdam","Berlin","New York","San Francisco","Tokyo","London"]}
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')
