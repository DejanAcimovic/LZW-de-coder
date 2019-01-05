from flask import Flask,request, render_template
from compress_logic import LZW
from decompress_logic import LZW_decoder

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/compress', methods=['GET', 'POST'])
def compress():
    content = request.json
    
    return LZW(content["text"])

@app.route('/decompress', methods=['GET', 'POST'])
def decompress():
    content = request.json
    
    return LZW_decoder(content["text"])


if __name__ == '__main__':
   app.run()
