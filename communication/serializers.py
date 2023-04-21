from rest_framework.serializers import ModelSerializer
from .models import Comment
from users.serializers import TinyUserSerializer


class TinyCommentSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "user",
            "category",
            "payload",
            "science_project",
            "student_project",
            "external_project",
            "core_function_project",
        ]


class CommentSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
