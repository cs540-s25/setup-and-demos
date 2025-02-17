# Security problems abound in this app! Can you find them?

import flask
from flask_sqlalchemy import SQLAlchemy


app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    # this string will look different for you!
    # format is postgresql://user:password@localhost:port/db_name
    # you can run \conninfo in psql to find your values
    "postgresql://johnmartin:donotstealpls@localhost:5432/johnmartin"
)


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
    user = User.query.filter_by(username=username).filter_by(password=password)
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


app.run()
