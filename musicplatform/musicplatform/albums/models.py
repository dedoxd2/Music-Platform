from django.db import models
from datetime import datetime
from artists.models import Artist
from django import forms
from django_extensions.db.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.exceptions import ValidationError

# Create your models here.


class Album (TimeStampedModel):
    name = models.CharField(max_length=30, default="New Album")

    creation_datetime = models.DateTimeField(
        'Creation Date ', default=datetime.now)

    release_datetime = models.DateTimeField('Release Date', null=False)

    cost = models.DecimalField(max_digits=7, decimal_places=2)

    artist = models.ForeignKey(
        'artists.Artist', related_name='albums', on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False, )

    def __str__(self):
        return self.name

    class Meta:
        order_with_respect_to = 'artist'


def validate_audio_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path + filename
    valid_extensions = ['.mp3', '.wav']
    if not ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension.")
    else:
        return True


class Song (models.Model):
    name = models.CharField(max_length=50, default='New Song')

    image = models.ImageField(upload_to='songs/images/%y/%m/%d')

    thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(
        100, 50)], format='JPEG', options={'quality': 60})
    audio = models.FileField(
        upload_to='songs/audio/%y/%m/%d', validators=[validate_audio_file_extension], help_text="Allowed Extensions .mp3 , .wav")
    album = models.ForeignKey(
        'Album', on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.album.songs.count() <= 1:
            raise ValidationError("An album must have at least one song")
            super().delete(*args, **kwargs)
