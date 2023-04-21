from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "category",
        "payload",
        "created_at",
        "is_public",
    ]

    list_filter = [
        "is_public",
        "category",
    ]

    search_fields = [
        "payload",
        "user__username",
    ]
