import pytest
from rest_framework.test import APIClient
pytestmark = pytest.mark.django_db


class Test_ArtistEndpoint:
    endpoint1 = "/artists/"

    def test_get_artists(self):
        client = APIClient()
        response = client.get(self.endpoint1)
        assert response.status_code == 200

    def test_post_artist(self, create_user):
        client = APIClient()
        response = client.post(self.endpoint1, data={
                               "stagename": "Queen", "social_link": "https://www.instagram.com/queen", "user": create_user.pk}, format="json")
    #    print(response.data)
        assert response.status_code == 201
