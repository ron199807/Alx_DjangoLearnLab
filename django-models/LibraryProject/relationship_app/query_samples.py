from relationship_app.models import Author, Book, Librarian, Library

def book_by_author(author_name):
    author = Author.objects.get(name = author_name)
    books = library.books.all()
    return books

def librarian_for_library(library_name):
    library = Library.objects.get(name = library_name)
    librarian = Librarian.objects.get(library = library)
    return librarian

if __name__ == "__main__":
    print(books_by_author("ronald"))
    print(books_in_library("ron's lib"))
    print(librarian_for_library("hendrix"))