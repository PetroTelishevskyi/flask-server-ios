from flask import Flask, request, redirect, jsonify, make_response, url_for
from werkzeug.utils import secure_filename
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
from translate import Translator

UPLOAD_FOLDER = './flask server'
ALLOWED_EXTENSIONS = {'m4a'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
        
          
        
    return make_response(
            jsonify(
                        {"ruword": 'прєвєт', "uaword": 'привіт'}
                    ), 200
            )
        


if __name__ == '__main__':
    app.run(debug=True)