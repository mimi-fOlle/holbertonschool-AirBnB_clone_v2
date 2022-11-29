#!/usr/bin/python3
"""Module web_flask"""
from flask import Flask, render_template, request
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    cities = list(storage.all(City).values())
    cities.sort(key=lambda city: city.name)
    return render_template("8-cities_by_states.html", cities=cities)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
