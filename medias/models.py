from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    """
    Model Definition for Photos

    null,blank=True allows users to decide where the project belongs (busarea/project)
    """

    file = models.URLField()
    description = models.CharField(max_length=100)
    uploader = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="photos_uploaded",
    )
    category = models.ForeignKey(
        "categories.ProjectCategory",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    business_area = models.ForeignKey(
        "classifications.BusinessArea",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    science_project = models.ForeignKey(
        "projects.ScienceProject",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    external_project = models.ForeignKey(
        "projects.ExternalProject",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    student_project = models.ForeignKey(
        "projects.StudentProject",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    core_function_project = models.ForeignKey(
        "projects.CoreFunctionProject",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self) -> str:
        return "Photo File"


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
