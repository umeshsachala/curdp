from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
books = []

# Create
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

# Read
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):      
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None:
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Update
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_data = request.get_json()
    book = next((book for book in books if book['id'] == book_id), None)
    if book is not None:
        book.update(updated_data)
        return jsonify(book)
    return jsonify({'message': 'Book not found'}), 404

# Delete
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)
