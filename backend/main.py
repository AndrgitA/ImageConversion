from flask import Flask, jsonify, request, redirect, url_for, render_template, send_from_directory
from flask_cors import CORS
import os

import json
from  src.modules.conversion import Conversion


conversion = Conversion()

#configuration
DEBUG = True
UPLOAD_FOLDER = './src/uploads/'
TEMPLATE_FOLDER = os.path.abspath('../frontend/dist/')
STATIC_FOLDER = os.path.abspath('../frontend/dist/')
ALLOWED_EXTENSIONS = set(['zip'])
HOST = "0.0.0.0"
PORT = 8888


#instance app
app = Flask(
    __name__,
    static_url_path = '',
    template_folder = TEMPLATE_FOLDER,
    static_folder = STATIC_FOLDER
)

app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#enable CORS
cors = CORS(app, resources = { r"/api/*": { "origins": "*" }})

def allowedFile(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploads/<path:filename>', methods=["GET"])
def uploads(filename):
    # send_from_directory('js', path)
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                                  filename, as_attachment=True)
    # return jsonify(file = filename)

@app.route('/api/upload', methods=["POST", "OPTIONS"])
def upload():
    if (request.method == "POST"):
        options = json.loads(request.form.get('options')) if request.form.get('options') is not None else []
        file = request.files['images']
        if (file and allowedFile(file.filename)):
            filename = file.filename
            result = conversion.run(file, options)
            if result is not None:
                return jsonify(result)
        return jsonify(success = False)

    elif (request.method == "OPTIONS"):
        return jsonify(success = True)


@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(
        debug = DEBUG,
        host = HOST,
        port = PORT
    )