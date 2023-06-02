from django.contrib import admin
from .models import (
    ARARPDF,
    CoverPage,
    ServiceDeliveryImage,
    PartnershipsImage,
    StudentProjectsImage,
    StudentReportsImage,
    PublicationsImage,
    RearPage,
    BusinessAreaPhoto,
)

display_tuple = (
    "file",
    "year",
    "uploader",
)


@admin.register(ARARPDF)
class ARARPDFAdmin(admin.ModelAdmin):
    list_display = display_tuple


@admin.register(CoverPage)
class CoverPageAdmin(admin.ModelAdmin):
    list_display = display_tuple


@admin.register(ServiceDeliveryImage)
class ServiceDeliveryImageAdmin(admin.ModelAdmin):
    list_display = display_tuple


@admin.register(PartnershipsImage)
class PartnershipsImageAdmin(admin.ModelAdmin):
    list_display = display_tuple


@admin.register(StudentProjectsImage)
class StudentProjectsImageAdmin(admin.ModelAdmin):
    list_display = display_tuple


@admin.register(StudentReportsImage)
class StudentReportsImageAdmin(admin.ModelAdmin):
    list_display = display_tuple


@admin.register(PublicationsImage)
class PublicationsImageAdmin(admin.ModelAdmin):
    list_display = display_tuple


@admin.register(RearPage)
class RearPageAdmin(admin.ModelAdmin):
    list_display = display_tuple


@admin.register(BusinessAreaPhoto)
class BusinessAreaPhotoAdmin(admin.ModelAdmin):
    list_display = (
        "file",
        "year",
        "business_area",
        "uploader",
    )


# @admin.register(Photo)
# class MediaAdmin(admin.ModelAdmin):
#     list_display = (
#         "file",
#         "business_area",
#         "external_project",
#         "student_project",
#         "core_function_project",
#         "created_at",
#         "updated_at",
#     )
