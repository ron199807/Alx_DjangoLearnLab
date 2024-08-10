# Delete Operation

## Command:
```python
# Delete the book instance
book.delete()

# Confirming that there are no books left
books = Book.objects.all()
print(books)

# QuerySet []
