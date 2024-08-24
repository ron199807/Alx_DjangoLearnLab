from relationship_app.models import Author, Book, Librarian, Library

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # This line filters books by the specific author
        return books
    except Author.DoesNotExist:
        return None

def book_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = library.books.all()
    return books

def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return 
    

if __name__ == "__main__":
    print(books_by_author("ronald"))
    print(books_in_library("ron's lib"))
    print(librarian_for_library("hendrix"))