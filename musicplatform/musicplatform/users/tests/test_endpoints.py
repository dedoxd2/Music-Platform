import pytest
from rest_framework.test import APIClient
from users.models import User
from users.serializers import UserSerializer
pytestmark = pytest.mark.django_db


class Test_UserEndpoint:

    def test_get_method(self, auth_client, create_user):
        client, id = auth_client()
        # {"username": "za3tar", "password": "Pa$$w0rd!", "email": "checktest@gmail.com", "bio": "bio"}) # Optional
        response = client.get(f"/user/{id}/")
        assert response.status_code == 200

    def test_put_method(self, auth_client, create_user):
        client, id = auth_client()
        response = client.put(
            f"/user/{id}/", {"username": "NewUsername", "email": "NEWEmail@gmail.com", "bio": "bioooooo"})
        assert response.status_code == 202
        user = User.objects.get(id=id)
        assert user.bio == "bioooooo"
        assert user.username == "NewUsername"
        assert user.email == "NEWEmail@gmail.com"

    def test_patch_method(self, auth_client, create_user):
        client, id = auth_client()
        response = client.patch(
            f"/user/{id}/", {"username": "NewUsername"})
        assert response.status_code == 202
        user = User.objects.get(id=id)
        assert user.username == "NewUsername"

    def test_UnAuthorized(self, auth_client, create_user):
        client1, id1 = auth_client()

        client2, id2 = auth_client({"username": "za3tar", "password": "Pa$$w0rd!",
                                   "email": "checktest@gmail.com", "bio": "bio"})

        response = client2.get(f"/user/{id1}/")
        assert response.status_code == 401  # UnAuthorized Access Denied
