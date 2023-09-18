from django.db import models

# Create your models here.


class Artist(models.Model):

    stagename = models.CharField(
        max_length=50, primary_key=True, help_text="Artist Name")
    social_link = models.URLField(
        max_length=50, blank=True, null=False, help_text="Artist Profile")

    def __str__(self):
        return self.stagename

    class meta:
        ordering = ['stagename']
