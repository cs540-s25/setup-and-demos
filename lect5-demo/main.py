import flask
from flask import request
from nyt import get_headlines
import os

app = flask.Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def main():
    query = "deepseek"  # default
    if request.method == "POST":
        query = request.form.get("query", "deepseek")

    headlines = get_headlines(query)
    return flask.render_template("index.html", headlines=headlines, topic=query)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
