#!/usr/bin/python3
"""Starts a Flask app"""


from models import state


if __name__ == '__main__':
    from flask import Flask, render_template
    from models import storage
    from models.state import State

    app = Flask(__name__)
    app.url_map.strict_slashes = False

    @app.route('/states', strict_slashes=False)
    @app.route('/states/<id>', strict_slashes=False)
    def states(id=None):
        """
        sets the route for '/states
        """
        states = storage.all(State)
        if id:
            states = states.get("State.{}".format(id))
        return render_template('9-states.html', states=states)

    @app.teardown_appcontext
    def teardown(context):
        """resets storage after each request"""
        storage.close()

    app.run(host='0.0.0.0', port='5000')
