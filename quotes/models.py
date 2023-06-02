from django.db import models
from common.models import CommonModel


class Quote(CommonModel):
    """Definition for Quotes"""

    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

    text = models.TextField(unique=True)
    author = models.CharField(max_length=50)

    # def reports(self):
    #     try:
    #         return QuoteReport.objects.filter(quote=self.pk).count()
    #     except QuoteReport.DoesNotExist:
    #         return 0

    def __str__(self) -> str:
        return f"{self.pk} | {self.text}"


class QuoteReport(CommonModel):
    """Definition for Quote Reports"""

    class Meta:
        verbose_name = "Quote Report"
        verbose_name_plural = "Quote Reports"

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
