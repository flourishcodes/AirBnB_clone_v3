#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:              display "Hello nope!"
            /nope:          display "nope"
            /c/<text>:      display "C" + text (replace underscores with space)
            /python/<text>: display "Python" + text (default is "is cool")
            /number/<n>:    display "n is a number" only if int
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


@app.route('/c/<text>')
def c_text(text):
    """display custom text given"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """display custom text given
       first route statement ensures it works for:
          curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
          curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def text_if_int(n):
    """display text only if int given"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
