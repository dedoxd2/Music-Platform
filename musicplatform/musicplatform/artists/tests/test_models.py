import pytest
from artists.models import Artist
from datetime import datetime
pytestmark = pytest.mark.django_db


class Test_Artist:
    def test_create_invalid_artist(self):
        artist = Artist()
        artist.stagename = "Test"
        artist.stagename = "https://www.instagram.com/Test"

        with pytest.raises(Exception):
            artist.save()

    def test_create_invalid_artist_UniqueViloation(self, create_user):
        artist = Artist()
        artist.stagename = "Test"
        artist.stagename = "https://www.instagram.com/Test"
        artist.user = create_user
        artist.save()
        artist2 = Artist()
        artist2.stagename = "Test"
        artist2.stagename = "https://www.instagram.com/Test"
        artist2.user = create_user
        with pytest.raises(Exception):
            artist2.save()

    def test_create_valid_artist(self, create_user):
        artist = Artist()
        artist.stagename = "Test"
        artist.stagename = "https://www.instagram.com/Test"
        artist.user = create_user
        artist.save()
        assert Artist.objects.all().count() == 1
