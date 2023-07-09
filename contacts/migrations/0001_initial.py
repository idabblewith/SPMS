# Generated by Django 4.2.2 on 2023-07-08 02:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("street", models.CharField(max_length=140)),
                ("suburb", models.CharField(blank=True, max_length=140, null=True)),
                ("city", models.CharField(max_length=140)),
                ("zipcode", models.IntegerField()),
                ("state", models.CharField(max_length=140)),
                ("country", models.CharField(max_length=140)),
                ("pobox", models.CharField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Addresses",
            },
        ),
        migrations.CreateModel(
            name="AgencyContact",
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
                ("phone", models.CharField(max_length=20)),
                ("alt_phone", models.CharField(max_length=20)),
                ("fax", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name": "agency Contact",
                "verbose_name_plural": "agency Contacts",
            },
        ),
        migrations.CreateModel(
            name="BranchContact",
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
                ("fax", models.CharField(max_length=20)),
            ],
            options={
                "verbose_name": "Branch Contact",
                "verbose_name_plural": "Branch Contacts",
            },
        ),
        migrations.CreateModel(
            name="UserContact",
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
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, unique=True
                    ),
                ),
                ("phone", models.CharField(blank=True, max_length=20, null=True)),
                ("alt_phone", models.CharField(blank=True, max_length=20, null=True)),
                ("fax", models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                "verbose_name": "User Contact",
                "verbose_name_plural": "User Contacts",
            },
        ),
    ]
