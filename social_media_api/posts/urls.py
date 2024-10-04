from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import FollowedUsersPostsView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# urlpatterns =  router.urls


urlpatterns = [
    router.urls

    # URL for the feed of posts from followed users
    path('feed/', FollowedUsersPostsView.as_view(), name='followed-users-feed'),
]

