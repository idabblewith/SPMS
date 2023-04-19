from django.contrib import admin
from .models import BusinessArea


@admin.register(BusinessArea)
class BusinessAreaAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "effective_from",
        "creator_id",
        "created_at",
        "updated_at",
    )
