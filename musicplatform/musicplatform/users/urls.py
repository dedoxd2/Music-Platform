from django.urls import path, include
from .views import User_pk

urlpatterns = [
    path('<int:pk>', User_pk.as_view()),
]
