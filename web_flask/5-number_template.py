#!/usr/bin/python3
"""
A script that starts a Flask web application
"""


from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_route():
    """
    display: 'Hello HBNB!'
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    display: 'HBNB'
    """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """
    display 'C' followed by the value of text
    """
    text = text.replace("_", " ")
    return "C {}".format(text)

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_fun(text="is cool"):
    """
    display 'Python' followed by the value of text
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    display 'n is a number'
    """
    return  "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    display a HTML page only if n is an integer
    """
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
