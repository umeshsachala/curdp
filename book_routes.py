from flask import Blueprint, request, jsonify
from models.book import books # type: ignore

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

@book_bp.route('', methods=['GET'])
def get_books():
    return jsonify(books)

@book_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None:
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

@book_bp.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_data = request.get_json()
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None:
        book.update(updated_data)
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

@book_bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'})
