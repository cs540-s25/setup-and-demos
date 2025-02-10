# Security problems abound in this app! Can you find them?

import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, LoginManager, UserMixin, login_user
from flask_login.utils import login_required
from flask_bcrypt import Bcrypt


app = flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    # this string will look different for you!
    # format is postgresql://user:password@localhost:port/db_name
    # you can run \conninfo in psql to find your values
    "postgresql://quickstart-user:alsodonotsteal@35.237.84.57/quickstart-db?host=/cloudsql/lecture-5-demo-redux:us-east1:quickstart-instance"
)
app.secret_key = "I am a secret key!"
bcrypt = Bcrypt(app)


db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(120))
    date_registered = db.Column(db.Integer())


class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service = db.Column(db.String(80))
    user_id = db.Column(db.Integer)  # foreign key, points to User table
    username = db.Column(db.String(80))
    password = db.Column(db.String(40))


with app.app_context():
    db.create_all()


login_manager = LoginManager()
# login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_name):
    return User.query.get(user_name)


@app.route("/", methods=["GET", "POST"])
def index():
    if flask.request.method == "POST":
        user = User.query.filter_by(username=flask.request.form["username"]).first()
        if user:
            print("Username already exists; not adding")
            pass  # this isn't great -- we should give some feedback to the user
        else:
            pw_hash = bcrypt.generate_password_hash(
                flask.request.form["password"]
            ).decode("utf-8")
            user = User(
                username=flask.request.form["username"],
                password=pw_hash,
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
    user = User.query.filter_by(username=username).first()
    if bcrypt.check_password_hash(user.password, password):
        # pass the username argument to the passwords URL
        login_user(user)
        return flask.redirect(flask.url_for("passwords"))
    return flask.redirect(flask.url_for("index"))


@app.route("/passwords", methods=["GET", "POST"])
@login_required
def passwords():
    user = current_user
    if flask.request.method == "POST":
        password = Password(
            user_id=user.id,
            username=flask.request.form.get("username"),
            service=flask.request.form.get("service"),
            password=flask.request.form.get("password"),
        )
        db.session.add(password)
        db.session.commit()

    passwords = Password.query.filter_by(user_id=user.id).all()
    return flask.render_template(
        "passwords.html", username=user.username, passwords=passwords
    )


app.run()
