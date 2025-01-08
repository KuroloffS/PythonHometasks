class BookNotFoundException(Exception):
    """Raised when attempting to borrow a book that does not exist in the library."""
    pass

class BookAlreadyBorrowedException(Exception):
    """Raised when boook already borrowed by someone."""
    pass

class MemberLimitExceededException(Exception):
    """Raised when member reached limit of borrowed books."""
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def reset_borrowed_status(self):
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}" + (" (Borrowed)" if self.is_borrowed else "")

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book not in library.books:
            raise BookNotFoundException(f"The book '{book.title}' does not exist in the library.")
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"{book.title} is already borrowed.")

        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

    def __str__(self):
        borrowed = ', '.join([book.title for book in self.borrowed_books]) or "No books borrowed"
        return f"Member: {self.name}, Borrowed books: {borrowed}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def _find_member_and_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise ValueError(f"Member {member_name} not found.")

        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException(f"Book {book_title} not found in the library.")

        return member, book

    def borrow_book(self, member_name, book_title):
        member, book = self._find_member_and_book(member_name, book_title)
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member, book = self._find_member_and_book(member_name, book_title)
        member.return_book(book)

    def __str__(self):
        books = '\n'.join([str(book) for book in self.books]) or "No books in the library."
        members = '\n'.join([str(member) for member in self.members]) or "No members in the library."
        return f"Library Books:\n{books}\n\nLibrary Members:\n{members}"

# Test cases
library = Library()

# Adding books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("1984", "George Orwell")
book3 = Book("To Kill a Mockingbird", "Harper Lee")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Adding members
member1 = Member("Alice")
member2 = Member("Bob")
library.add_member(member1)
library.add_member(member2)

# Borrowing books
try:
    library.borrow_book("Alice", "The Great Gatsby")
    library.borrow_book("Bob", "1984")
    library.borrow_book("Alice", "To Kill a Mockingbird")
except Exception as e:
    print(e)

# Returning books
try:
    library.return_book("Alice", "The Great Gatsby")
except Exception as e:
    print(e)

# Exception handling
try:
    library.borrow_book("Alice", "Nonexistent Book")
except Exception as e:
    print(e)

try:
    library.borrow_book("Bob", "1984")
except Exception as e:
    print(e)

try:
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "The Great Gatsby")
except Exception as e:
    print(e)

print(library)
