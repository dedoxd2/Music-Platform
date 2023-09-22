from django.urls import path
from . import views


urlpatterns = [
    path('create', views.album_form, name='album_form')
]
