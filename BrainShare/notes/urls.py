from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path("", views.home_page, name="home"),
    path("notes/", views.note_list, name="notes"),
]