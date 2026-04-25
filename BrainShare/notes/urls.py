from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path("", views.home_page, name="note_list"),
    path("notes/", views.note_list, name="notes"),
    path('<int:pk>/', views.note_detail_view, name='note_detail'),
    path("add/", views.add_note_view, name="add_note"),
]