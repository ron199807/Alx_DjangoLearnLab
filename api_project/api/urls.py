from django.urls import path, include
from api.views import BookViewSet 
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api.views.py/', views.BookListCreateAPIView.as_view(), name="book_list_create"),
    path('', include(router.urls)),
    path('api-token-auth/',  obtain_auth_token, name='api_token_auth'),
]
