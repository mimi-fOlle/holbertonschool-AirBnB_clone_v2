#!/usr/bin/python3
"""Module web_flask"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Starts a Flask web app and listening on 0.0.0.0, port 5000"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Bind to hbnb"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
