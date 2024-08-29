from django.urls import path, include
from .views import BookViewSet 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api.views.py/', views.BookListCreateAPIView.as_view(), name="book_list_create"),
]
