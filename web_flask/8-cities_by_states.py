#!/usr/bin/python3
"""
A script that starts a Flask web application
"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    display a HTML page: (inside the tag BODY)
    """
    states = storage.all("State")
    return render_template("8-states_list.html", states=states)

@app.teardown_appcontext
def teardown(exc):
    """
    Remove the current SQLAlchemy session
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")