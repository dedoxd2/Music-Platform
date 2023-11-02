import pytest
from rest_framework.test import APIClient
from datetime import datetime
from artists.serializers import ArtistSerializer
from artists.models import Artist
from albums.models import Album
from users.models import User
from django.contrib.auth import authenticate
from datetime import datetime
pytestmark = pytest.mark.django_db


class TestAlbumAPI:
    def test_get(self):
        client = APIClient()
        response1 = client.get('/albums/')
        response2 = client.get('/albums/manually/')
        assert response1.status_code == 200
        assert response2.status_code == 200

    def test_post(self):
        client = APIClient()

        artist = ArtistSerializer(
            data={"stagename": "Test", "social_link": "https://www.instagram.com/testy", "user": 1})
        if artist.is_valid():
            artist.save()

        response = client.post(
            "/albums/", {'name': "New Album", "artist": artist})
        albums = Album.objects.all().count()
      #  print(response)
      #  print(response.data)  # -> Please Login First
     #   print(albums)

        assert response.status_code == 403

    def test__invalid_Data_post(self, create_user):
        client = APIClient()

        login = client.post(
            "/auth/login", data={"username": "tesSSSSt", "password": "test1111"})
        print(login)
        token = login.data["token"]
        client.credentials(HTTP_AUTHORIZATION="Token "+token)
        user = authenticate(client)
        artist = ArtistSerializer(
            data={"stagename": "Test", "social_link": "https://www.instagram.com/testy", "user": 1})
        if artist.is_valid():
            artist.save()

        response = client.post(
            "/albums/", {'name': "New Album", "artist": artist})
        albums = Album.objects.all().count()
        assert response.status_code == 400

    def test__valid_post(self, create_user):
        client = APIClient()

        login = client.post(
            "/auth/login", data={"username": "tesSSSSt", "password": "test1111"})
        print(login)
        token = login.data["token"]
        client.credentials(HTTP_AUTHORIZATION="Token "+token)
        user = authenticate(client)
        client.login()

        print(user)

        artist = ArtistSerializer(
            data={"stagename": "Test", "social_link": "https://www.instagram.com/testy", "user": 1})
        if artist.is_valid():
            artist.save()

        response = client.post(
            "/albums/", {'name': "New Album", "artist": 1, "release_datetime": datetime.strptime(
                "12/11/2023 09:15:32", "%d/%m/%Y %H:%M:%S"), "cost": 20.33})
        albums = Album.objects.all().count()
        assert response.status_code == 201
