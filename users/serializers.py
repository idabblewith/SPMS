from rest_framework import serializers

from entities.serializers import (
    TinyBranchSerializer,
    TinyBusinessAreaSerializer,
    TinyEntitySerializer,
)
from medias.serializers import PhotoSerializer
from .models import User, UserWork, UserProfile


class PrivateTinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = [
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        ]


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TinyUserWorkSerializer(serializers.ModelSerializer):
    user_id = TinyUserSerializer()
    branch_id = TinyBranchSerializer()
    business_area_id = TinyBusinessAreaSerializer()

    class Meta:
        model = UserWork
        fields = (
            "user_id",
            "branch_id",
            "business_area_id",
        )


class UserWorkSerializer(serializers.ModelSerializer):
    user_id = TinyUserSerializer()
    branch_id = TinyBranchSerializer()
    business_area_id = TinyBusinessAreaSerializer()

    class Meta:
        model = UserWork
        fields = "__all__"


class TinyUserProfileSerializer(serializers.ModelSerializer):
    user_id = TinyUserSerializer()
    member_of = TinyEntitySerializer()
    image = PhotoSerializer()

    class Meta:
        model = UserProfile
        fields = (
            "user_id",
            "profile_text",
            "expertise",
            "member_of",
        )


class UserProfileSerializer(serializers.ModelSerializer):
    user_id = TinyUserSerializer()
    member_of = TinyEntitySerializer()
    image = PhotoSerializer()

    class Meta:
        model = UserProfile
        fields = "__all__"
