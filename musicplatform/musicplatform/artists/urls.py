from django.urls import path
from . import views

urlpatterns = [
    path('create', views.artist_form, name='artist_form'),
    path('', views.artist_list, name='artist_list')
]
