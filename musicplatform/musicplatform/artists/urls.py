from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtistList.as_view()),
  #  path('test', views.test, name='test'),
]
