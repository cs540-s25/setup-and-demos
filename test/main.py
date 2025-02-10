import flask
from nyt import get_headlines
import os

app = flask.Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    if flask.request.method == "POST":
        query = flask.request.form.get("query", "bananas")
    else:
        query = "bananas"
    headlines = get_headlines(query)
    return flask.render_template("index.html", headlines=headlines, topic=query)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 8080))
