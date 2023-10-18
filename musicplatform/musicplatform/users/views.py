from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
# Create your views here.


class User_pk(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except:
            return Response('Not Found', status=status.HTTP_400_BAD_REQUEST)
        if request.user == user:
            data = {'id': user.pk, 'username': user.username,
                    'email': user.email, 'bio': user.bio}
        else:
            return Response('Permision Denied', status=status.HTTP_401_UNAUTHORIZED)
        return Response(data=data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except:
            return Response('Not Found', status=status.HTTP_400_BAD_REQUEST)
        if request.user == user:
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                print(serializer.errors)
                return Response("Please Enter Valid Data", status=status.HTTP_406_NOT_ACCEPTABLE)

        else:
            return Response('Permision Denied', status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except:
            return Response('Not Found', status=status.HTTP_400_BAD_REQUEST)
        if request.user == user:
            serializer = UserSerializer(
                user, data=request.data)  # , partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                print(serializer.errors)
                return Response("Please Enter Valid Data or Make Sure you have provided the whole fields ", status=status.HTTP_406_NOT_ACCEPTABLE)

        else:
            return Response('Permision Denied', status=status.HTTP_401_UNAUTHORIZED)
