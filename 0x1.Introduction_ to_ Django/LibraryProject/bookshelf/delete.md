# delete the book instance

# command
''' python
book.delete()
# confirming that there are no books left
books = Book.objects.all()
print(books)

# QuerySet []