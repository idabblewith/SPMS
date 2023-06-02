from django.contrib import admin

# Register your models here.
from .models import ARARReport


@admin.register(ARARReport)
class ARARReportAdmin(admin.ModelAdmin):
    list_display = ("year",)
