import flask
import random
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)


@app.route("/data")
def data():
    val = random.random()
    print(f"Got a request, generating value {val}")
    return flask.jsonify({"value": val})


app.run()
