#!/usr/bin/python3
"""
Simple module that starts a Flask web application
Starting to display formatted text and conditional message
Addind basic template
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    displays Hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    displays HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_mylove(text):
    """
    displays 'C' followed by the value of text variable
    """
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonista(text='is cool'):
    """
    displays 'Python ' followed by the value of text variable
    """
    return "Python " + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def is_num(n):
    """
    Displays message only if n is an integer
    """
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numbersandtemp(n):
    """
    Displays 5-number.html template
    only if n is an integer
    """
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    """ app listening on host 0.0.0.0 and port 5000 """
    app.run(host='0.0.0.0', port='5000')
