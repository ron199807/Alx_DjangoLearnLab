#retrieve operation

#command:
''' python

book = Book.object.get(id = 1)
print(book.title, book.author, book.publication_year)