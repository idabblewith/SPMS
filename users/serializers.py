from rest_framework import serializers

from agencies.serializers import (
    TinyBranchSerializer,
    TinyBusinessAreaSerializer,
    TinyAgencySerializer,
)
from medias.serializers import UserAvatarSerializer
from .models import User, UserWork, UserProfile


class UpdatePISerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "first_name",
            "last_name",
            "username",
            "email",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
            "image",
            "role",
            "expertise",
            "title",
            "about",
            "agency",
            "branch",
        )


class UpdateProfileSerializer(serializers.ModelSerializer):
    pass


class UpdateMembershipSerializer(serializers.ModelSerializer):
    pass


class ProfilePageSerializer(serializers.ModelSerializer):
    image = UserAvatarSerializer(source="profile.image")
    role = serializers.CharField(source="profile.role")

    expertise = serializers.CharField(source="profile.expertise")
    title = serializers.CharField(source="profile.title")
    about = serializers.CharField(source="profile.about")
    agency = TinyAgencySerializer(source="profile.agency")
    branch = serializers.CharField(source="work.branch")

    class Meta:
        model = User
        fields = (
            "pk",
            "first_name",
            "last_name",
            "username",
            "email",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
            "image",
            "role",
            "expertise",
            "title",
            "about",
            "agency",
            "branch",
        )


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
    role = serializers.CharField(source="profile.role")
    branch = serializers.CharField(source="work.branch")

    class Meta:
        model = User
        fields = (
            "pk",
            "first_name",
            "last_name",
            "username",
            "email",
            "is_superuser",
            "is_staff",
            "role",
            "branch",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
