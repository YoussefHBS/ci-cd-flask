from flask import Flask

PORT = 8000

app = Flask(__name__)

@app.route('/')
def hello():
    return "Esto es un test"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
