from django.contrib import admin
from .models import Entity, Branch, BusinessArea, Division, ResearchFunction


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "key_stakeholder",
    ]

    list_filter = ["key_stakeholder"]

    search_fields = [
        "name",
    ]


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "manager",
    ]

    list_filter = ["manager"]

    search_fields = [
        "name",
    ]


@admin.register(BusinessArea)
class BusinessAreaAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "focus",
        "leader",
    ]

    list_filter = ["leader"]

    search_fields = [
        "name",
        "focus",
    ]


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "approver",
        "director",
    ]

    list_filter = [
        "approver",
        "director",
    ]

    search_fields = ["name"]


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
