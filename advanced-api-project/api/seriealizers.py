from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# The BookSerializer serializes all fields of the Book model and includes a custom validation to check that the publication year is not in the future.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation for publication_year
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# The AuthorSerializer serializes the name of the author and dynamically includes related books using the nested BookSerializer.

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serialization of related books

    class Meta:
        model = Author
        fields = ['name', 'books']
