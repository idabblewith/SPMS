from django.contrib import admin
from .models import BusinessArea, Division, ResearchFunction


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
