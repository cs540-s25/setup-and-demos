import flask
from nyt import get_headlines

app = flask.Flask(__name__)


@app.route("/")
def main():
    headlines = get_headlines("bananas")
    return flask.render_template("index.html", headlines=headlines)


app.run()
