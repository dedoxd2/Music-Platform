from typing import Any
from django.shortcuts import render
from .models import *
from .forms import AlbumForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from .serializers import AlbumSerializer, SongSerializer

# Create your views here.


class AlbumListCreate(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongListCreate(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


# class AlbumFormView (LoginRequiredMixin, FormView):
#     template_name = 'albums/album_form.html'
#     form_class = AlbumForm

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context['AlbumForm'] = context.pop('form')

#         return context

# def album_form(request):

#     if request.method == "POST":
#         form = AlbumForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = AlbumForm()
#     return render(request, 'albums/album_form.html', {'AlbumForm': AlbumForm})
