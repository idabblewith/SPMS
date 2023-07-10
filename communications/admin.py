from django.contrib import admin
from .models import (
    ProjectDocumentComment,
    DirectMessage,
    DirectMessageReaction,
    CommentReaction,
    ChatRoom,
)


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "created_at",
        "updated_at",
    ]

    list_filter = [
        "created_at",
    ]

    search_fields = [
        "user__username",
    ]
    pass


@admin.register(ProjectDocumentComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        # "category",
        "document",
        "text",
        "created_at",
        "is_public",
        "is_removed",
    ]

    list_filter = [
        "is_public",
        "is_removed",
    ]

    search_fields = [
        "text",
        "user__username",
    ]


@admin.register(CommentReaction)
class CommentReactionAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "comment",
    ]

    # list_filter = [
    #     "comment__category",
    # ]

    search_fields = [
        "comment__text",
        "user__username",
    ]


@admin.register(DirectMessage)
class DirectMessageAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "chat_room",
        "text",
        "ip_address",
    ]

    list_filter = [
        "is_public",
    ]

    search_fields = [
        "text",
        "user__username",
        "ip_address",
    ]


@admin.register(DirectMessageReaction)
class DirectMessageReactionAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "direct_message",
    ]

    # list_filter = [
    #     "is_public",
    #     "category",
    # ]

    search_fields = [
        "direct_message__text",
        "user__username",
    ]
