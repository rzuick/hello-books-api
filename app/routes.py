from flask import Blueprint, jsonify

hello_world_bp = Blueprint("hello, world", __name__)
books_bp = Blueprint("books", __name__, url_prefix="/books")
@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    my_beautiful_response_body = "Hello, World!"
    return 
    
@hello_world_bp.route("/hello/JSON", methods=["GET"])
def hello_json():
    my_response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    return my_response_body

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"] = new_hobby
    return response_body

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Enders Game", "A dystopian scifi and fantasy novel"),
    Book(2, "Children of Blood and Bone", "African fantasy that follows a female protagonist"),
    Book(3, "Wonder", "A book about how wonderful it is to be different")
]

@books_bp.route("", methods=["GET"])
def handle_books():
    pass
    books_response = []
    for book in books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    return jsonify(books_response)

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    book_id = int(book_id)
    for book in books:
        if book.id == book_id:
            response = {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
    return jsonify(response)