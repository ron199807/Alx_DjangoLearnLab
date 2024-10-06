from django.urls import path
from .views import RegisterUser, LoginUser, FollowUserView, UnfollowUserView, ListFollowersView, ListFollowingView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),

    # following urls
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('followers/<int:user_id>/', ListFollowersView.as_view(), name='list_followers'),
    path('following/<int:user_id>/', ListFollowingView.as_view(), name='list_following'),

]
