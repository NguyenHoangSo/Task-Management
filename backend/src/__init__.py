from flask import Flask  # type: ignore[import]

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
