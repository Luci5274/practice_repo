from flask import Flask, render_template, request
from werkzeug.utils import redirect
import json
import os

app = Flask(__name__)


# Load books from JSON file
def load_books():
    """Read books from books.json if it exists, otherwise return an empty list."""
    if os.path.exists("books.json"):
        with open("books.json", "r") as file:
            return json.load(file)  # Convert JSON -> Python list
    return []  # If file doesn't exist, start with empty list


# Save books to JSON file
def save_books(books_list):
    """Write the current books list to books.json."""
    with open("books.json", "w") as file:
        json.dump(books_list, file, indent=4)  # Pretty print for readability

books = load_books()

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add_book', methods=["POST"])
def add_book():
    book_title = request.form['title']
    true_title = book_title.strip().lower()
    for book in books:
        if book['title'].lower() == true_title:
            book['times_read'] += 1
            break
    else:
        books.append({
            'title': book_title.strip(),
            'times_read': 1
        })
    return redirect('/')

@app.route('/mark_read', methods=["POST"])
def mark_read():
    book_title_input = request.form['title']
    normalized_title = book_title_input.strip().lower()

    for book in books:
        if book['title'].lower() == normalized_title:
            book['times_read'] += 1
            break

    return redirect('/')

@app.route('/delete_book', methods=["POST"])
def delete_book():
    book_title_input = request.form['title']
    normalized_title = book_title_input.strip().lower()

    for i, book in enumerate(books):
        if book['title'].lower() == normalized_title:
            del books[i]
            break

    return redirect('/')

@app.route('/save',methods=['POST'])
def save():
    save_books(books)
    print('Save Successful!')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
