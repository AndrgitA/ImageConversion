from flask import Flask, jsonify, request, redirect, url_for
from flask_cors import CORS
import os

from  src.modules.conversion import Conversion


conversion = Conversion()

#configuration
DEBUG = True
UPLOAD_FOLDER = './src/uploads/'
ALLOWED_EXTENSIONS = set(['zip'])
HOST = "0.0.0.0"
PORT = 8888

#instance app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#enable CORS
cors = CORS(app, resources = { r"/api/*": { "origins": "*" }})

def allowedFile(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=["GET"])
def index():
    return jsonify(hello = "world")

@app.route('/api/upload', methods=['POST', 'OPTIONS'])
def upload():
    if (request.method == "POST"):
        print(request)
        file = request.files['images']
        if (file and allowedFile(file.filename)):
            filename = file.filename
            options = {}
            result = conversion.run(file, options)
            if result is not None:
                return jsonify(result)
        return jsonify(success = False)

    elif (request.method == "OPTIONS"):
        return jsonify(success = True)

if __name__ == '__main__':
    app.run(debug = DEBUG, host = HOST, port = PORT)