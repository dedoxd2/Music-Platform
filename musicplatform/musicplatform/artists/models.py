from django.db import models
from django.db.models import Count, Q, QuerySet
from django.db.models.query import QuerySet
from users.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.


class ArtistQuerySet(QuerySet):
    def with_approved_albums(self):
        return self.annotate(approved_albums=Count('albums', filter=Q(albums__is_approved=True)))


class ArtistManager(models.Manager):
    def get_queryset(self):
        return ArtistQuerySet(self.model, using=self._db).with_approved_albums()


class Artist(models.Model):

    stagename = models.CharField(
        max_length=50, unique=True, help_text="Artist Name")
    social_link = models.URLField(
        max_length=50, blank=True, null=False, unique=True, help_text="Artist Profile")
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    objects = ArtistManager()

    def __str__(self):
        return self.stagename

    @property
    def num_approved(self):
        return self.albums.filter(is_approved=True).count()
   # num_approved.short_description = 'Number of approved albums'

    class meta:
        ordering = ['stagename']
