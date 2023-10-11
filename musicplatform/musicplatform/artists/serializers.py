from .models import Artist
from rest_framework import serializers
from django.core.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from albums.serializers import AlbumSerializer


def blank_check(str) -> str:
    if str == '':
        raise ValidationError("This Field Is Required ")


class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)
    stagename = serializers.CharField(
        max_length=50, validators=[blank_check])

    social_link = serializers.URLField(
        max_length=50, help_text="Artist Profile", validators=[blank_check])

    def validate_stagename(self, value):
        if Artist.objects.filter(stagename=value).exists():
            raise serializers.ValidationError(
                "This field value already exists.")
        return value

    def validate_social_link(self, value):
        if Artist.objects.filter(social_link=value).exists():
            raise serializers.ValidationError(
                "This field value already exists.")
        return value

    class Meta:
        model = Artist
        fields = '__all__'
