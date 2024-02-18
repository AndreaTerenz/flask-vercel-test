import time

import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return flask.render_template("index.html", funny=69, time=time.time())


if __name__ == '__main__':
    app.run()
