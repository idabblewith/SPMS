from rest_framework import serializers

from entities.serializers import (
    TinyBranchSerializer,
    TinyBusinessAreaSerializer,
    TinyEntitySerializer,
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
            "entity",
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
    about = serializers.CharField(source="profile.profile_text")
    entity = TinyEntitySerializer(source="profile.member_of")
    branch = serializers.CharField(source="work.branch")

    # entity = serializers.CharField(source="work.branch.entity")  # Assuming 'branch' has a foreign key to 'Entity' model

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
            "entity",
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


# class TinyUserWorkSerializer(serializers.ModelSerializer):
#     user_id = TinyUserSerializer()
#     branch_id = TinyBranchSerializer()
#     business_area_id = TinyBusinessAreaSerializer()

#     class Meta:
#         model = UserWork
#         fields = (
#             "user_id",
#             "branch_id",
#             "business_area_id",
#         )


# class UserWorkSerializer(serializers.ModelSerializer):
#     user_id = TinyUserSerializer()
#     branch_id = TinyBranchSerializer()
#     business_area_id = TinyBusinessAreaSerializer()

#     class Meta:
#         model = UserWork
#         fields = "__all__"


# class TinyUserProfileSerializer(serializers.ModelSerializer):
#     user_id = TinyUserSerializer()
#     member_of = TinyEntitySerializer()
#     image = PhotoSerializer()

#     class Meta:
#         model = UserProfile
#         fields = (
#             "user_id",
#             "profile_text",
#             "expertise",
#             "member_of",
#         )


# class UserProfileSerializer(serializers.ModelSerializer):
#     user_id = TinyUserSerializer()
#     member_of = TinyEntitySerializer()
#     image = PhotoSerializer()

#     class Meta:
#         model = UserProfile
#         fields = "__all__"
