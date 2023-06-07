from .models import (
    ChatRoom,
    Comment,
    CommentReaction,
    DirectMessage,
    DirectMessageReaction,
)
from users.serializers import TinyUserSerializer
from rest_framework.serializers import ModelSerializer


# Chat Rooms


class TinyChatRoomSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = ChatRoom
        fields = [
            "users",
        ]


class ChatRoomSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = ChatRoom
        fields = "__all__"


# Comments


class TinyCommentSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "user",
            "category",
            "text",
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


# Direct Messages


class TinyDirectMessageSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)
    chat_room = TinyChatRoomSerializer()

    class Meta:
        model = DirectMessage
        fields = [
            "user",
            "text",
            "chat_room",
        ]


class DirectMessageSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)
    chat_room = TinyChatRoomSerializer()

    class Meta:
        model = DirectMessage
        fields = "__all__"


# Reactions


class TinyDirectMessageReactionSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)
    direct_message = TinyDirectMessageSerializer()

    class Meta:
        model = DirectMessageReaction
        fields = [
            "user",
            "direct_message",
        ]


class DirectMessageReactionSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = DirectMessageReaction
        fields = "__all__"


class TinyCommentReactionSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)
    comment = TinyCommentSerializer()

    class Meta:
        model = CommentReaction
        fields = [
            "user",
            "comment",
        ]


class CommentReactionSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = CommentReaction
        fields = "__all__"
