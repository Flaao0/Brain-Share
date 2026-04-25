from rest_framework import serializers

from .models import Meme


class MemeSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Meme
        fields = ["id", "title", "image_path", "author", "likes", "created_at"]
