from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a user and authenticate for tests requiring authentication
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Set up initial data
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Test Book', publication_year=2023, author=self.author)

    # Test ListView - Retrieve all books
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    # Test DetailView - Retrieve a single book by ID
    def test_detail_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    # Test CreateView - Add a new book
    def test_create_book(self):
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, 'New Book')

    # Test UpdateView - Modify an existing book
    def test_update_book(self):
        url = reverse('book-update', kwargs={'pk': self.book.id})
        data = {
            'title': 'Updated Book',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    # Test DeleteView - Remove a book
    def test_delete_book(self):
        url = reverse('book-delete', kwargs={'pk': self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # Test Filtering - Filter books by author name
    def test_filter_books_by_author(self):
        url = reverse('book-list') + '?author__name=Test Author'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Test Searching - Search books by title
    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Test Book'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Test Ordering - Order books by title
    def test_order_books_by_title(self):
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book')
