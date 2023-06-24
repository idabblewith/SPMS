# Generated by Django 4.2.2 on 2023-06-23 13:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Agency",
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
                ("name", models.CharField(max_length=140)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Agency",
                "verbose_name_plural": "Agencies",
            },
        ),
        migrations.CreateModel(
            name="Branch",
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
                ("old_id", models.IntegerField()),
                ("name", models.CharField(max_length=140)),
            ],
            options={
                "verbose_name": "Branch",
                "verbose_name_plural": "Branches",
            },
        ),
        migrations.CreateModel(
            name="BusinessArea",
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
                ("name", models.CharField(max_length=140)),
                (
                    "slug",
                    models.SlugField(
                        help_text="A URL-sage acronym of the BA's name without whitespace"
                    ),
                ),
                ("published", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("cost_center", models.IntegerField(blank=True, null=True)),
                ("old_leader_id", models.IntegerField(blank=True, null=True)),
                ("old_finance_admin_id", models.IntegerField(blank=True, null=True)),
                ("old_data_custodian_id", models.IntegerField(blank=True, null=True)),
                ("focus", models.CharField(max_length=1250)),
                ("introduction", models.TextField()),
            ],
            options={
                "verbose_name": "Business Area",
                "verbose_name_plural": "Business Areas",
            },
        ),
        migrations.CreateModel(
            name="Division",
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
                ("name", models.CharField(max_length=150)),
                (
                    "slug",
                    models.SlugField(
                        help_text="A URL-sage acronym of the Division's name without whitespace"
                    ),
                ),
                ("old_id", models.IntegerField()),
                ("old_director_id", models.IntegerField()),
            ],
            options={
                "verbose_name": "Derpartment Division",
                "verbose_name_plural": "Department Divisions",
            },
        ),
        migrations.CreateModel(
            name="ResearchFunction",
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
                ("name", models.CharField(max_length=150)),
                ("description", models.TextField(blank=True)),
                (
                    "association",
                    models.TextField(
                        blank=True,
                        help_text="The research function's association with departmental programs/divisions.",
                        null=True,
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        default=True,
                        help_text="Whether this research function has been deprecated or not.",
                    ),
                ),
            ],
            options={
                "verbose_name": "Research Function",
                "verbose_name_plural": "Research Functions",
            },
        ),
    ]
