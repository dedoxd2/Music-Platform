from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *
from .forms import AlbumForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import AlbumSerializer, SongSerializer
from rest_framework.pagination import LimitOffsetPagination
from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AlbumFilter
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from django.core.exceptions import SuspiciousOperation

# Create your views here.


class AlbumListCreate(generics.ListCreateAPIView):
    queryset = Approved_Albums()
    serializer_class = AlbumSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_classes = AlbumFilter
    # ['cost', 'name'] # -> the cost field didn't work with the range queries
    filterset_fields = AlbumFilter.get_fields()
    search_fields = ['name']
    ordering_fields = ['name', 'cost']

    def post(self, request):
        if request.user.is_authenticated:
            try:
                artist = Artist.objects.get(user=request.user)
            except ObjectDoesNotExist:
                return Response("U Must Be An Artist So You Can Add Albums", status=status.HTTP_403_FORBIDDEN)
            if artist.user == request.user:

                album = AlbumSerializer(data=request.data)
                if album.is_valid():
                    album.save()
                    return Response(album.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(album.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("U Must Be This Artist so you can add to him Albums ", status=status.HTTP_403_FORBIDDEN)

        else:
            return Response("Please Login First", status=status.HTTP_403_FORBIDDEN)


class AlbumList_FilterManually(ListAPIView):
    serializer_class = AlbumSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        queryset = Approved_Albums()
        # Implement custom filtering logic ,anually
        cost__gte = self.request.query_params.get("cost__gte")
        cost__lte = self.request.query_params.get("cost__lte")
        name = self.request.query_params.get('name__icontains')
        if type(cost__gte) == str or type(cost__lte) == type("sad"):
            raise SuspiciousOperation("Please Enter Numerical Value !")
        print(name)
        if cost__gte is not None:
            queryset = queryset.filter(cost__gte=cost__gte)
        if cost__lte is not None:
            queryset = queryset.filter(cost__lte=cost__lte)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SongListCreate(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
