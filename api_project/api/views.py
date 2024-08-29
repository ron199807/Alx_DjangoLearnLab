from django.shortcuts import render
from rest_framework import generics.ListAPIView
from .models import MyModel
from .serializers import MyModelserializer
from .serializers import BookSerializer
from rest_framework import BookViewSet

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

