from django.contrib import admin
from .models import Artist
from albums.models import Album

# Register your models here.


class AlbumInline (admin.TabularInline):
    model = Album
    extra = 1


class ArtistAdmin (admin.ModelAdmin):
    list_display = ['stagename', 'social_link', 'num_approved']
    inlines = [AlbumInline]
    search_fields = ['stagename']


admin.site.register(Artist, ArtistAdmin)
