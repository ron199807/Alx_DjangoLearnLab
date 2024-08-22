from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # class-based view URL
    
    path('login/', CustomLoginView.as_view(), name='login'),  # Login URL
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Logout URL
    path('register/', register, name='register'),  # Registration URL

]
