import json

class Book:
    def __init__(self, title, times_read=0):
        self.title = title
        self.times_read = times_read

    def mark_as_read(self):
        self.times_read += 1
        print(f"You have read {self.title} {self.times_read} time(s).")

    def to_dict(self):
        return {
            'title': self.title,
            'times read': self.times_read
        }

    @classmethod
    def from_dict(cls, data):
        return cls(title=data['title'], times_read=data['times read'])

class Shelf:
    def __init__(self):
        self.shelf = {}

    def save_shelf(self):
        """Save the shelf to a JSON file"""
        shelf_data = {title: book.to_dict() for title, book in self.shelf.items()}
        with open('shelf.json', 'w') as file:
            json.dump(shelf_data, file)
        print("Shelf saved to 'shelf.json'.")

    def load_shelf(self):
        """Load the shelf from a JSON file"""
        try:
            with open('shelf.json', 'r') as file:
                loaded_data = json.load(file)
            self.shelf = {
                title: Book.from_dict(book_data)
                for title, book_data in loaded_data.items()
            }
            print("Shelf loaded from 'shelf.json'.")
        except FileNotFoundError:
            print("No saved shelf found. Starting with an empty shelf.")
        except json.JSONDecodeError:
            print("Error reading shelf file. File might be corrupted.")

    def add_mark_read(self, title):
        if title not in self.shelf:
            self.shelf[title] = Book(title)
        self.shelf[title].mark_as_read()

    def display_shelf(self):
        if not self.shelf:
            print("Shelf is empty")
            return

        print("Shelf contents")
        for title, book in self.shelf.items():
            print("-", title, "read", book.times_read, "time(s)")

    def select_book_by_num(self):
        if not self.shelf:
            print("The shelf is empty")
            return

        titles = list(self.shelf.keys())
        print("Choose a book to mark as read")
        for index, title in enumerate(titles, start=1):
            print(index, title)

        try:
            selection = int(input("Enter the number assigned to the book: "))
            if 1 <= selection <= len(titles):
                chosen_title = titles[selection - 1]
                self.shelf[chosen_title].mark_as_read()
            else:
                print("Invalid number. Choose one from the list.")
        except ValueError:
            print("Invalid input. Enter a number.")

    def remove_book(self):
        titles = list(self.shelf.keys())
        if not titles:
            print("No books to remove.")
            return

        for index, title in enumerate(titles, start=1):
            print(index, title)

        try:
            choice = int(input('Which one do you want to remove? (choose by number): '))
            if 1 <= choice <= len(titles):
                key_to_delete = titles[choice - 1]
                del self.shelf[key_to_delete]
                print(f'"{key_to_delete}" has been removed.')
            else:
                print(f'ERROR: {choice} is not a valid selection!')
        except ValueError as e:
            print(f'Invalid input: {e}')

def main():
    shelf = Shelf()
    shelf.load_shelf()

    while True:
        print("\n=== My Book Shelf ===")
        print("1. Display shelf")
        print("2. Add or mark a book as read")
        print("3. Select book by number to mark as read")
        print("4. Remove book")
        print("5. Save and exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            shelf.display_shelf()
        elif choice == "2":
            title = input("Enter the book title: ").lower()
            shelf.add_mark_read(title)
        elif choice == "3":
            shelf.select_book_by_num()
        elif choice == "4":
            shelf.remove_book()
        elif choice == "5":
            shelf.save_shelf()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
