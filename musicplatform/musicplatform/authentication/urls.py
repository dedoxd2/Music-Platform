from django.urls import path
from . import views
from knox.views import LogoutAllView, LogoutView

urlpatterns = [
    path('register', views.RegisterAPI.as_view()),
    path('login', views.LoginAPI.as_view()),
    path('logout', LogoutView.as_view()),
    path('logoutall', LogoutAllView.as_view()),
]
