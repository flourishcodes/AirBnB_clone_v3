#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:     display "Hello nope!"
            /nope: display "nope"
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_nope():
    """display text"""
    return "Hello nope!"


@app.route('/nope')
def nope():
    """display text"""
    return "nope"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
