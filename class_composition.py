class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf contains {len(self.books)} books"


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"This book name is {self.name}"


book1 = Book("Harry Potter")
book2 = Book("Python")

shelf = BookShelf(book1, book2)

print(book1)
print(book2)
print(shelf)