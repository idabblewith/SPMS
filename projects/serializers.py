from medias.models import ProjectPhoto
from medias.serializers import ProjectImageSerializer
from .models import (
    Project,
    ProjectMember,
    ResearchFunction,
)
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.response import Response


class ProjectSerializer(ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "pk",
            "kind",
            "title",
            "status",
            "description",
            "tagline",
            "keywords",
            "year",
            "number",
            "start_date",
            "end_date",
            "created_at",
            "updated_at",
            "business_area",
            "image",
        )

    def get_image(self, project):
        project_photo = ProjectPhoto.objects.filter(project=project).first()
        if project_photo:
            return project_photo.file
        return None


class TinyProjectSerializer(ModelSerializer):
    image = serializers.SerializerMethodField()
    # image = ProjectImageSerializer()

    class Meta:
        model = Project
        fields = (
            "title",
            "status",
            "kind",
            "year",
            "business_area",
            "image",
        )

    def get_image(self, project):
        project_photo = ProjectPhoto.objects.filter(project=project).first()
        if project_photo:
            return project_photo.file
        return None


class TinyResearchFunctionSerializer(ModelSerializer):
    # leader = TinyUserSerializer()

    class Meta:
        model = ResearchFunction
        fields = (
            "name",
            "description",
            "leader",
            "association",
            "is_active",
        )


class ResearchFunctionSerializer(ModelSerializer):
    # creator = TinyUserSerializer(read_only=True)
    # leader = TinyUserSerializer()

    class Meta:
        model = ResearchFunction
        fields = "__all__"


# class ProjectTeamSerializer(ModelSerializer):
#     class Meta:
#         model = ProjectTeam
#         fields = [
#             "project",
#             "members",
#         ]


class ProjectMemberSerializer(ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = [
            "user",
            "role",
            "time_allocation",
            "position",
            "comments",
            "short_code",
        ]
