from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from flask_wtf import FlaskForm
from wtforms.fields.numeric import FloatField
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired,NumberRange
from sqlalchemy.exc import IntegrityError

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

@app.errorhandler(404)
def not_found(error):
    return {
        "error": {
            "code": "RESOURCE_NOT_FOUND",
            "message": "The requested resource was not found"
        }
    }, 404


@app.errorhandler(405)
def method_not_allowed(error):
    return {
        "error": {
            "code": "METHOD_NOT_ALLOWED",
            "message": "The HTTP method is not allowed for this endpoint"
        }
    }, 405


@app.errorhandler(IntegrityError)
def handle_integrity_error(error):
    db.session.rollback()

    return {
        "error": "A database constraint was violated"
    }, 409

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

# API METHODS

# GET METHOD
@app.route("/api/books", methods=["GET"])
def get_books():

    author = request.args.get("author")

    query = db.select(Book)

    if author:
        query = query.where(Book.author == author)

    books = db.session.execute(query).scalars().all()

    return [
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "rating": book.rating
        }
        for book in books
    ]

# POST METHOD
@app.route("/api/books", methods=["POST"])
def create_book():
    data = request.get_json()

    if not data:
        return {"error": "Request body is required"}, 400

    if "title" not in data:
        return {
            "error": {
                "code": "MISSING_TITLE",
                "message": "Title is required"
            }
        }, 400

    if "author" not in data:
        return {
            "error": {
                "code": "MISSING_AUTHOR",
                "message": "Author is required"
            }
        }, 400

    if "rating" not in data:
        return {
            "error": {
                "code": "MISSING_RATING",
                "message": "Rating is required"
            }
        }, 400

    if not 1 <= data["rating"] <= 10:
        return {
            "error": {
                "code": "INVALID_RATING",
                "message": "Rating must be between 1 and 10"
            }
        }, 400

    book = Book(
        title=data["title"],
        author=data["author"],
        rating=data["rating"]
    )

    db.session.add(book)
    db.session.commit()

    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "rating": book.rating
    }, 201

# PATCH METHOD
@app.route("/api/books/<int:book_id>", methods=["PATCH"])
def update_book(book_id):
    book = db.get_or_404(Book, book_id)

    data = request.get_json()

    if not data:
        return {"error": "Request body is required"}, 400

    if "title" in data:
        book.title = data["title"]

    if "author" in data:
        book.author = data["author"]

    if "rating" in data:
        if not 1 <= data["rating"] <= 10:
            return {"error": "Rating must be between 1 and 10"}, 400

        book.rating = data["rating"]

    db.session.commit()

    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "rating": book.rating
    }


# PUT METHOD
@app.route("/api/books/<int:book_id>", methods=["PUT"])
def replace_book(book_id):
    book = db.get_or_404(Book, book_id)

    data = request.get_json()

    if not data:
        return {
            "error": {
                "code": "EMPTY_REQUEST",
                "message": "Request body is required"
            }
        }, 400

    if "title" not in data:
        return {
            "error": {
                "code": "MISSING_TITLE",
                "message": "Title is required"
            }
        }, 400

    if "author" not in data:
        return {
            "error": {
                "code": "MISSING_AUTHOR",
                "message": "Author is required"
            }
        }, 400

    if "rating" not in data:
        return {
            "error": {
                "code": "MISSING_RATING",
                "message": "Rating is required"
            }
        }, 400

    if not 1 <= data["rating"] <= 10:
        return {
            "error": {
                "code": "INVALID_RATING",
                "message": "Rating must be between 1 and 10"
            }
        }, 400

    book.title = data["title"]
    book.author = data["author"]
    book.rating = data["rating"]

    db.session.commit()

    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "rating": book.rating
    }


# DELETE METHOD
@app.route("/api/books/<int:book_id>", methods=["DELETE"])
def delete_book_api(book_id):
    book = db.get_or_404(Book, book_id)

    db.session.delete(book)
    db.session.commit()

    return "", 204



if __name__ == "__main__":
    app.run(debug=True)
