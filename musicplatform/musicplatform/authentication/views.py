from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import CustomSignupform

# Create your views here.


class LoginForm(LoginView):
    template_name = "auth/login.html"


class SignupForm(CreateView):
    form_class = CustomSignupform
    success_url = reverse_lazy('login')
    template_name = 'auth/signup.html'


class LogoutForm (LogoutView):
    next_page = '/'
