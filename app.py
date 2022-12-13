from flask import Flask, request, redirect, jsonify, make_response
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
from translate import Translator
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    
    if request.method == "POST":
        print("FORM DATA RECEIVED")
    
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        
          
    return make_response(
        jsonify(
            {"ruword": 'прєвєт', "uaword": 'привіт' }
        ), 200
    )
        


if __name__ == '__main__':
    app.run(debug=True)