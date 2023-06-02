from django.db import models

from common.models import CommonModel
from django.core.validators import MinValueValidator


class ARARReport(CommonModel):
    """
    The Annual Research Report.

    There can only be one ARR per year, enforced with a `unique` year.
    """

    pdf = models.ForeignKey(
        "medias.ARARPDF",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        editable=False,
        help_text="The PDF file generated for the report.",
    )

    year = models.DateField(
        verbose_name="Report Year",
        help_text=(
            "The publication year of this report with four digits, e.g. 2014 for the ARAR 2013-2014"
        ),
        unique=True,
        validators=[MinValueValidator(2013)],  # Set to Date Value instead of int
    )

    divisions = models.ForeignKey(
        "classifications.Division",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="reports",
        help_text="Divisions included in this report",
    )

    dm = models.TextField(
        verbose_name="Director's Message",
        blank=True,
        null=True,
        help_text="Directors's message (less than 10,000 words)",
    )

    coverpage = models.ForeignKey(
        "medias.CoverPage",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="The cover page for the document",
    )

    rearcoverpage = models.ForeignKey(
        "medias.RearPage",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="The back page for the document",
    )

    # sds_chapter_image = models.ForeignKey(
    #     "medias.Photo",
    #     blank=True,
    #     null=True,
    #     size=[2480, 1240],
    #     help_text="",
    # )

    service_delivery_intro = models.TextField(
        verbose_name="Service Deilvery Structure",
        blank=True,
        null=True,
        help_text="Introductory paragraph for the Science Delivery Structure section in the ARAR",
    )

    # Previously sds_orgchart
    service_delivery_chart = models.ForeignKey(
        "medias.ServiceDeliveryImage",
        on_delete=models.SET_NULL,
        # size=[2480, 2480],
        blank=True,
        null=True,
        help_text="The 'Service Delivery Structure' page image (2480pt, 2480pt).",
    )

    def __str__(self) -> str:
        return f"ARAR - {self.year}"

    class Meta:
        verbose_name_plural = "ARAR Reports"

    # research_chapterimage = ResizedImageField(
    #     upload_to=reports_upload_to,
    #     blank=True, null=True,
    #     size=[2480, 1240],
    #     help_text=_(
    #         "Upload a chapter image for the Summary of Research projects."
    #         " Aim for a visually quiet, low contrast image."
    #         " The horizon, if shown, should be in the top third and level."
    #         " The aspect ratio (width to height) must be 2:1."
    #         " The image will be resized to max 2480 (wt) x 1240 pt (ht)."
    #     )
    # )

    # research_intro = models.TextField(
    #     verbose_name=_("Research Activities Introduction"),
    #     blank=True, null=True,
    #     help_text=_("Introduction paragraph for the Research Activity section "
    #                 "in the ARAR"))

    # partnerships_chapterimage = ResizedImageField(
    #     upload_to=reports_upload_to,
    #     blank=True, null=True,
    #     size=[2480, 1240],
    #     help_text=_(
    #         "Upload a chapter image for the External Partnerships chapter."
    #         " Aim for a visually quiet, low contrast image."
    #         " The horizon, if shown, should be in the top third and level."
    #         " The aspect ratio (width to height) must be 2:1."
    #         " The image will be resized to max 2480 (wt) x 1240 pt (ht)."
    #     )
    # )

    # collaboration_chapterimage = ResizedImageField(
    #     upload_to=reports_upload_to,
    #     blank=True, null=True,
    #     size=[2480, 1240],
    #     help_text=_(
    #         "Upload a chapter image for the Collab with Academia summary."
    #         " Aim for a visually quiet, low contrast image."
    #         " The horizon, if shown, should be in the top third and level."
    #         " The aspect ratio (width to height) must be 2:1."
    #         " The image will be resized to max 2480 (wt) x 1240 pt (ht)."
    #     )
    # )

    # studentprojects_chapterimage = ResizedImageField(
    #     upload_to=reports_upload_to,
    #     blank=True, null=True,
    #     size=[2480, 1240],
    #     help_text=_(
    #         "Upload a chapter image for the Student Projects chapter."
    #         " Aim for a visually quiet, low contrast image."
    #         " The horizon, if shown, should be in the top third and level."
    #         " The aspect ratio (width to height) must be 2:1."
    #         " The image will be resized to max 2480 (wt) x 1240 pt (ht)."
    #     )
    # )

    # student_intro = models.TextField(
    #     verbose_name=_("Student Projects Introduction"),
    #     blank=True, null=True,
    #     help_text=_("Introduction paragraph for the Student Projects section "
    #                 "in the ARAR"))

    # publications_chapterimage = ResizedImageField(
    #     upload_to=reports_upload_to,
    #     blank=True, null=True,
    #     size=[2480, 1240],
    #     help_text=_(
    #         "Upload a chapter image for the Publications chapter."
    #         " Aim for a visually quiet, low contrast image."
    #         " The horizon, if shown, should be in the top third and level."
    #         " The aspect ratio (width to height) must be 2:1."
    #         " The image will be resized to max 2480 (wt) x 1240 pt (ht)."
    #     )
    # )

    # pub = models.TextField(
    #     verbose_name=_("Publications and Reports"),
    #     blank=True, null=True,
    #     help_text=_("The Publications go here, Lisa!"))

    # date_open = models.DateField(
    #     verbose_name=_("Open for submissions"),
    #     help_text=_("Date from which this ARAR report can be updated."))

    # date_closed = models.DateField(
    #     verbose_name=_("Closed for submissions"),
    #     help_text=_("The cut-off date for any changes."))

    # pdf = models.FileField(
    #     upload_to=reports_upload_to,
    #     blank=True, null=True,
    #     editable=False,
    #     help_text="The latest, greatest and PDFest version of all times")

    # class Meta:
    #     """Class opts."""

    #     app_label = 'pythia'
    #     get_latest_by = 'date_open'  # 'created'
    #     verbose_name = 'Annual Report'
    #     verbose_name_plural = 'Annual Reports'

    # def __str__(self):
    #     """The report name."""
    #     return "Annual Report {0}-{1}".format(
    #         self.year - 1, self.year)
