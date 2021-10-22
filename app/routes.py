from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request


books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET", "POST"])
def handle_books():
    if request.method == "GET":
        books = Book.query.all()
        books_response = [{"id": book.id, "title": book.title, "description": book.description} for book in books]
        return jsonify(books_response)
    else:
        request_body = request.get_json()
        new_book = Book(title = request_body["title"], 
        description = request_body["description"])

        db.session.add(new_book)
        db.session.commit()

        return make_response(f"Book {new_book.title} successfully added!", 201)


@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    book_id = int(book_id)
    books = Book.query.all()
    for book in books:
        if book.id == book_id:
            response = {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
    return jsonify(response)

