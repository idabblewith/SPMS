from django.contrib import admin
from .models import (
    Project,
    ProjectArea,
    ResearchFunction,
    ProjectMember,
)
from categories.serializers import ProjectCategorySerializer


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
        "old_id",
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


@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "project",
        # "created_at",
        "updated_at",
    ]

    # list_filter = [
    #     "user",
    # ]

    search_fields = [
        "user__name",
        "project__title",
    ]


@admin.register(ProjectArea)
class ProjectAreaAdmin(admin.ModelAdmin):
    list_display = [
        "project",
        "area",
    ]

    list_filter = [
        "area",
    ]

    search_fields = [
        "project__title",
    ]
