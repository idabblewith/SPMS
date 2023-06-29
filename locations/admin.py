from django.contrib import admin
from .models import ProjectArea


@admin.register(ProjectArea)
class ProjectAreaAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "area_type",
        "old_id",
    ]

    list_filter = ["area_type"]

    search_fields = [
        "name",
        # "area_type",
    ]
