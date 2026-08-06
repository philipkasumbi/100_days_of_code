from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms.fields.simple import PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length

from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

class MyForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=8)])

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email)
        print(password)

        return f"<h1>Login successful</h1>"


    return render_template("login.html",form=form)


if __name__ == "__main__":
    app.run(debug=True)