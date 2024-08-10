# Create Operation

## Command:
```python
# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Book: 1984


# Retrieve Operation

## Command:
```python
# Retrieve the book with ID 1
book = Book.objects.get(id=1)
print(book.title, book.author, book.publication_year)

# 1984 George Orwell 1949


# Update Operation

## Command:
```python
# Update the book's title
book.title = "Nineteen Eighty-Four"
book.save()

# Book: Nineteen Eighty-Four


# Delete Operation

## Command:
```python
# Delete the book instance
book.delete()

# Confirming that there are no books left
books = Book.objects.all()
print(books)

# QuerySet []
