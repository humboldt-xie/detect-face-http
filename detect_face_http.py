import detect
import json
from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('/tmp/tmp.jpg')
        bb=detect.face.detect('/tmp/tmp.jpg')
        return json.dumps(bb.tolist())
    return 'Hello, World!'

@app.route('/uploadStream', methods=['GET', 'POST'])
def upload_stream_file():
    if request.method == 'POST':
        f = request.files['file']
        bb=detect.face.detectStream(f.stream)
        return json.dumps(bb.tolist())
    return 'Hello, World!'

