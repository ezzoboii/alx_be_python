class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Derived class for e-books
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

# Derived class for print books
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

# Library class using composition to manage a collection of books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, Book):
                if isinstance(book, EBook):
                    print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
                elif isinstance(book, PrintBook):
                    print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
                else:
                    print(f"Book: {book.title} by {book.author}")
            else:
                print("Invalid book type")

# Test cases if required
if __name__ == "__main__":
    # Test your classes here if needed
    pass
 "__str__"
