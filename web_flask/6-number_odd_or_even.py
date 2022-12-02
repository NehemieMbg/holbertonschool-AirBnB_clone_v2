#!/usr/bin/python3
"""Script that starts a Flask a web application."""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hello_hbnb():
    '''Display "Hello HBNB" '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    '''Display "HBNB" '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    '''Display "C following by the text'''
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    '''Display Python followed by a new line'''
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):
    '''Display number only if integer'''
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
    '''Display html page'''
def template_isInt(n):
    return render_templates('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
    '''Display html page'''
    num = 'odd' if n % 2 else 'even'
    return render_template("6-number_odd_or_even.html", number=n,
                           num=num)

if __name__ == '__main__':
    '''Listen to this port'''
    app.run(host='0.0.0.0', port=5000)
