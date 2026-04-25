from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .models import Category, Note
from .serializers import CategorySerializer, NoteSerializer


@extend_schema(
    summary="Список категорий",
    description="Возвращает массив всех доступных категорий конспектов",
    tags=["Категории"],
)
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(
    summary="Список конспектов",
    description="Возвращает массив всех конспектов",
    tags=["Конспекты"],
)
class NoteListAPIView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


@extend_schema(
    summary="Детальная информация о конспекте",
    description="Возвращает полную информацию об одном конспекте по id",
    tags=["Конспекты"],
)
class NoteDetailAPIView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
