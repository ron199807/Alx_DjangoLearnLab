from rest_framework import serializers
from posts.models import Like Notification


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'post']  # You can add other fields if necessary (e.g., 'created_at')
        read_only_fields = ['user']

    def create(self, validated_data):
        # Create a like instance, the user is added through the request
        user = self.context['request'].user
        post = validated_data['post']

        # Check if the like already exists
        if Like.objects.filter(user=user, post=post).exists():
            raise serializers.ValidationError("You have already liked this post.")

        return Like.objects.create(user=user, post=post)


      

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()  # Display the actor as a string (username)
    target = serializers.SerializerMethodField()  # Custom method to display the target
    recipient = serializers.StringRelatedField()  # Display recipient username

    class Meta:
        model = Notification
        fields = ['recipient', 'actor', 'verb', 'target', 'timestamp', 'unread']
        read_only_fields = ['recipient', 'actor', 'verb', 'target', 'timestamp', 'unread']

    def get_target(self, obj):
        # Return a string representation of the target (e.g., Post title)
        return str(obj.target)
