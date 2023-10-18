from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    bio = models.TextField(max_length=256, blank=True)

    def __str__(self):
        return self.username
