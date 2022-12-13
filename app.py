from flask import Flask, request, redirect

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
        
    
    return 'OK'
        


if __name__ == '__main__':
    app.run(debug=True)