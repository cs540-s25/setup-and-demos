import flask
import random

app = flask.Flask(__name__)


@app.route("/")
def foo():
    num = random.randint(0, 100)
    return flask.render_template("index.html", number=num)


@app.route("/bigger_numbers")
def bigger_numbers():
    num = random.randint(100, 1000000)
    return flask.render_template("index.html", number=num)


app.run(debug=True)
