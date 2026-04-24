from django.urls import path
from . import views

app_name = 'mems'

urlpatterns = [
    path('', views.mems_list, name='meme_feed'),
]