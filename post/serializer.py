from rest_framework import serializers
from .models import PostModel
from user.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = PostModel
        fields = ["author","id", "title", "content"]