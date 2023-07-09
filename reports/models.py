from django.db import models

from common.models import CommonModel
from django.core.validators import MinValueValidator


# Renamed from ARARReport
class AnnualReport(CommonModel):
    """
    The Annual Research Report.

    There can only be one ARR per year, enforced with a `unique` year.
    """

    # NOT IN TABLE
    # divisions = models.ManyToManyField(
    #     "agencies.Division",
    #     # on_delete=models.SET_NULL,
    #     blank=True,
    #     # null=True,
    #     related_name="reports_in",
    #     help_text="Divisions included in this report",
    # )

    old_id = models.IntegerField()

    creator = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        related_name="created_reports",
        blank=True,
        null=True,
    )
    modifier = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        related_name="modified_reports",
        blank=True,
        null=True,
    )

    year = models.PositiveIntegerField(
        verbose_name="Report Year",
        help_text=(
            "The publication year of this report with four digits, e.g. 2014 for the ARAR 2013-2014"
        ),
        unique=True,
        validators=[
            MinValueValidator(2013)
        ],  # Potentially Set to Date Value instead of int
    )

    dm = models.TextField(
        verbose_name="Director's Message",
        blank=True,
        null=True,
        help_text="Directors's message (less than 10,000 words)",
    )

    # sds_intro
    service_delivery_intro = models.TextField(
        verbose_name="Service Deilvery Structure",
        blank=True,
        null=True,
        help_text="Introductory paragraph for the Science Delivery Structure section in the ARAR",
    )

    research_intro = models.TextField(
        verbose_name="Research Activities Intro",
        blank=True,
        null=True,
        help_text="Introduction paragraph for the Research Activity section in the ARAR",
    )

    student_intro = models.TextField(
        verbose_name="Student Projects Introduction",
        blank=True,
        null=True,
        help_text="Introduction paragraph for the Student Projects section in the ARAR",
    )

    # pub
    publications = models.TextField(
        blank=True,
        null=True,
        verbose_name="Publications and Reports",
        help_text="Publications for the year",
    )

    date_open = models.DateField(
        help_text="The date at which submissions are opened for this report",
    )

    date_closed = models.DateField(
        help_text="The date at which submissions are closed for this report",
    )

    # pdf = models.ForeignKey(
    #     "medias.ReportPDF",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     editable=False,
    #     help_text="The PDF file generated for the report.",
    # )
    # coverpage
    # cover_page = models.ForeignKey(
    #     "medias.AnnualReportImage",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     help_text="The cover page for the document",
    #     related_name="cover_page",
    # )

    # # rearcoverpage
    # rear_cover_page = models.ForeignKey(
    #     "medias.AnnualReportImage",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     help_text="The back page for the document",
    #     related_name="rear_cover_page",
    # )

    # # sds_chapterimage (service_delivery_structure)
    # sds_chapter_image = models.ForeignKey(
    #     "medias.AnnualReportImage",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="sds_chapter_image",
    # )

    # # Previously sds_orgchart
    # service_delivery_chart = models.ForeignKey(
    #     "medias.AnnualReportImage",
    #     on_delete=models.SET_NULL,
    #     # size=[2480, 2480],
    #     blank=True,
    #     null=True,
    #     help_text="The 'Service Delivery Structure' page image (2480pt, 2480pt).",
    #     related_name="service_delivery_chart",
    # )

    # # research_chapterimage
    # research_chapter_image = models.ForeignKey(
    #     "medias.AnnualReportImage",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="research_chapter_image",
    # )

    # # partnerships_chapterimage
    # partnerships_chapter_image = models.ForeignKey(
    #     "medias.AnnualReportImage",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="partnerships_chapter_image",
    # )

    # # collaborations_chapterimage
    # collaborations_chapter_image = models.ForeignKey(
    #     "medias.AnnualReportImage",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="collaborations_chapter_image",
    # )

    # # studentprojects_chapterimage
    # studentprojects_chapter_image = models.ForeignKey(
    #     "medias.AnnualReportImage",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="student_projects_chapter_image",
    # )

    # # publications_chapterimage
    # publications_chapter_image = models.ForeignKey(
    #     "medias.AnnualReportImage",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="publications_chapter_image",
    # )

    def __str__(self) -> str:
        return f"ARAR - {self.year}"

    class Meta:
        verbose_name = "Annual Report"
        verbose_name_plural = "Annual Reports"
