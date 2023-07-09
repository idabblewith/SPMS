# Generated by Django 4.2.2 on 2023-07-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AgencyImage",
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
                ("file", models.URLField()),
            ],
            options={
                "verbose_name": "Agency Image",
                "verbose_name_plural": "Agency Images",
            },
        ),
        migrations.CreateModel(
            name="AnnualReportImage",
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
                ("file", models.URLField()),
                ("year", models.PositiveIntegerField()),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("cover", "Cover"),
                            ("rear_cover", "Rear Cover"),
                            ("sdchart", "Service Delivery Chart"),
                            ("service_delivery", "Service Delivery"),
                            ("research", "Research"),
                            ("partnerships", "Partnerships"),
                            ("collaborations", "Collaborations"),
                            ("student_projects", "Student Projects"),
                            ("publications", "Publications"),
                        ],
                        max_length=140,
                    ),
                ),
            ],
            options={
                "verbose_name": "Annual Reoprt Image",
                "verbose_name_plural": "Annual Reoprt Images",
            },
        ),
        migrations.CreateModel(
            name="BusinessAreaPhoto",
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
                ("file", models.URLField()),
            ],
            options={
                "verbose_name": "Business Area Image",
                "verbose_name_plural": "Business Area Images",
            },
        ),
        migrations.CreateModel(
            name="ProjectPhoto",
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
                ("file", models.URLField()),
            ],
            options={
                "verbose_name": "Project Image",
                "verbose_name_plural": "Project Images",
            },
        ),
        migrations.CreateModel(
            name="ReportPDF",
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
                ("file", models.URLField()),
                ("year", models.DateField()),
            ],
            options={
                "verbose_name": "ARAR PDF",
                "verbose_name_plural": "ARAR PDFs",
            },
        ),
        migrations.CreateModel(
            name="UserAvatar",
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
                ("file", models.URLField()),
            ],
            options={
                "verbose_name": "User Avatar Image",
                "verbose_name_plural": "User Avatar Images",
            },
        ),
    ]
