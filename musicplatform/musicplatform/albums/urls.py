from django.urls import path
from . import views


urlpatterns = [
    path('create', views.AlbumFormView.as_view(), name='album_form')
]
