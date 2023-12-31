from django.contrib import admin
from .models import Artist
from albums.models import Album
from albums.admin import AlbumInline

# Register your models here.



class ArtistAdmin (admin.ModelAdmin):
    list_display = ['stagename', 'social_link', 'num_approved']
    search_fields = ['stagename']


admin.site.register(Artist, ArtistAdmin)
