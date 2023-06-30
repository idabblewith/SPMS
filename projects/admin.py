from django.contrib import admin
from .models import (
    # ScienceProject,
    # StudentProject,
    # ExternalProject,
    # CoreFunctionProject,
    Project,
    # ProjectDetails,
    # StudentProjectDetails,
    ResearchFunction,
)
from categories.serializers import ProjectCategorySerializer


# @admin.register(ScienceProject)
# class ScienceProjectAdmin(admin.ModelAdmin):
#     kind = ProjectCategorySerializer()
#     list_display = (
#         # "creator_id",
#         "title",
#         "kind",
#         "active",
#         "status",
#         # "created_at",
#         # "updated_at",
#     )


# @admin.register(StudentProject)
# class StudentProjectAdmin(admin.ModelAdmin):
#     kind = ProjectCategorySerializer()
#     list_display = (
#         # "creator_id",
#         "level",
#         "organisation",
#         "title",
#         "kind",
#         "active",
#         "status",
#         # "created_at",
#         # "updated_at",
#     )


# @admin.register(ExternalProject)
# class ExternalProjectAdmin(admin.ModelAdmin):
#     kind = ProjectCategorySerializer()
#     list_display = (
#         # "creator_id",
#         "time_budget",
#         "monetary_budget",
#         "title",
#         "kind",
#         "active",
#         "status",
#         # "created_at",
#         # "updated_at",
#     )


# @admin.register(CoreFunctionProject)
# class CoreFunctionProjectAdmin(admin.ModelAdmin):
#     kind = ProjectCategorySerializer()
#     list_display = (
#         "creator_id",
#         "title",
#         "kind",
#         "active",
#         "status",
#         # "created_at",
#         # "updated_at",
#     )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # kind = ProjectCategorySerializer()
    list_display = [
        "title",
        "year",
        "kind",
        "status",
        "business_area",
    ]

    search_fields = [
        "title",
        "tagline",
        "description",
    ]

    list_filter = [
        "kind",
        "status",
        "year",
        "business_area",
    ]


@admin.register(ResearchFunction)
class ResearchFunctionAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "description",
        "leader",
        "is_active",
    ]

    list_filter = [
        "is_active",
        "leader",
    ]

    search_fields = [
        "name",
        "description",
    ]
