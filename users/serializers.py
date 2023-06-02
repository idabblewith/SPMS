from rest_framework import serializers
from .models import User


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
        )


class FullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
