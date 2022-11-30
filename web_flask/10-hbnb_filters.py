#!/usr/bin/python3
"""Module web_flask"""
from flask import Flask, render_template, request
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
app = Flask(__name__)


"""Gets list of states"""
states = []
data = storage.all(State)
for key, value in data.items():
    states.append(value)

"""Gets list of cities"""
cities = []
data = storage.all(City)
for key, value in data.items():
    cities.append(value)

"""Gets list of amenities"""
amenities = []
data = storage.all(Amenity)
for key, value in data.items():
    amenities.append(value)


@app.route("/hbnb_filters")
def hbnb_filters():
    """Render filter"""
    return render_template("10-hbnb_filters.html", states=states,
                           cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
