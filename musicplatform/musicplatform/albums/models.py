from django.db import models
from datetime import datetime
from artists.models import Artist

# Create your models here.


class Album (models.Model):
    name = models.CharField(max_length=30, default="New Album")

    creation_datetime = models.DateTimeField(
        'Creation Date ', default=datetime.now)

    release_datetime = models.DateTimeField('Release Date', null=False)

    cost = models.DecimalField(max_digits=7, decimal_places=2)

    artist = models.ForeignKey(
        'artists.Artist', related_name='albums', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        order_with_respect_to = 'artist'
