#!/usr/bin/python3
"""Starts a Flask app"""


if __name__ == '__main__':
    from flask import Flask, render_template
    from models import storage
    from models.state import State

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.route('/states')
    def states_list():
        """
        sets the route for '/states
        """
        return render_template('9-states.html',
                               states=storage.all(State))

    @app.route('/states/<id>')
    def state_cities(id=None):
        """sets the route for '/states/<id>"""
        return render_template('9-states.html',
                               state=storage.all(State).get(
                                   "State.{}".format(id)))

    @app.teardown_appcontext
    def teardown(context):
        """resets storage after each request"""
        storage.close()

    app.debug = True
    app.run(host='0.0.0.0', port='5000')
