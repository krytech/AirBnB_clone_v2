#!/usr/bin/python3
"""
Starts Flask web app
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(self):
    """Removes the current SQLAlchemy session"""
    storage.close()


@app.route('/states_list')
def html_states():
    """Displays html page for states"""
    return render_template('7-states_list.html', states=storage.all(State))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
