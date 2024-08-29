from django.urls import path
from . import views  # Import the views from the current app

urlpatterns = [
    path('api.views.py/', views.BookListCreateAPIView.as_view(), name="book_list_create"),
]
