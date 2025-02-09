# Security problems abound in this app! Can you find them?

import flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://quickstart-user:alsodonotsteal@35.237.84.57/quickstart-db?unix_socket=/cloudsql/lecture-5-demo-redux:us-east1:quickstart-instance'
# app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://quickstart-user:alsodonotsteal@35.237.84.57/quickstart-db?host=/cloudsql/lecture-5-demo-redux:us-east1:quickstart-instance'
# app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://quickstart-user:alsodonotsteal/quickstart-instance?unix_socket=/cloudsql/lecture-5-demo-redux:us-east1:quickstart-instance'
# app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://quickstart-user:alsodonotsteal/quickstart-instance?unix_socket=/cloudsql/lecture-5-demo-redux:us-east1:quickstart-instance'


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(40))


class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(80))
    user_id = db.Column(db.Integer)  # foreign key, points to User table
    username = db.Column(db.String(80))
    password = db.Column(db.String(40))


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "POST":
        user = User.query.filter_by(username=flask.request.form["username"]).first()
        if user:
            print("Username already exists; not adding")
            pass  # this isn't great -- we should give some feedback to the user
        else:
            user = User(
                username=flask.request.form["username"],
                password=flask.request.form["password"],
            )
            db.session.add(user)
            db.session.commit()
            print(f"Created user {flask.request.form["username"]}")
    return flask.render_template("index.html")


# note the use of flask.redirect()! This will bounce the user to another page
@app.route("/login", methods=["POST"])
def login():
    data = flask.request.form
    username, password = data.get("username"), data.get("password")
    user = User.query.filter_by(username=username).filter_by(password=password).first()
    if user:
        # pass the username argument to the passwords URL
        return flask.redirect(flask.url_for("passwords", username=username))
    return flask.redirect(flask.url_for("index"))


@app.route("/passwords/<username>", methods=["GET", "POST"])
def passwords(username):
    if flask.request.method == "POST":
        user = User.query.filter_by(username=username).first()
        password = Password(
            user_id=user.id,
            username=flask.request.form.get("username"),
            service=flask.request.form.get("service"),
            password=flask.request.form.get("password"),
        )
        db.session.add(password)
        db.session.commit()

    passwords = Password.query.all()
    return flask.render_template(
        "passwords.html", username=username, passwords=passwords
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT", 8080))
