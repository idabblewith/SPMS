from .models import ScienceProject, StudentProject, ExternalProject, CoreFunctionProject
from rest_framework.serializers import ModelSerializer


class ScienceProjectSerializer(ModelSerializer):
    model = ScienceProject
    fields = "__all__"


class StudentProjectSerializer(ModelSerializer):
    model = StudentProject
    fields = "__all__"


class ExternalProjectSerializer(ModelSerializer):
    model = ExternalProject
    fields = "__all__"


class CoreFunctionProjectSerializer(ModelSerializer):
    model = CoreFunctionProject
    fields = "__all__"


class TinyScienceProjectSerializer(ModelSerializer):
    model = ScienceProject
    fields = [
        "title",
        "tagline",
        "kind",
        "creator_id",
        "effective_from",
        "active",
        "status",
    ]


class TinyStudentProjectSerializer(ModelSerializer):
    model = StudentProject
    fields = [
        "title",
        "tagline",
        "kind",
        "active",
        "status",
        "level",
        "organisation",
    ]


class TinyExternalProjectSerializer(ModelSerializer):
    model = ExternalProject
    fields = [
        "title",
        "tagline",
        "kind",
        "active",
        "status",
        "time_budget",
        "monetary_budget",
        "aims",
    ]


class TinyCoreFunctionProjectSerializer(ModelSerializer):
    model = CoreFunctionProject
    fields = [
        "title",
        "tagline",
        "kind",
        "active",
        "status",
    ]
