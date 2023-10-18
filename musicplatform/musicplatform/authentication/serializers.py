from rest_framework import serializers
from users.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def validate(self, request):
        password1 = request.get('password1')
        password2 = request.get('password2')
        if password1 != password2:
            raise serializers.ValidationError("Passwords Must Match")
        validate_password(password1)

        return request

    def create(self, validated_data):
        user = User.objects.create(username=validated_data.get('username'),
                                   email=validated_data.get('email').lower())
        user.set_password(validated_data.get('password1'))
        user.save()

        # password=validated_data.get('password1'))

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user

        raise serializers.ValidationError('Incorrect Credentials')

    # class Meta:
    #     model = User
    #     fields = ['username', 'password1']
