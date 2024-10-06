from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import FollowedUsersPostsView
from notification.views import LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

# urlpatterns =  router.urls


urlpatterns = [
    router.urls,

    # URL for the feed of posts from followed users
    path('feed/', FollowedUsersPostsView.as_view(), name='followed-users-feed'),

    # Like and Unlike URLs
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),


]

