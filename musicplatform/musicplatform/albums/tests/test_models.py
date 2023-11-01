import pytest
from albums.models import Song, Album
from artists.models import Artist
from datetime import datetime
pytestmark = pytest.mark.django_db


def create_valid_album(create_user):
    artist = Artist.objects.create(
        stagename="test", social_link="www.instagram.com/test", user=create_user)
    album = Album()
    album.name = "Cool Album"
    album.artist = artist
    album.cost = 12.33
    album.release_datetime = datetime.strptime(
        "12/11/2023 09:15:32", "%d/%m/%Y %H:%M:%S")
    album.save()

    return album


class Test_Album:

    def test_create_invalid_album(self, create_user):
        artist = Artist.objects.create(
            stagename="test", social_link="www.instagram.com/test", user=create_user)
        album = Album()
        album.name = "Cool Album"
        album.artist = artist
        with pytest.raises(Exception):
            album.save()

    def test_create_valid_album(self, create_user):
        artist = Artist.objects.create(
            stagename="test", social_link="www.instagram.com/test", user=create_user)
        album = Album()
        album.name = "Cool Album"
        album.artist = artist
        album.cost = 12.33
        album.release_datetime = datetime.strptime(
            "12/11/2023 09:15:32", "%d/%m/%Y %H:%M:%S")
        album.save()

        assert Album.objects.all().count() == 1
        return album


class Test_Song:
    def test_create_valid_song(self, create_user):
        album = create_valid_album(create_user)
        song = Song()
        song.album = album
        song.save()
        assert Song.objects.all().count() == 1
