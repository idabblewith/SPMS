from django.db import models
from common.models import CommonModel


# Images are separated into relevant tables, as opposed to one big 'Photos' table.

# ARAR


class ReportPDF(CommonModel):
    """
    Model Definition for the actual Report PDF
    """

    file = models.URLField()
    year = models.DateField()

    def __str__(self) -> str:
        return f"{self.year} ARAR PDF"

    class Meta:
        verbose_name = "ARAR PDF"
        verbose_name_plural = "ARAR PDFs"


class AnnualReportImage(CommonModel):
    class ImageTypes(models.TextChoices):
        COVER = "cover", "Cover"
        REAR_COVER = "rear_cover", "Rear Cover"
        SDCHART = "sdchart", "Service Delivery Chart"
        SDCHAPTER = "service_delivery", "Service Delivery"
        RESEARCHCHAPTER = "research", "Research"
        PARTNERSHIPSCHAPTER = "partnerships", "Partnerships"
        COLLABORATIONSCHAPTER = "collaborations", "Collaborations"
        STUDENTPROJECTSCHAPTER = "student_projects", "Student Projects"
        PUBLICATIONSCHAPTER = "publications", "Publications"

    file = models.URLField()
    year = models.PositiveIntegerField()
    kind = models.CharField(
        max_length=140,
        choices=ImageTypes.choices,
    )
    uploader = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="annual_report_images_uploaded",
    )

    def __str__(self) -> str:
        return f"({self.year}) {self.kind.capitalize} Annual Report Image"

    class Meta:
        verbose_name = "Annual Reoprt Image"
        verbose_name_plural = "Annual Reoprt Images"


class BusinessAreaPhoto(CommonModel):

    """
    Model Definition for BusinessArea Photos
    """

    file = models.URLField()
    business_area = models.ForeignKey(
        "agencies.BusinessArea",
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


# Includes student projects
class ProjectPhoto(CommonModel):
    """
    Model Definition for Project Photos
    """

    file = models.URLField()
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        # blank=True,
        # null=True,
        related_name="image",
    )
    uploader = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="project_photos_uploaded",
    )

    def __str__(self) -> str:
        return "Project Photo File"

    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"


class AgencyImage(CommonModel):
    """
    Model Definition for Agency Photos (DBCA's image)
    """

    file = models.URLField()
    agency = models.ForeignKey(
        "agencies.Agency",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="image",
    )

    def __str__(self) -> str:
        return "Agency Photo File"

    class Meta:
        verbose_name = "Agency Image"
        verbose_name_plural = "Agency Images"


class UserAvatar(CommonModel):
    """
    Model Definition for User Photos
    """

    file = models.URLField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="avatar",
    )

    def __str__(self) -> str:
        return "User Photo File"

    class Meta:
        verbose_name = "User Avatar Image"
        verbose_name_plural = "User Avatar Images"
