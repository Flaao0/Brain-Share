from django.urls import path
from . import api_views, views

app_name = 'mems'

urlpatterns = [
    path('', views.mems_list, name='meme_feed'),
    path('add/', views.add_meme, name='add_meme'),
    path('<int:pk>/edit/', views.edit_meme, name='edit_meme'),
    path('<int:pk>/delete/', views.delete_meme, name='delete_meme'),
    path("api/memes/", api_views.MemeListAPIView.as_view(), name="api_memes"),
    path("api/memes/<int:pk>/", api_views.MemeDetailAPIView.as_view(), name="api_meme_detail"),
]