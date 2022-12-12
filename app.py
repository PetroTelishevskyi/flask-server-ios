import requests
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['POST'])
def getInfo():
    dataparser = request.get_data()


if __name__ == '__main__':
    app.run(debug=True)