from typing import Any
# from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import ArtistForm
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ArtistSerializer
# from musicplatform.tasks import test_func
# Create your views here.


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


# def test(request):
#     test_func.delay()
#     return HttpResponse("Done")
