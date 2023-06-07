# Generated by Django 4.2 on 2023-06-07 00:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CoreFunctionProject",
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
                ("title", models.CharField(max_length=200)),
                ("tagline", models.CharField(max_length=200)),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Describe the project in one to three paragraphs.",
                        null=True,
                        verbose_name="Project Description",
                    ),
                ),
                ("keywords", models.CharField(max_length=300)),
                ("active", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("pending", "Pending Project Plan"),
                            ("active", "Active (Approved)"),
                            ("updating", "Update Requested"),
                            ("closure_requested", "Closure Requested"),
                            ("closing", "Closure Pending Final Update"),
                            ("final_update", "Final Update Requested"),
                            ("completed", "Completed and Closed"),
                            ("terminated", "Terminated and Closed"),
                            ("suspended", "Suspended"),
                        ],
                        default="new",
                        max_length=50,
                    ),
                ),
                ("effective_from", models.DateField()),
                ("effective_to", models.DateField()),
            ],
            options={
                "verbose_name": "Core Function",
                "verbose_name_plural": "Core Functions",
            },
        ),
        migrations.CreateModel(
            name="ExternalProject",
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
                ("title", models.CharField(max_length=200)),
                ("tagline", models.CharField(max_length=200)),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Describe the project in one to three paragraphs.",
                        null=True,
                        verbose_name="Project Description",
                    ),
                ),
                ("keywords", models.CharField(max_length=300)),
                ("active", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("pending", "Pending Project Plan"),
                            ("active", "Active (Approved)"),
                            ("updating", "Update Requested"),
                            ("closure_requested", "Closure Requested"),
                            ("closing", "Closure Pending Final Update"),
                            ("final_update", "Final Update Requested"),
                            ("completed", "Completed and Closed"),
                            ("terminated", "Terminated and Closed"),
                            ("suspended", "Suspended"),
                        ],
                        default="new",
                        max_length=50,
                    ),
                ),
                ("effective_from", models.DateField()),
                ("effective_to", models.DateField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("time_budget", models.PositiveBigIntegerField()),
                (
                    "monetary_budget",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "aims",
                    models.TextField(
                        blank=True,
                        help_text="List the project aims.",
                        null=True,
                        verbose_name="Project Aims",
                    ),
                ),
            ],
            options={
                "verbose_name": "Exterrnal Project",
                "verbose_name_plural": "External Projects",
            },
        ),
        migrations.CreateModel(
            name="ScienceProject",
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
                ("title", models.CharField(max_length=200)),
                ("tagline", models.CharField(max_length=200)),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Describe the project in one to three paragraphs.",
                        null=True,
                        verbose_name="Project Description",
                    ),
                ),
                ("keywords", models.CharField(max_length=300)),
                ("active", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("pending", "Pending Project Plan"),
                            ("active", "Active (Approved)"),
                            ("updating", "Update Requested"),
                            ("closure_requested", "Closure Requested"),
                            ("closing", "Closure Pending Final Update"),
                            ("final_update", "Final Update Requested"),
                            ("completed", "Completed and Closed"),
                            ("terminated", "Terminated and Closed"),
                            ("suspended", "Suspended"),
                        ],
                        default="new",
                        max_length=50,
                    ),
                ),
                ("effective_from", models.DateField()),
                ("effective_to", models.DateField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
            ],
            options={
                "verbose_name": "Science Project",
                "verbose_name_plural": "Science Projects",
            },
        ),
        migrations.CreateModel(
            name="StudentProject",
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
                ("title", models.CharField(max_length=200)),
                ("tagline", models.CharField(max_length=200)),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        help_text="Describe the project in one to three paragraphs.",
                        null=True,
                        verbose_name="Project Description",
                    ),
                ),
                ("keywords", models.CharField(max_length=300)),
                ("active", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "New"),
                            ("pending", "Pending Project Plan"),
                            ("active", "Active (Approved)"),
                            ("updating", "Update Requested"),
                            ("closure_requested", "Closure Requested"),
                            ("closing", "Closure Pending Final Update"),
                            ("final_update", "Final Update Requested"),
                            ("completed", "Completed and Closed"),
                            ("terminated", "Terminated and Closed"),
                            ("suspended", "Suspended"),
                        ],
                        default="new",
                        max_length=50,
                    ),
                ),
                ("effective_from", models.DateField()),
                ("effective_to", models.DateField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "level",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("pd", "Post-Doc"),
                            ("phd", "PhD"),
                            ("msc", "MSc"),
                            ("honours", "BSc Honours"),
                            ("fourth_year", "Fourth Year"),
                            ("third_year", "Third Year"),
                            ("undergrad", "Undergradate"),
                        ],
                        default="phd",
                        help_text="The academic qualification achieved through this project.",
                        max_length=50,
                    ),
                ),
                (
                    "organisation",
                    models.TextField(
                        blank=True,
                        help_text="The full name of the academic organisation.",
                        null=True,
                        verbose_name="Academic Organisation",
                    ),
                ),
            ],
            options={
                "verbose_name": "Student Project",
                "verbose_name_plural": "Student Projects",
            },
        ),
    ]
