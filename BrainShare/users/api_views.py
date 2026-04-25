from drf_spectacular.utils import extend_schema
from rest_framework import permissions, serializers
from rest_framework.response import Response
from rest_framework.views import APIView


class MyProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(read_only=True)


@extend_schema(
    summary="Мой профиль",
    description="Возвращает данные текущего авторизованного пользователя",
    tags=["Пользователь"],
    responses=MyProfileSerializer,
)
class MyProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        data = {
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
        }
        return Response(data)
