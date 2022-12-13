from flask import Flask, request, redirect, jsonify, make_response
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment
from translate import Translator
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    FRAME_RATE = 16000
    CHANNELS=1

    modelUa = Model(model_name="vosk-model-uk-v3")
    modelRu = Model(model_name="vosk-model-small-ru-0.22")
            # For a smaller download size, use model = Model(model_name="vosk-model-small-en-us-0.15")
    recUa = KaldiRecognizer(modelUa, FRAME_RATE)
    recRu = KaldiRecognizer(modelRu, FRAME_RATE)
    recUa.SetWords(True)
    recRu.SetWords(True)
    if request.method == "POST":
        print("FORM DATA RECEIVED")
    
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        
        if file:
            song = AudioSegment.from_file(file, format="mp4")
            song.export("filename.mp3", format="mp3")
            song = song.set_channels(CHANNELS)
            song = song.set_frame_rate(FRAME_RATE)

            recUa.AcceptWaveform(song.raw_data)
            resultUa = recUa.Result()
            recRu.AcceptWaveform(song.raw_data)
            resultRu = recRu.Result()
            textUa = json.loads(resultUa)
            textRu = json.loads(resultRu)

            tUA = textUa['result']
            tRU = textRu['result']

            arrRU = []
            translation = []
            translator= Translator(from_lang="ru",to_lang="uk")
            for i in range(len(text1['result'])):
                ttUa = tUA[i]
                ttRu = tRU[i]
                if ttUA['conf'] < ttRu['conf']:
                    arrRU.append(ttRu['word'])
                    translation.append(translator.translate(ttRu['word']))
    
    return make_response(
        jsonify(
            {"ruword": 'прєвєт', "uaword": 'привіт' }
        ), 200
    )
        


if __name__ == '__main__':
    app.run(debug=True)