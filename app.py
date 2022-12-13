from flask import Flask, request, redirect, jsonify, make_response
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
from translate import Translator
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        print('post request received')
        file = request.files['file']
        if file and allowed_file(file.filename):
            print('file name is valid and saving')
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({'success': 1})
        else:
            print('file failed to save')
            return jsonify({'success': 2})
        

def allowed_file(filename):
    print('in allowed_file')
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config['AllOWED_EXTENSIONS']

#Config settings
UPLOAD_FOLDER = './Users/User/Desktop/flask server'
ALLOWED_EXTENSIONS = set(['m4a'])       

if __name__ == '__main__':
    app.run(debug=True)