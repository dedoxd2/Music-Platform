from django.urls import path
from . import views

urlpatterns = [

    path('login', views.LoginForm.as_view(), name='login'),
    path('signup', views.SignupForm.as_view(), name='signup'),
    path('logout', views.LogoutForm.as_view(), name='logout'),

]
