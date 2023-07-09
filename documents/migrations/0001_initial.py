# Generated by Django 4.2.2 on 2023-07-09 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ConceptPlanDetail",
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
                (
                    "background",
                    models.TextField(
                        blank=True,
                        help_text="Provide background in up to 500 words",
                        null=True,
                    ),
                ),
                (
                    "aims",
                    models.TextField(
                        blank=True,
                        help_text="List the aims in up to 500 words",
                        null=True,
                    ),
                ),
                (
                    "outcome",
                    models.TextField(
                        blank=True,
                        help_text="Summarise expected outcome in up to 500 words",
                        null=True,
                    ),
                ),
                (
                    "collaborations",
                    models.TextField(
                        blank=True,
                        help_text="List expected collaborations in up to 500 words",
                        null=True,
                    ),
                ),
                (
                    "strategic_context",
                    models.TextField(
                        blank=True,
                        help_text="Describe strategic context and management implications in up to 500 words",
                        null=True,
                    ),
                ),
                (
                    "staff_time_allocation",
                    models.TextField(
                        blank=True,
                        default='[["Role", "Year 1", "Year 2", "Year 3"], ["Scientist", "", "", ""], ["Technical", "", "", ""], ["Volunteer", "", "", ""], ["Collaborator", "", "", ""]]',
                        help_text="Summarise staff time allocation by role for the first three years, or for a time span appropriate for the Project's life time",
                        null=True,
                    ),
                ),
                (
                    "budget",
                    models.TextField(
                        blank=True,
                        default='[["Source", "Year 1", "Year 2", "Year 3"], ["Consolidated Funds (DBCA)", "", "", ""], ["External Funding", "", "", ""]]',
                        help_text="Indicate the operating budget for the first three years, or for a time span appropriate for the Project's life time.",
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Concept Plan",
                "verbose_name_plural": "Concept Plans",
            },
        ),
        migrations.CreateModel(
            name="Endorsement",
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
                (
                    "bm_endorsement",
                    models.CharField(
                        choices=[
                            ("notrequired", "Not Required"),
                            ("required", "Required"),
                            ("denied", "Denied"),
                            ("granted", "Granted"),
                        ],
                        default="required",
                        help_text="The Biometrician's endorsement of the methodology's statistical validity.",
                        max_length=100,
                    ),
                ),
                (
                    "hc_endorsement",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("notrequired", "Not Required"),
                            ("required", "Required"),
                            ("denied", "Denied"),
                            ("granted", "Granted"),
                        ],
                        default="notrequired",
                        help_text="The Herbarium Curator's endorsement of the planned collection of voucher specimens.",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "ae_endorsement",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("notrequired", "Not Required"),
                            ("required", "Required"),
                            ("denied", "Denied"),
                            ("granted", "Granted"),
                        ],
                        default="notrequired",
                        help_text="The Animal Ethics Committee's endorsement of the planned direct interaction with animals. Approval process is currently handled outside of SPMS.",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "data_manager_endorsement",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("notrequired", "Not Required"),
                            ("required", "Required"),
                            ("denied", "Denied"),
                            ("granted", "Granted"),
                        ],
                        default="notrequired",
                        help_text="The Data Manager's endorsement of the project's data management.             The DM will help to set up Wiki pages, data catalogue permissions,             scientific sites, and advise on metadata creation.",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "data_management",
                    models.TextField(
                        blank=True,
                        help_text="Describe how and where data will be maintained, archived, cataloged. Read DBCA guideline 16.",
                        null=True,
                    ),
                ),
                (
                    "no_specimens",
                    models.TextField(
                        blank=True,
                        help_text="Estimate the number of collected vouchered specimens. Provide any additional info required for the Harbarium Curator's endorsement.",
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Endorsement",
                "verbose_name_plural": "Endorsements",
            },
        ),
        migrations.CreateModel(
            name="ProgressReportDetail",
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
                (
                    "year",
                    models.PositiveIntegerField(
                        default=2023,
                        editable=False,
                        help_text="The year on which this progress report reports on with four digits, e.g. 2014 for FY 2013/14.",
                    ),
                ),
                (
                    "is_final_report",
                    models.BooleanField(
                        default=False,
                        help_text="Whether this report is the final progress report after submitting a project closure request.",
                    ),
                ),
                (
                    "context",
                    models.TextField(
                        blank=True,
                        help_text="A shortened introduction / background for the annual activity update. Aim for 100 to 150 words.",
                        null=True,
                    ),
                ),
                (
                    "aims",
                    models.TextField(
                        blank=True,
                        help_text="A bullet point list of aims for the annual activity update. Aim for 100 to 150 words. One bullet point per aim.",
                        null=True,
                    ),
                ),
                (
                    "progress",
                    models.TextField(
                        blank=True,
                        help_text="Current progress and achievements for the annual activity update. Aim for 100 to 150 words. One bullet point per achievement.",
                        null=True,
                    ),
                ),
                (
                    "implications",
                    models.TextField(
                        blank=True,
                        help_text="Management implications for the annual activity update. Aim for 100 to 150 words. One bullet point per implication.",
                        null=True,
                    ),
                ),
                (
                    "future",
                    models.TextField(
                        blank=True,
                        help_text="Future directions for the annual activity update. Aim for 100 to 150 words. One bullet point per direction.",
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Progress Report",
                "verbose_name_plural": "Progress Reports",
            },
        ),
        migrations.CreateModel(
            name="ProjectClosureDetail",
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
                (
                    "intended_outcome",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("completed", "Completed with final update"),
                            ("forcecompleted", "Completed w/o Final Update"),
                            ("suspended", "Suspended"),
                            ("terminated", "Terminated"),
                        ],
                        default="completed",
                        help_text="The intended project status outcome of this closure",
                        max_length=300,
                        null=True,
                    ),
                ),
                (
                    "reason",
                    models.TextField(
                        blank=True,
                        help_text="Reason for closure, provided by project team and/or program leader.",
                        null=True,
                    ),
                ),
                (
                    "scientific_outputs",
                    models.TextField(
                        blank=True,
                        help_text="List key publications and documents.",
                        null=True,
                    ),
                ),
                (
                    "knowledge_transfer",
                    models.TextField(
                        blank=True,
                        help_text="List knowledge transfer achievements.",
                        null=True,
                    ),
                ),
                (
                    "data_location",
                    models.TextField(
                        blank=True,
                        help_text="Paste links to all datasets of this project on the http://internal-data.dpaw.wa.gov.au",
                        null=True,
                    ),
                ),
                (
                    "hardcopy_location",
                    models.TextField(
                        blank=True,
                        help_text="Location of hardcopy of all project data.",
                        null=True,
                    ),
                ),
                (
                    "backup_location",
                    models.TextField(
                        blank=True,
                        help_text="Location of electronic project data.",
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Project Closure",
                "verbose_name_plural": "Project Closures",
            },
        ),
        migrations.CreateModel(
            name="ProjectDocument",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("new", "New Document"),
                            ("inreview", "Review Requested"),
                            ("inapproval", "Approval Requested"),
                            ("approved", "Approved"),
                        ],
                        default="new",
                        max_length=50,
                    ),
                ),
                (
                    "kind",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("concept", "Concept Plan"),
                            ("projectplan", "Project Plan"),
                            ("progressreport", "Progress Report"),
                            ("studentreport", "Student Report"),
                            ("projectclosure", "Project Closure"),
                        ],
                        help_text="Type of document from above category kind choices",
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Project Document",
                "verbose_name_plural": "Project Documents",
            },
        ),
        migrations.CreateModel(
            name="ProjectPlanDetail",
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
                (
                    "background",
                    models.TextField(
                        blank=True,
                        help_text="Describe project background (SPP C16) including a literature review",
                        null=True,
                    ),
                ),
                (
                    "aims",
                    models.TextField(
                        blank=True, help_text="List project aims", null=True
                    ),
                ),
                (
                    "outcome",
                    models.TextField(
                        blank=True,
                        help_text="Describe expected project outcome",
                        null=True,
                    ),
                ),
                (
                    "knowledge_transfer",
                    models.TextField(
                        blank=True,
                        help_text="Anticipated users of the knowledge to be gained, and technology transfer strategy",
                        null=True,
                    ),
                ),
                (
                    "project_tasks",
                    models.TextField(
                        blank=True,
                        help_text="Major tasks, milestones and outputs. Indicate delivery time frame for each task.",
                        null=True,
                    ),
                ),
                (
                    "listed_references",
                    models.TextField(
                        blank=True,
                        help_text="Paste in the bibliography of your literature research",
                        null=True,
                    ),
                ),
                (
                    "methodology",
                    models.TextField(
                        blank=True,
                        help_text="Describe the study design and statistical analysis.",
                        null=True,
                    ),
                ),
                (
                    "involves_plants",
                    models.BooleanField(
                        default=False,
                        help_text="Tick to indicate that this project will collect plant specimens, which will require endorsement by the Herbarium Curator.",
                    ),
                ),
                (
                    "involves_animals",
                    models.BooleanField(
                        default=False,
                        help_text="Tick to indicate that this project will involve direct interaction with animals, which will require endorsement by the Animal Ethics Committee.",
                    ),
                ),
                (
                    "operating_budget",
                    models.TextField(
                        blank=True,
                        default='[["Source", "Year 1", "Year 2", "Year 3"], ["FTE Scientist", "", "", ""], ["FTE Technical", "", "", ""], ["Equipment", "", "", ""], ["Vehicle", "", "", ""], ["Travel", "", "", ""], ["Other", "", "", ""], ["Total", "", "", ""]]',
                        help_text="Estimated budget: consolidated DBCA funds",
                        null=True,
                    ),
                ),
                (
                    "operating_budget_external",
                    models.TextField(
                        blank=True,
                        default='[["Source", "Year 1", "Year 2", "Year 3"], ["Salaries, Wages, Overtime", "", "", ""], ["Overheads", "", "", ""], ["Equipment", "", "", ""], ["Vehicle", "", "", ""], ["Travel", "", "", ""], ["Other", "", "", ""], ["Total", "", "", ""]]',
                        help_text="Estimated budget: external funds",
                        null=True,
                    ),
                ),
                (
                    "related_projects",
                    models.TextField(
                        blank=True,
                        help_text="Name related SPPs and the extent you have consulted with their project leaders",
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Project Plan",
                "verbose_name_plural": "Project Plans",
            },
        ),
        migrations.CreateModel(
            name="StudentReportDetail",
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
                (
                    "year",
                    models.PositiveIntegerField(
                        default=2023,
                        editable=False,
                        help_text="The year on which this progress report reports on with four digits, e.g. 2014 for FY 2013/14.",
                    ),
                ),
                (
                    "progress_report",
                    models.TextField(
                        blank=True,
                        help_text="Report progress made this year in max. 150 words.",
                        null=True,
                    ),
                ),
                (
                    "document",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student_report_details",
                        to="documents.projectdocument",
                    ),
                ),
            ],
            options={
                "verbose_name": "Student Report",
                "verbose_name_plural": "Student Reports",
            },
        ),
    ]
