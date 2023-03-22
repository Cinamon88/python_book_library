from flask import render_template
from app import app
from app.models import Book

@app.route("/")
def index():
    all_books = Book.query.all()
    return render_template("homepage.html", all_books=all_books)