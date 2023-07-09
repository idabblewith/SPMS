from django.contrib import admin

# Register your models here.
from .models import AnnualReport


@admin.register(AnnualReport)
class AnnualReportAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "year",
        # "pdf",
    )

    ordering = ["year"]
