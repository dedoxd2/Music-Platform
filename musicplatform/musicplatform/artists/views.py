from django.shortcuts import render
from .models import *
from .forms import ArtistForm


# Create your views here.


def artist_form(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ArtistForm()

    return render(request, 'artists/artist_form.html', {'ArtistForm': form})


def artist_list(request):
    artists_list = Artist.objects.prefetch_related('albums')

    return render(request, 'artists/artist_list.html', {'list': artists_list})
