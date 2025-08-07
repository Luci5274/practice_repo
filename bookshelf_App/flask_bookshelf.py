from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(__name__)

books = [
    {"title": "Dune", "times_read": 3},
]

@app.route('/')
def index():
    return render_template('index.html',books=books)

@app.route('/add_book',methods=["POST"])
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
                'times_read' : 1
            })


    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)