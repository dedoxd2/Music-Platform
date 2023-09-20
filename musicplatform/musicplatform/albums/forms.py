from django import forms
from .models import Album


class AlbumForm (forms.ModelForm):
    is_approved = forms.BooleanField(
        help_text="Approve the album if its name is not explicit")  # To Avoid Changing the field itself

    class Meta:
        model = Album
        fields = '__all__'
