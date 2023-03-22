from flask import render_template
from app import app
from app.models import Book

@app.route("/")
def index():
    all_books = Book.query.all()
    return render_template("homepage.html", all_books=all_books)

@app.route('/add', methods=['GET'])
def add():
    return render_template("add.html")