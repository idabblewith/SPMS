from django.contrib import admin
from .models import EntityContact, BranchContact, UserContact, Address


@admin.register(EntityContact)
class EntityContactAdmin(admin.ModelAdmin):
    list_display = [
        # "entity_id__name",
        "entity_id",
        "email",
    ]

    list_filter = ["entity_id__key_stakeholder"]

    search_fields = [
        "entity_id__name",
    ]


@admin.register(BranchContact)
class BranchContactAdmin(admin.ModelAdmin):
    list_display = [
        "branch_id",
        # "branch_id__name",
        "email",
    ]

    list_filter = ["branch_id__manager"]

    search_fields = [
        # "branch_id",
        "branch_id__name",
    ]


@admin.register(UserContact)
class UserContactAdmin(admin.ModelAdmin):
    list_display = [
        "user_id",
        "email",
    ]

    list_filter = ["user_id__username"]

    search_fields = [
        # "user_id",
        "user_id__first_name",
    ]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "street",
        "state",
        "country",
    ]

    list_filter = [
        "state",
        "country",
    ]

    search_fields = ["street"]
