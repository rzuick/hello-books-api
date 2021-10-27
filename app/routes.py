from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request


books_bp = Blueprint("books", __name__, url_prefix="/books")


@books_bp.route("", methods=["GET", "POST"])
def handle_books():
    
    if request.method == "GET":
        title_query = request.args.get("title")
        if title_query:
            books = Book.query.filter_by(title = title_query)
            books_response = [{"id": book.id, "title": book.title,
                            "description": book.description} for book in books]
            return jsonify(books_response)
        else:
            books = Book.query.all()
            books_response = [{"id": book.id, "title": book.title,
                            "description": book.description} for book in books]
            return jsonify(books_response), 200
    elif request.method == "POST":
        request_body = request.get_json()
        new_book = Book(title=request_body["title"],
                        description=request_body["description"])
        db.session.add(new_book)
        db.session.commit()
        return make_response(f"Book {new_book.title} successfully added!", 201)


@books_bp.route("/<book_id>", methods=["GET", "PUT", "PATCH", "DELETE"])
def handle_book(book_id):
    book_id = int(book_id)
    book = Book.query.get(book_id)
    if book == None:
        return make_response(f"Book #{book_id} does not exist", 404)
    if request.method == "GET":
        if book.id == book_id:
            response = {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
            return jsonify(response)
    elif request.method == "PUT":
        updated_request_body = request.get_json()
        book.title = updated_request_body["title"]
        book.description = updated_request_body["description"]
        db.session.commit()
        return make_response(f"{book.title} successfully updated", 200)
    elif request.method == "PATCH":
        updated_request_body = request.get_json()
        if "title" in updated_request_body:
            book.title = updated_request_body["title"]
            db.session.commit()
        if "description" in updated_request_body:
            book.description = updated_request_body["description"]
            db.session.commit()
        return jsonify(f"{book.title} successfully updated"), 200
    elif request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return make_response(f"{book.title} successfully deleted", 200)
# testing filter_by method from Flask


@books_bp.route("title/<title>", methods=["GET"])
def handle_book_title(title):
    title = str(title)
    book = Book.query.filter_by(title=title).first()
    if request.method == "GET":
        if book.title.lower() == title.lower():
            response = {
                "title": book.title,
                "id": book.id,
                "description": book.description
            }
        return jsonify(response)
