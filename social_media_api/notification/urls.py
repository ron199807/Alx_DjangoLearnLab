from django.urls import path
from .views import NotificationListView

urlpatterns = [
    # Notification URL
    path('', NotificationListView.as_view(), name='notifications-list'),
]
