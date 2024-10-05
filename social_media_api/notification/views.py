from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Like
from notifications.models import Notification
from rest_framework.permissions import IsAuthenticated


class LikePostView(APIView):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        if Like.objects.filter(user=user, post=post).exists():
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        Like.objects.create(user=user, post=post)
        
        # Create a notification
        Notification.objects.create(
            recipient=post.author, actor=user, verb="liked", target=post
        )

        return Response({"detail": "Post liked."}, status=status.HTTP_200_OK)

class UnlikePostView(APIView):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        user = request.user

        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()

        return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)



class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.filter(unread=True)
        data = [{
            "actor": notification.actor.username,
            "verb": notification.verb,
            "target": str(notification.target),
            "timestamp": notification.timestamp,
        } for notification in notifications]

        # Mark notifications as read
        notifications.update(unread=False)

        return Response(data)
