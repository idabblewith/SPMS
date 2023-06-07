from django.db import models
from common.models import CommonModel


class Quote(CommonModel):
    """Definition for Quotes"""

    text = models.TextField(unique=True)
    author = models.CharField(max_length=50)

    # def reports(self):
    #     try:
    #         return QuoteReport.objects.filter(quote=self.pk).count()
    #     except QuoteReport.DoesNotExist:
    #         return 0

    def __str__(self) -> str:
        return f"{self.pk} | {self.text}"

    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"


class QuoteReport(CommonModel):
    """Definition for Quote Reports"""

    class ReportReasons(models.TextChoices):
        offensive = "offensive", "Offensive"
        error = "error", "Error"
        incorrect = "incorrect", "Incorrect"

    reporter = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="reported_quotes",
    )
    quote = models.ForeignKey(
        "quotes.Quote",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reports",
    )
    reason = models.CharField(
        max_length=20,
        choices=ReportReasons.choices,
    )
    details = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"Quote Report | {self.reporter__username}"

    class Meta:
        verbose_name = "Quote Report"
        verbose_name_plural = "Quote Reports"
