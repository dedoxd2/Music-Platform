import pytest
from rest_framework.test import APIClient
from users.serializers import UserSerializer
from users.models import User
from decouple import config


@pytest.fixture
def create_user(db=User):
    return User.objects.create_user(username="tesSSSSt", email="test@gmail.com", password="test1111", bio="test")


@pytest.fixture
def auth_client(user=None):
    def api_client(user_instance=user):
        if user_instance == None:
            # arbitrary user
            client = APIClient()
            login = client.post(
                '/auth/login', data={"username": 'tesSSSSt', "password": "test1111"})
            print(login.data)
            token = login.data["token"]
            client.credentials(HTTP_AUTHORIZATION="Token "+token)
            uid = User.objects.get(username="tesSSSSt")
            return client, uid.id  # user.id
        else:
            client = APIClient()

            user_inst = User.objects.create_user(
                username=user_instance["username"], password=user_instance["password"], email=user_instance["email"], bio=user_instance['bio'])
            login = client.post(
                '/auth/login', data={"username": user_inst.username, "password": user_instance['password']})
            token = login.data['token']
            client.credentials(HTTP_AUTHORIZATION='Token ' + token)
            return client, user_inst.pk
    return api_client
