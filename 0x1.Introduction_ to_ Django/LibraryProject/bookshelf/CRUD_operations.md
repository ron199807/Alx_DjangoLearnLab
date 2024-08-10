# Create Operation

## Command:
'''python

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# output
# Book: 1984

# retrieve operation

# Command:
'''python

book = Book.object.get(id = 1)
print(book.title, book.author, book.publication_year)

# output
# 1984 George Orwell

# update operation

# command:
''' python
book.title = "Nineteen Eighty-Four"
book.save()
# output
# Book: Nineteen Eighty-Four

# delete the book instance

# command
''' python
book.delete()
# confirming that there are no books left
books = Book.objects.all()
print(books)

# output
# QuerySet []
