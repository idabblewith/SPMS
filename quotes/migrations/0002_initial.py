# Generated by Django 4.2.2 on 2023-07-04 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("quotes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="quotereport",
            name="reporter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reported_quotes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
