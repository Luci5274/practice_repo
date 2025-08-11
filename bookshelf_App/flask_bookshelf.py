"""
Flask Bookshelf App
-------------------
This web application allows users to manage a personal bookshelf stored in a JSON file.
Users can:
    - View all books and their read counts.
    - Add a new book or increase the read count of an existing book.
    - Mark a book as read (incrementing its read count).
    - Delete a book from the list.
    - Save the current list of books to a JSON file for persistence.

The app uses:
    - Flask for routing and HTML rendering.
    - JSON for persistent storage of the bookshelf.
    - A simple HTML template (index.html) to display and interact with the data.

The server must be running for the application to function, and books.json
will be created automatically upon saving if it does not exist.
"""

import os
import json
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

app = Flask(__name__)


# Load books from JSON file
def load_books():
    """
    Load books from the JSON file if it exists.

    Returns:
        list: A list of book dictionaries in the format:
              [{'title': str, 'times_read': int}, ...]
              If the file doesn't exist, returns an empty list.
    """
    if os.path.exists("books.json"):
        with open("books.json", "r") as file:
            return json.load(file)  # Convert JSON -> Python list
    return []  # If file doesn't exist, start with empty list


# Save books to JSON file
def save_books(books_list):
    """
    Save the provided list of books to the JSON file.

    Args:
        books_list (list): A list of book dictionaries to save.
                           Each book should be in the format:
                           {'title': str, 'times_read': int}
    """
    with open("books.json", "w") as file:
        json.dump(books_list, file, indent=4)  # Pretty print for readability


books = load_books()


@app.route('/')
def index():
    """
    Render the homepage with the list of books.

    Returns:
        str: HTML content for the homepage.
    """
    return render_template('index.html', books=books)


@app.route('/add_book', methods=["POST"])
def add_book():
    """
    Add a new book or increment the read count of an existing book.

    Process:
        - If the submitted title already exists (case-insensitive),
          increment its 'times_read' value by 1.
        - Otherwise, add a new book entry starting with 'times_read' = 1.

    Redirects:
        - Redirects to the homepage after processing.
    """
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
    """
    Increment the 'times_read' value for the specified book.

    Process:
        - Matches the title in a case-insensitive way.
        - If found, increments the book's read count by 1.

    Redirects:
        - Redirects to the homepage after processing.
    """
    book_title_input = request.form['title']
    normalized_title = book_title_input.strip().lower()

    for book in books:
        if book['title'].lower() == normalized_title:
            book['times_read'] += 1
            break

    return redirect('/')


@app.route('/delete_book', methods=["POST"])
def delete_book():
    """
    Remove a book from the list.

    Process:
        - Matches the title in a case-insensitive way.
        - Deletes the first match found.

    Redirects:
        - Redirects to the homepage after deletion.
    """
    book_title_input = request.form['title']
    normalized_title = book_title_input.strip().lower()

    for i, book in enumerate(books):
        if book['title'].lower() == normalized_title:
            del books[i]
            break

    return redirect('/')

@app.route('/edit_book', methods=['POST'])
def edit_book():
    old_title = request.form.get('old_title')
    new_title = request.form.get('new_title').strip()

    normalized_old_title = old_title.strip().lower()

    if not new_title:
        return redirect('/')

    for book in books:
        if book['title'].lower() == normalized_old_title:
            book['title'] = new_title
            break

    return redirect('/')


@app.route('/save', methods=['POST'])
def save():
    """
    Save the current list of books to the JSON file.

    Redirects:
        - Redirects to the homepage after saving.
    """
    save_books(books)
    print('Save Successful!')
    return redirect('/')




if __name__ == '__main__':
    app.run(debug=True)
