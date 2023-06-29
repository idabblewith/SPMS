# Generated by Django 4.2.2 on 2023-06-29 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Quote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("text", models.TextField(unique=True)),
                ("author", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Quote",
                "verbose_name_plural": "Quotes",
            },
        ),
        migrations.CreateModel(
            name="QuoteReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "reason",
                    models.CharField(
                        choices=[
                            ("offensive", "Offensive"),
                            ("error", "Error"),
                            ("incorrect", "Incorrect"),
                        ],
                        max_length=20,
                    ),
                ),
                ("details", models.TextField(blank=True, null=True)),
                (
                    "quote",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reports",
                        to="quotes.quote",
                    ),
                ),
            ],
            options={
                "verbose_name": "Quote Report",
                "verbose_name_plural": "Quote Reports",
            },
        ),
    ]
