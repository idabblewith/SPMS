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

    def __str__(self) -> str:
        return f"{self.year} ARAR PDF"

    class Meta:
        verbose_name = "ARAR PDF"
        verbose_name_plural = "ARAR PDFs"


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

    def __str__(self) -> str:
        return "CoverPage Photo File"

    class Meta:
        verbose_name = "Cover Page"
        verbose_name_plural = "Cover Pages"


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

    def __str__(self) -> str:
        return "ServiceDelivery Photo File"

    class Meta:
        verbose_name = "Service Delivery Image"
        verbose_name_plural = "Service Delivery Images"


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

    def __str__(self) -> str:
        return "Partnerships Photo File"

    class Meta:
        verbose_name = "Partnership Image"
        verbose_name_plural = "Partnership Images"


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

    def __str__(self) -> str:
        return "StudentProjects Photo File"

    class Meta:
        verbose_name = "Student Projects Image"
        verbose_name_plural = "Student Projects Images"


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

    def __str__(self) -> str:
        return "StudentReports Photo File"

    class Meta:
        verbose_name = "Student Reports Image"
        verbose_name_plural = "Student Reports Images"


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

    def __str__(self) -> str:
        return "Publications Photo File"

    class Meta:
        verbose_name = "Publications Image"
        verbose_name_plural = "Publications Images"


class RearPage(CommonModel):

    """
    Model Definition for Rear Page Cover for the year (Provided by Graphic Designers in A4)
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

    def __str__(self) -> str:
        return "RearPage Photo File"

    class Meta:
        verbose_name = "Rear Page Image"
        verbose_name_plural = "Rear Page Images"


class BusinessAreaPhoto(CommonModel):

    """
    Model Definition for BusinessArea Photos
    """

    file = models.URLField()
    business_area = models.ForeignKey(
        "entities.BusinessArea",
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

    def __str__(self) -> str:
        return "Business Area Photo File"

    class Meta:
        verbose_name = "Business Area Image"
        verbose_name_plural = "Business Area Images"


class UserAvatar(CommonModel):
    """
    Model Definition for User Photos
    """

    file = models.URLField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="avatar",
    )

    def __str__(self) -> str:
        return "User Photo File"

    class Meta:
        verbose_name = "User Avatar Image"
        verbose_name_plural = "User Avatar Images"
