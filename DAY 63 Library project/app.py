from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from flask_wtf import FlaskForm
from wtforms.fields.numeric import FloatField
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired,NumberRange

from dotenv import load_dotenv

import os
load_dotenv()

class MyForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = StringField('author', validators = [DataRequired()])
    rating = FloatField('rating', validators=[DataRequired(),NumberRange(1,10)])


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.__init__(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False,unique=True)
    author: Mapped[str] = mapped_column(nullable=False)
    rating : Mapped[float]

with app.app_context():
    db.create_all()

@app.route('/home')
def books():
    books = db.session.execute(db.select(Book)).scalars().all()
    return render_template("index.html",books=books)

@app.route('/home/create',methods=["POST","GET"])
def add_books():
    form = MyForm()

    if form.validate_on_submit():
        book = Book(
            title = form.title.data,
            author= form.author.data,
            rating = form.rating.data
        )
        db.session.add(book)
        db.session.commit()

        return redirect(url_for("books"))

    return render_template("add.html", form=form)

@app.route("/home/update/<int:id>" ,methods=["POST","GET"])
def edit_book(id):
    book = db.get_or_404(Book, id)
    form = MyForm(obj=book)

    if form.validate_on_submit():
        book.title = form.title.data
        book.author = form.author.data
        book.rating = form.rating.data

        db.session.commit()

        return redirect(url_for("books"))

    return render_template("edit.html", form=form, book=book)


@app.route("/home/delete/<int:id>" ,methods=["POST","GET"])
def delete_book(id):
    book = db.get_or_404(Book, id)

    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("books"))


if __name__ == "__main__":
    app.run(debug=True)
