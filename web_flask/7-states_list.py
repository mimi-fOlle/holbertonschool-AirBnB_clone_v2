#!/usr/bin/python3
"""Module web_flask"""
from flask import Flask, render_template, request
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    states= []
    data = storage.all()
    for key, value in data.items():
        states.append(value)
    return render_template("/7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
