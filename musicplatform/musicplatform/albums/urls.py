from django.urls import path
from . import views


urlpatterns = [
    path('', views.AlbumListCreate.as_view(), name='album_form'),
    path('songs', views.SongListCreate.as_view(), name='album_form')
]
