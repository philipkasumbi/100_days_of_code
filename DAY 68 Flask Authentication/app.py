from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column



class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SECRET_KEY"] = "my-super-secret-key"
db.init_app(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

with app.app_context():
    db.create_all()

@app.route("/users")
def users():
    users = db.session.execute(
        db.select(User)
    ).scalars().all()

    for user in users:
        print(user.id, user.email, user.password)

    return "Check your terminal"

@app.route("/")
def authenticator():
    return render_template("authenticator.html")

# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        hashed_password = generate_password_hash(password)

        user = User(
            email=email,
            password=hashed_password
        )
        db.session.add(user)
        db.session.commit()

        return "Registration successful!"


    return render_template("register.html")

# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = db.session.execute(
            db.select(User).where(User.email == email)
        ).scalar()

        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            return redirect(url_for("secret"))

        return "Invalid email or password"

    return render_template("login.html")


@app.route("/secret")
def secret():

    if "user_id" not in session:
        return "You need to log in first."

    return render_template("secret.html")

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)