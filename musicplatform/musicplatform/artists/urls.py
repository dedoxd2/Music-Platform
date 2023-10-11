from django.urls import path
from . import views

urlpatterns = [
    # path('create', views.artist_form, name='artist_form'),
    # path('', views.artist_list, name='artist_list')
    # path('create', views.ArtistFormView.as_view(), name='artist_form'),
    # path('', views.ArtistListView.as_view(), name='artist_list')
    path('', views.ArtistList.as_view())


]
