# Generated by Django 4.2.2 on 2023-07-09 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("quotes", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
