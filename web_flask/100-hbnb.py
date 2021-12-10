#!/usr/bin/python3
"""Starts a Flask app"""


if __name__ == '__main__':
    from flask import Flask, render_template
    from models import storage, State, Amenity, Place

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.route('/hbnb')
    def hbnb_filters():
        """
        sets the route for '/hbnb'
        """
        return render_template('100-hbnb.html',
                               states=storage.all(State),
                               a=storage.all(Amenity),
                               places=storage.all(Place))

    @app.teardown_appcontext
    def teardown(context):
        """resets storage after each request"""
        storage.close()

    app.run(host='0.0.0.0', port='5000')
