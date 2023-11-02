import pytest
from rest_framework.test import APIClient
from datetime import datetime
from artists.serializers import ArtistSerializer
from artists.models import Artist
from albums.models import Album
pytestmark = pytest.mark.django_db


class Test_Albums_Endpoints:
    endpoint1 = "/albums/"
    endpoint2 = "/albums/songs"

    def test_album_get(self, create_user):
        client = APIClient()
        response = client.get(self.endpoint1)
        assert response.status_code == 200

    def test_album_post(self, create_user):
        artist = Artist.objects.create(
            stagename="Queen", social_link="https://www.instagram.com/KillerQueenn", user=create_user)
        client = APIClient()
        client.force_authenticate(user=create_user)
        response = client.post(self.endpoint1, {"name": "test Album", "release_datetime": str(datetime.strptime(
            "12/11/2023 09:15:32", "%d/%m/%Y %H:%M:%S")), "cost": 123.1, "artist": artist.pk}, fromat="json")
        print(response.data)
        assert response.status_code == 201

    def test_songs_get(self):
        client = APIClient()
        response = client.get(self.endpoint2)
        assert response.status_code == 200

    def test_invalid_song_post(self, create_user):
        artist = Artist.objects.create(
            stagename="Queen", social_link="https://www.instagram.com/KillerQueenn", user=create_user)
        album = Album.objects.create(name="Cool Album", cost=122.3, release_datetime=datetime.strptime(
            "12/11/2023 09:15:32", "%d/%m/%Y %H:%M:%S"), artist=artist)
        client = APIClient()
        response = client.post(self.endpoint2, data={
                               "name": "Bohemian Rhapsody", "album": album.pk})
      #  print(response.data)
        assert response.status_code == 400
