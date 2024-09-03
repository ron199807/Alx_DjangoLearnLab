from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework

# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Allow all users to view
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Corrected indentation

    # Define fields that can be filtered
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Define fields that can be searched
    search_fields = ['title', 'author__name']

    # Define fields that can be ordered
    ordering_fields = ['title', 'publication_year']

    # Default ordering (optional)
    ordering = ['title']

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create

    def perform_create(self, serializer):
        # Add custom logic here if needed before saving
        serializer.save()  # Save the book object

# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Add custom update logic here
        serializer.save()

# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


