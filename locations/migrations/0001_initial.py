# Generated by Django 4.2.2 on 2023-07-09 07:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Area",
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
                    "name",
                    models.CharField(
                        help_text="A human-readable, short but descriptive name.",
                        max_length=150,
                    ),
                ),
                (
                    "area_type",
                    models.CharField(
                        choices=[
                            ("dbcaregion", "DBCA Region"),
                            ("dbcadistrict", "DBCA District"),
                            (
                                "ibra",
                                "IBRA Region (Interim Biogeographic Regionalisation for Australia)",
                            ),
                            (
                                "imcra",
                                "IMCRA Region (Integrated Marine and Coastal Regionalisation of Australia)",
                            ),
                            ("nrm", "Natural Resource Management Region"),
                        ],
                        max_length=25,
                        verbose_name="Area Type",
                    ),
                ),
                ("old_id", models.IntegerField()),
            ],
            options={
                "verbose_name": "Area",
                "verbose_name_plural": "Areas",
            },
        ),
    ]
