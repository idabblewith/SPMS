from django.contrib import admin
from .models import Photo


@admin.register(Photo)
class MediaAdmin(admin.ModelAdmin):
    list_display = (
        "file",
        "business_area",
        "external_project",
        "student_project",
        "core_function_project",
        "created_at",
        "updated_at",
    )
