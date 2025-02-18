#!/usr/bin/python3
"""Starts a Flask app"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
@app.route('/airbnb-onepage/')
def hello():
    """
    sets the route for '/'
    """
    return "Hello HBNB!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
