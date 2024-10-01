from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Create a new user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None),
        )

        # Create an auth token for the new user
        Token.objects.create(user=user)

        return user
