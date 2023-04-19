from django.contrib import admin
from .models import ScienceProject, StudentProject, ExternalProject, CoreFunctionProject


@admin.register(ScienceProject)
class ScienceProjectAdmin(admin.ModelAdmin):
    list_display = (
        "creator_id",
        "title",
        "type",
        "active",
        "status",
        "created_at",
        "updated_at",
    )


@admin.register(StudentProject)
class StudentProjectAdmin(admin.ModelAdmin):
    list_display = (
        "creator_id",
        "organisation",
        "level",
        "title",
        "type",
        "active",
        "status",
        "created_at",
        "updated_at",
    )


@admin.register(ExternalProject)
class ExternalProjectAdmin(admin.ModelAdmin):
    list_display = (
        "creator_id",
        "time_budget",
        "monetary_budget",
        "title",
        "type",
        "active",
        "status",
        "created_at",
        "updated_at",
    )


@admin.register(CoreFunctionProject)
class CoreFunctionProjectAdmin(admin.ModelAdmin):
    list_display = (
        "creator_id",
        "title",
        "type",
        "active",
        "status",
        "created_at",
        "updated_at",
    )
