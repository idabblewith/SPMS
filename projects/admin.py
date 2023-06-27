from django.contrib import admin
from .models import (
    ScienceProject,
    StudentProject,
    ExternalProject,
    CoreFunctionProject,
    ResearchFunction,
)
from categories.serializers import ProjectCategorySerializer


@admin.register(ScienceProject)
class ScienceProjectAdmin(admin.ModelAdmin):
    kind = ProjectCategorySerializer()
    list_display = (
        # "creator_id",
        "title",
        "kind",
        "active",
        "status",
        # "created_at",
        # "updated_at",
    )


@admin.register(StudentProject)
class StudentProjectAdmin(admin.ModelAdmin):
    kind = ProjectCategorySerializer()
    list_display = (
        # "creator_id",
        "level",
        "organisation",
        "title",
        "kind",
        "active",
        "status",
        # "created_at",
        # "updated_at",
    )


@admin.register(ExternalProject)
class ExternalProjectAdmin(admin.ModelAdmin):
    kind = ProjectCategorySerializer()
    list_display = (
        # "creator_id",
        "time_budget",
        "monetary_budget",
        "title",
        "kind",
        "active",
        "status",
        # "created_at",
        # "updated_at",
    )


@admin.register(CoreFunctionProject)
class CoreFunctionProjectAdmin(admin.ModelAdmin):
    kind = ProjectCategorySerializer()
    list_display = (
        "creator_id",
        "title",
        "kind",
        "active",
        "status",
        # "created_at",
        # "updated_at",
    )


@admin.register(ResearchFunction)
class ResearchFunctionAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "leader",
        "active",
    ]

    list_filter = [
        "active",
        "leader",
    ]

    search_fields = [
        "name",
        "description",
    ]
