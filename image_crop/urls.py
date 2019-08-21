from django.urls import path, include
from .views import *

urlpatterns = [
    path('photo_list',photo_list, name = 'photo_list'),
]