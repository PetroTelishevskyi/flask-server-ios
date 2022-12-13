from flask import Flask, request, redirect, jsonify, make_response
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
from translate import Translator

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return {'success': False, 'reason': 'No file'}

        file = request.files["file"]
        if file.filename == "":
            return {'success': False, 'reason': 'Empty filename'}

        return {'success': True, 'file': file.filename}

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)