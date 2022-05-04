#!/usr/bin/python3
""" Starts a flask web application to list all state object database storage """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def display_states_and_cities():
    """ Displays an HTML page with a list of states and associated cities """
    states = storage.all("State")
    cities = storage.all("City")
    return render_template("8-cities_by_states.html",
                           states=states, cities=cities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
