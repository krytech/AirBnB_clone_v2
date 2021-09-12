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


@app.route('/states')
def states():
    """Displays html page for states"""
    return render_template('9-states.html', state_list=storage.all(State))


@app.route('/states/<id>')
def states_ids(id):
    """Displays html for states and id"""
    try:
        state = storage.all()["State.{}".format(id)]
        return render_template('9-states.html', state=state)
    except KeyError:
        return render_template('9-states.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
