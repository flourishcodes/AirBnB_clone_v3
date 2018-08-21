#!/usr/bin/python3
"""Python api built with flask"""
from flask import Flask
import models
from models import storage
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slases = False


@app.teardown_appcontext
def tear_down(exception):
    """Calls storage close on appcontext"""
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    if host is None:
        host = '0.0.0.0'
    port = getenv('HBNB_API_PORT')
    if port is None:
        port = 5000
    app.run(host, int(port))
