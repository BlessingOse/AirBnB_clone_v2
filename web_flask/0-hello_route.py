#!/usr/bin/python3
<<<<<<< HEAD
"""Begins a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Prints 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Prints 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
=======
""" Script that runs app with Flask """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function """
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> ad52c21dc9c567524048e5ffe490c46ed7c5f132
