from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio']
