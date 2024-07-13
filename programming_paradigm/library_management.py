class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initially, the book is available
    
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successful checkout
        else:
            return False  # Book is already checked out
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successful return
        else:
            return False  # Book is already available
    
    def is_checked_out(self):
        return self._is_checked_out

    lass Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_checked_out():
                    if book.check_out():
                        print(f"Successfully checked out '{title}'")
                    else:
                        print(f"'{title}' is already checked out")
                return
        print(f"'{title}' is not available in the library")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_checked_out():
                    if book.return_book():
                        print(f"Successfully returned '{title}'")
                else:
                    print(f"'{title}' is not checked out")
                return
        print(f"'{title}' is not available in the library")

    def list_available_books(self):
        available_books = [book.title for book in self._books if not book.is_checked_out()]
        if available_books:
            print("Available books:")
            for title in available_books:
                print(f"   {title}")
        else:
            print("No books available in the library")

            from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()

    class Library

