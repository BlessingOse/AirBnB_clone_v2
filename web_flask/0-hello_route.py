#!/usr/bin/python3
"""Begins a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Shows 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Shows 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
