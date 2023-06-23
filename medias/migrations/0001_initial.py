# Generated by Django 4.2.2 on 2023-06-23 02:33

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
            name="ARARPDF",
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
            name="CoverPage",
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
                "verbose_name": "Cover Page",
                "verbose_name_plural": "Cover Pages",
            },
        ),
        migrations.CreateModel(
            name="PartnershipsImage",
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
                "verbose_name": "Partnership Image",
                "verbose_name_plural": "Partnership Images",
            },
        ),
        migrations.CreateModel(
            name="PublicationsImage",
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
                "verbose_name": "Publications Image",
                "verbose_name_plural": "Publications Images",
            },
        ),
        migrations.CreateModel(
            name="RearPage",
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
                "verbose_name": "Rear Page Image",
                "verbose_name_plural": "Rear Page Images",
            },
        ),
        migrations.CreateModel(
            name="ServiceDeliveryImage",
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
                "verbose_name": "Service Delivery Image",
                "verbose_name_plural": "Service Delivery Images",
            },
        ),
        migrations.CreateModel(
            name="StudentProjectsImage",
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
                "verbose_name": "Student Projects Image",
                "verbose_name_plural": "Student Projects Images",
            },
        ),
        migrations.CreateModel(
            name="StudentReportsImage",
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
                "verbose_name": "Student Reports Image",
                "verbose_name_plural": "Student Reports Images",
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
