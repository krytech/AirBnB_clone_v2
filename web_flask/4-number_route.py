#!/usr/bin/python3
"""
Starts Flask web app
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Displays text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Displays text"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Displays custom text"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """Displays custom text, with default value"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def text_int(n):
    """Displays text if int"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
