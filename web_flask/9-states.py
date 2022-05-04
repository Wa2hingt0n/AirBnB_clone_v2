#!/usr/bin/python3
""" Starts a flask web application to list all state object database storage """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route("/states", strict_slashes=False)
def display_states():
    """ Displays an HTML page with a list of states present in DB storage """
    states = storage.all("State")
    return render_template("9-states.html",
                           states=states)


#@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def display_cities_of_state(id):
    """ Displays the cities associated with the state_id """
    states = storage.all("State")
    #if id is None:
        #return render_template("9-states.html",
                           #states=states)
    for state in states.values():
        if state.id == id:
            return render_template("9-states.html", state=state)
        else:
            return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
