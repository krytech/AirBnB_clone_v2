#!/usr/bin/python3
"""
Starts Flask web app
"""
from flask import Flask, render_template
from models import storage
from models import *

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
    """Displays text int"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def html_int(n):
    """Displays html page if number template used"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def html_even_odd(n):
    """Displays html page if template is used to check for odd or even"""
    check = "even" if (n % 2 == 0) else "odd"
    return render_template('6-number_odd_or_even.html',
                           n=n, check=check)


@app.teardown_appcontext
def tear_down(self):
    """Removes the current SQLAlchemy session"""
    storage.close()


@app.route('/states_list')
def html_states():
    """Displays html page for states"""
    states_all = [s for s in storage.all("State").values()]
    return render_template('7-states_list.html',
                           states_all=states_all)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
