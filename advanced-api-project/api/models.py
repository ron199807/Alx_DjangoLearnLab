from django.db import models

# The Author model stores the name of an author.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# The Book model represents a book with a title, publication year, and a link to the author, showing a one-to-many relationship.

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title