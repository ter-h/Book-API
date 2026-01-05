from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.schemas import BookSchema, BookCreateSchema
from app.services.book_service import BookService


book_bp = Blueprint("books", __name__)

book_schema = BookSchema()
books_schema = BookSchema(many=True)
create_schema = BookCreateSchema()

@book_bp.route("/", methods=["POST"])
def create_book():
    try:
        data = create_schema.load(request.get_json())
        book = BookService.create_book(data)
        return jsonify(book_schema.dump(book)), 201
    except ValidationError as e:
        return {"errors": e.messages},  400
    
@book_bp.route("/", methods=["GET"])
def list_books():
    books = BookService.list_books()
    return jsonify(books_schema.dump(books))

@book_bp.route("/<int:book_id>")
def get_book(book_id):
    book = BookService.get_book(book_id)
    return jsonify(book_schema.dump(book))

@book_bp.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = BookService.delete_book(book_id)
    return jsonify(book_schema.dump(book))