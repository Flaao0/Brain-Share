from drf_spectacular.utils import extend_schema
from rest_framework import generics

from .models import Meme
from .serializers import MemeSerializer


@extend_schema(
    summary="Список мемов",
    description="Возвращает массив всех мемов",
    tags=["Мемы"],
)
class MemeListAPIView(generics.ListAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer


@extend_schema(
    summary="Детальная информация о меме",
    description="Возвращает полную информацию об одном меме по id",
    tags=["Мемы"],
)
class MemeDetailAPIView(generics.RetrieveAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer
