#!/usr/bin/python3
"""Module web_flask"""
from flask import Flask, render_template, request
from models.state import State
from models.city import City
from models import storage
app = Flask(__name__)


@app.route("/states_list")
def states_list():
    states = []
    data = storage.all(State)
    for key, value in data.items():
        states.append(value)
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states")
def cities_by_states():
    states = []
    data = storage.all(State)
    for key, value in data.items():
        states.append(value)

    cities = []
    data = storage.all(City)
    for key, value in data.items():
        cities.append(value)
    return render_template("8-cities_by_states.html", states=states,
                           cities=cities)


@app.route("/states")
@app.route("/states/<id>")
def states_id(id=""):
    states = []
    data_s = storage.all(State)
    for key, value in data_s.items():
        states.append(value)
    if id:
        key = "State." + id
        if key not in data_s:
            states = ""

    cities = []
    data_c = storage.all(City)
    for key, value in data_c.items():
        cities.append(value)
    return render_template("9-states.html", id=id, states=states,
                           cities=cities)
    


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
