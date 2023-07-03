from medias.models import ProjectPhoto
from medias.serializers import ProjectImageSerializer
from .models import (
    # ScienceProject,
    # StudentProject,
    # ExternalProject,
    # CoreFunctionProject,
    Project,
    ResearchFunction,
)
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.response import Response


# class ScienceProjectSerializer(ModelSerializer):
#     model = ScienceProject
#     fields = "__all__"


# class StudentProjectSerializer(ModelSerializer):
#     model = StudentProject
#     fields = "__all__"


# class ExternalProjectSerializer(ModelSerializer):
#     model = ExternalProject
#     fields = "__all__"


# class CoreFunctionProjectSerializer(ModelSerializer):
#     model = CoreFunctionProject
#     fields = "__all__"


# class TinyScienceProjectSerializer(ModelSerializer):
#     model = ScienceProject
#     fields = [
#         "title",
#         "tagline",
#         "kind",
#         "creator_id",
#         "effective_from",
#         "active",
#         "status",
#     ]


# class TinyStudentProjectSerializer(ModelSerializer):
#     model = StudentProject
#     fields = [
#         "title",
#         "tagline",
#         "kind",
#         "active",
#         "status",
#         "level",
#         "organisation",
#     ]


# class TinyExternalProjectSerializer(ModelSerializer):
#     model = ExternalProject
#     fields = [
#         "title",
#         "tagline",
#         "kind",
#         "active",
#         "status",
#         "time_budget",
#         "monetary_budget",
#         "aims",
#     ]


# class TinyCoreFunctionProjectSerializer(ModelSerializer):
#     model = CoreFunctionProject
#     fields = [
#         "title",
#         "tagline",
#         "kind",
#         "active",
#         "status",
#     ]


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
