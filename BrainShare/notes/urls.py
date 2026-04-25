from django.urls import path
from . import api_views, views

app_name = 'notes'
urlpatterns = [
    path("", views.home_page, name="note_list"),
    path("notes/", views.note_list, name="notes"),
    path("notes/history/", views.viewed_notes_history, name="history"),
    path('<int:pk>/', views.note_detail_view, name='note_detail'),
    path("add/", views.add_note_view, name="add_note"),
    path("<int:pk>/edit/", views.edit_note_view, name="edit_note"),
    path("<int:pk>/delete/", views.delete_note_view, name="delete_note"),
    path("toggle-theme/", views.toggle_theme, name="toggle_theme"),
    path("api/categories/", api_views.CategoryListAPIView.as_view(), name="api_categories"),
    path("api/notes/", api_views.NoteListAPIView.as_view(), name="api_notes"),
    path("api/notes/<int:pk>/", api_views.NoteDetailAPIView.as_view(), name="api_note_detail"),
]