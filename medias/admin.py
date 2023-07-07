from django.contrib import admin
from .models import (
    ReportPDF,
    AnnualReportImage,
    BusinessAreaPhoto,
    UserAvatar,
    ProjectPhoto,
    AgencyImage,
)


@admin.register(ReportPDF)
class ReportPDFAdmin(admin.ModelAdmin):
    list_display = [
        "year",
        "file",
    ]


@admin.register(AnnualReportImage)
class AnnualReportImageAdmin(admin.ModelAdmin):
    list_display = [
        "year",
        "kind",
        "file",
        "uploader",
    ]


@admin.register(BusinessAreaPhoto)
class BusinessAreaPhotoAdmin(admin.ModelAdmin):
    list_display = (
        "business_area",
        "file",
        "uploader",
    )


@admin.register(ProjectPhoto)
class ProjectPhotoAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "file",
        "uploader",
    )


@admin.register(AgencyImage)
class AgencyImageAdmin(admin.ModelAdmin):
    list_display = (
        "agency",
        "file",
    )


@admin.register(UserAvatar)
class UserAvatarAdmin(admin.ModelAdmin):
    list_display = (
        "file",
        "user",
    )
