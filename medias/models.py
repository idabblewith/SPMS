from django.db import models
from common.models import CommonModel


# Images are separated into relevant tables, as opposed to one big 'Photos' table.

# ARAR


class ARARPDF(CommonModel):
    """
    Model Definition for the actual Report PDF
    """

    file = models.URLField()
    year = models.DateField()
    uploader = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="generated_pdfs",
    )


class CoverPage(CommonModel):

    """
    Model Definition for the ARAR Front Page Cover (Provided by Graphic Designers in A4) for the year
    """

    file = models.URLField()
    year = models.DateField()
    uploader = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="front_covers_uploaded",
    )


class ServiceDeliveryImage(CommonModel):
    """
    Model Definition for the ARAR Service Delivery Image for the year

    """

    file = models.URLField()
    year = models.DateField()
    uploader = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="service_delivery_images_uploaded",
    )


class PartnershipsImage(CommonModel):
    """
    Model Definition for the ARAR Partnerships Image for the year

    """

    file = models.URLField()
    year = models.DateField()
    uploader = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="partnership_images_uploaded",
    )


class StudentProjectsImage(CommonModel):
    """
    Model Definition for the ARAR Student Projects Image for the year

    """

    file = models.URLField()
    year = models.DateField()
    uploader = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="student_project_images_uploaded",
    )


class StudentReportsImage(CommonModel):
    """
    Model Definition for the ARAR Student Reports Image for the year

    """

    file = models.URLField()
    year = models.DateField()
    uploader = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="student_report_images_uploaded",
    )


class PublicationsImage(CommonModel):
    """
    Model Definition for the ARAR Publications Image for the year

    """

    file = models.URLField()
    year = models.DateField()
    uploader = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="publication_images_uploaded",
    )


class RearPage(CommonModel):

    """
    Model Definition for Rear Page Cover (Provided by Graphic Designers in A4)
    """

    file = models.URLField()
    year = models.DateField()
    uploader = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="rear_covers_uploaded",
    )


class BusinessAreaPhoto(CommonModel):

    """
    Model Definition for BusinessArea Photos
    """

    file = models.URLField()
    year = models.DateField()
    business_area = models.ForeignKey(
        "classifications.BusinessArea",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="photos",
    )
    uploader = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="business_area_photos_uploaded",
    )


# class Photo(CommonModel):
#     """
#     Model Definition for Photos

#     null,blank=True allows users to decide where the project belongs (busarea/project)
#     """

#     file = models.URLField()
#     description = models.CharField(max_length=100)
#     uploader = models.ForeignKey(
#         "users.User",
#         on_delete=models.CASCADE,
#         blank=True,
#         null=True,
#         related_name="photos_uploaded",
#     )
#     category = models.ForeignKey(
#         "categories.ProjectCategory",
#         on_delete=models.SET_NULL,
#         blank=True,
#         null=True,
#     )
#     business_area = models.ForeignKey(
#         "classifications.BusinessArea",
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         related_name="photos",
#     )

#     science_project = models.ForeignKey(
#         "projects.ScienceProject",
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         related_name="photos",
#     )

#     external_project = models.ForeignKey(
#         "projects.ExternalProject",
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         related_name="photos",
#     )

#     student_project = models.ForeignKey(
#         "projects.StudentProject",
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         related_name="photos",
#     )

#     core_function_project = models.ForeignKey(
#         "projects.CoreFunctionProject",
#         on_delete=models.CASCADE,
#         null=True,
#         blank=True,
#         related_name="photos",
#     )

#     core_function_project = models.ForeignKey(
#         "reports.ARARReport",
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="photos",
#     )

#     def __str__(self) -> str:
#         return "Photo File"


# class Video(CommonModel):
#     """
#     Model Definition for Videos

#     """

#     file = models.URLField()
#     project = models.OneToOneField(
#         "projecs.BaseProject",
#         on_delete=models.CASCADE,
#         related_name="videos",
#     )

#     def __str__(self) -> str:
#         return "Video File"
