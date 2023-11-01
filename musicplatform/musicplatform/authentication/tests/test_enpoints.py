import pytest
from rest_framework.test import APIClient
from users.models import User
# register  login logout logoutall
# login endpoint has been tested in previous tests
pytestmark = pytest.mark.django_db


class Test_Auth:
    baseURL = "/auth/"

    def test_register_get(self):
        client = APIClient()
        response = client.get(self.baseURL + "register")
        assert response.status_code == 200

    def test_register_post(self):
        client = APIClient()
        response = client.post(self.baseURL + "register", data={
            "username": "Username", "email": "email@gmail.com", "password1": "Pa$$w0rD!", "password2": "Pa$$w0rD!"})
        assert response.status_code == 201

    @pytest.mark.parametrize("username, email, password1, password2,validity", [
        ("", "email@gmail.com", "Pa$$w0rD!", "Pa$$w0rD!", False),
        ("Username", "", "Pa$$w0rD!", "Pa$$w0rD!", True),
        ("Username", "email@gmail.com", "", "Pa$$w0rD!", False),
        ("Username", "email@gmail.com", "Pa$$w0rD!", "", False),
        ("Username", "email@gmail.com", "Pa$$w0rD!", "Pa$$w0rD!", True)

    ])
    def test_invalid_register_post(self, username, email, password1, password2, validity):
        client = APIClient()
        response = client.post(self.baseURL + "register", data={
            "username": username, "email": email, "password1": password1, "password2": password2})

        validation = User.objects.all().count()
        assert validation == validity

    def test_login_fail(self, auth_client):
        client = APIClient()
        payload = {
            "username": "remarema",
            "password": "ldifuhtrl23"
        }
        response = client.post("/auth/login", payload)
        assert response.status_code == 400

    def test_logout_user(self, auth_client, create_user):
        client = APIClient()
        response = client.post(
            '/auth/login', data={"username": "tesSSSSt", "password": "test1111"})
        token = response.data["token"]
        client.credentials(HTTP_AUTHORIZATION="Token "+token)
        response = client.post("/auth/logout")
        assert response.status_code == 204

    def test_logout_unauthenticated_user(self):
        client = APIClient()
        response = client.post("/auth/logout")
        assert response.status_code == 401  # UnAuthorized
