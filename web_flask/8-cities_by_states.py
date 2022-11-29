#!/usr/bin/python3
"""Module web_flask"""
from flask import Flask, render_template, request
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


#@app.route("/cities_by_states")
#def states_template():
#    states = list(storage.all(State).values())
#    states.sort(key=lambda state: state.name)
#    return render_template("8-cities_by_states.html", states=states)

@app.route('/states_list')
def states_list():
    '''Render states list'''
    # Get list of states
    states = []
    data = storage.all(State)
    for key, value in data.items():
        states.append(value)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_state():
    '''Render cities by state list'''
    # Get list of states
    states = []
    data = storage.all(State)
    for key, value in data.items():
        states.append(value)

    # Get list of cities
    cities = []
    data = storage.all(City)
    for key, value in data.items():
        cities.append(value)
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)

@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000, debug=True)
