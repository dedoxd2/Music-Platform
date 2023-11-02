from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CustomSignupform
from rest_framework import generics, status
from rest_framework.response import Response
from users.models import User
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from users.serializers import UserSerializer
from django.contrib.auth import authenticate, login
# Create your views here.


class RegisterAPI(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginAPI(generics.GenericAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    authentication_classes = []

    def post(self, request, *arg, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user)[1]
        login(request, user)
        return Response(data={'token': token,
                              'user': UserSerializer(user, context=self.get_serializer_context()).data},
                        status=status.HTTP_202_ACCEPTED)


class LogoutForm (LogoutView):
    next_page = '/'
