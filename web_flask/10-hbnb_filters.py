#!/usr/bin/python3
"""
Starts Flask web app
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(self):
    """Removes the current SQLAlchemy session"""
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    """Displays html page with city/state filters"""
    return render_template('10-hbnb_filters.html',
                           state_list=storage.all(State),
                           amenities=storage.all(Amenity))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
