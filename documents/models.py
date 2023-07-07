import json
from django.db import models
from common.models import CommonModel
from datetime import datetime as dt
from django.core.serializers.json import DjangoJSONEncoder


class Endorsement(CommonModel):
    """
    Model Definition for endorsements. Split from Project Plan.
    """

    class EndorsementChoices(models.TextChoices):
        NOTREQUIRED = "notrequired", "Not Required"
        REQUIRED = "required", "Required"
        DENIED = "denied", "Denied"
        GRANTED = "granted", "Granted"

    project_plan = models.ForeignKey(
        "documents.ProjectPlanDetail",
        related_name="endorsements",
        on_delete=models.CASCADE,
    )

    bm_endorsement = models.CharField(
        max_length=100,
        choices=EndorsementChoices.choices,
        default=EndorsementChoices.REQUIRED,
        help_text="The Biometrician's endorsement of the methodology's statistical validity.",
    )

    hc_endorsement = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        default=EndorsementChoices.NOTREQUIRED,
        choices=EndorsementChoices.choices,
        help_text="The Herbarium Curator's endorsement of the planned collection of voucher specimens.",
    )

    ae_endorsement = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        default=EndorsementChoices.NOTREQUIRED,
        choices=EndorsementChoices.choices,
        help_text="The Animal Ethics Committee's endorsement of the planned direct interaction with animals. Approval process is currently handled outside of SPMS.",
    )

    data_manager_endorsement = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        choices=EndorsementChoices.choices,
        help_text="The Data Manager's endorsement of the project's data management. \
            The DM will help to set up Wiki pages, data catalogue permissions, \
            scientific sites, and advise on metadata creation.",
    )

    def __str__(self) -> str:
        return f"ENDORSEMENTS - {self.project_plan}"

    class Meta:
        verbose_name = "Endorsement"
        verbose_name_plural = "Endorsements"


class ProjectDocument(CommonModel):

    """ "
    TODO: Potentially make Abstract model definition for Project Documents. They all share created_at, updated_at & a status.
    """

    class CategoryKindChoices(models.TextChoices):
        CONCEPTPLAN = "concept", "Concept Plan"
        PROJECTPLAN = "projectplan", "Project Plan"
        PROGRESSREPORT = "progressreport", "Progress Report"
        STUDENTREPORT = "studentreport", "Student Report"
        PROJECTCLOSURE = "projectclosure", "Project Closure"

    class StatusChoices(models.TextChoices):
        NEW = "new", "New Document"
        INREVIEW = "inreview", "Review Requested"
        INAPPROVAL = "inapproval", "Approval Requested"
        APPROVED = "approved", "Approved"

    status = models.CharField(
        max_length=50,
        choices=StatusChoices.choices,
        default=StatusChoices.NEW,
    )

    project = models.ForeignKey(
        "projects.Project",
        related_name="documents",
        on_delete=models.CASCADE,
    )

    creator = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="documents_created",
    )

    modifier = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="documents_modified",
    )

    kind = models.CharField(
        choices=CategoryKindChoices.choices,
        blank=True,
        null=True,
        help_text="Type of document from above category kind choices",
    )

    # ========= TODO: Change to foreign key linking to medias_pdf
    pdf = models.CharField(
        max_length=400,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.kind} - {self.project} | {self.created_at}"

    class Meta:
        verbose_name = "Project Document"
        verbose_name_plural = "Project Documents"


class ConceptPlanDetail(models.Model):
    document = models.ForeignKey(
        "documents.ProjectDocument",
        on_delete=models.CASCADE,
        related_name="concept_plan_details",
    )

    # =========
    background = models.TextField(
        blank=True, null=True, help_text="Provide background in up to 500 words"
    )
    # ACTUALLY Aims - renamed from summary which is within a PythiaTextField also called summary...
    aims = models.TextField(
        blank=True,
        null=True,
        help_text="List the aims in up to 500 words",
    )
    outcome = models.TextField(
        blank=True,
        null=True,
        help_text="Summarise expected outcome in up to 500 words",
    )
    collaborations = models.TextField(
        blank=True,
        null=True,
        help_text="List expected collaborations in up to 500 words",
    )
    strategic_context = models.TextField(
        blank=True,
        null=True,
        help_text="Describe strategic context and management implications in up to 500 words",
    )

    staff_time_allocation = models.TextField(
        blank=True,
        null=True,
        help_text="Summarise staff time allocation by role for the first three years, or for a time span appropriate for the Project's life time",
        default=json.dumps(
            [
                ["Role", "Year 1", "Year 2", "Year 3"],
                ["Scientist", "", "", ""],
                ["Technical", "", "", ""],
                ["Volunteer", "", "", ""],
                ["Collaborator", "", "", ""],
            ],
            cls=DjangoJSONEncoder,
        ),
    )

    budget = models.TextField(
        blank=True,
        null=True,
        help_text="Indicate the operating budget for the first three years, or for a time span appropriate for the Project's life time.",
        default=json.dumps(
            [
                ["Source", "Year 1", "Year 2", "Year 3"],
                ["Consolidated Funds (DBCA)", "", "", ""],
                ["External Funding", "", "", ""],
            ],
            cls=DjangoJSONEncoder,
        ),
    )

    def __str__(self) -> str:
        return f"CONCEPT PLAN | {self.project}"

    class Meta:
        verbose_name = "Concept Plan"
        verbose_name_plural = "Concept Plans"


class ProjectPlanDetail(models.Model):
    """
    Project Plan Definition
    """

    document = models.ForeignKey(
        "documents.ProjectDocument",
        on_delete=models.CASCADE,
        related_name="project_plan_details",
    )

    # ---

    # TODO: Change from text field to OneToMany to directly refer to the projects
    related_projects = models.TextField(
        blank=True,
        null=True,
        help_text="Name related SPPs and the extent you have consulted with their project leaders",
    )

    background = models.TextField(
        blank=True,
        null=True,
        help_text="Describe project background (SPP C16) including a literature review",
    )

    aims = models.TextField(
        blank=True,
        null=True,
        help_text="List project aims",
    )

    outcome = models.TextField(
        blank=True,
        null=True,
        help_text="Describe expected project outcome",
    )

    knowledge_transfer = models.TextField(
        blank=True,
        null=True,
        help_text="Anticipated users of the knowledge to be gained, and technology transfer strategy",
    )

    project_tasks = models.TextField(
        blank=True,
        null=True,
        help_text="Major tasks, milestones and outputs. Indicate delivery time frame for each task.",
    )

    references = models.TextField(
        blank=True,
        null=True,
        help_text="Paste in the bibliography of your literature research",
    )

    methadology = models.TextField(
        blank=True,
        null=True,
        help_text="Describe the study design and statistical analysis.",
    )

    involves_plants = models.BooleanField(
        # blank=False,
        # null=False,
        default=False,
        help_text="Tick to indicate that this project will collect plant specimens, which will require endorsement by the Herbarium Curator.",
    )

    involves_animals = models.BooleanField(
        # blank=False,
        # null=False,
        default=False,
        help_text="Tick to indicate that this project will involve direct interaction with animals, which will require endorsement by the Animal Ethics Committee.",
    )

    # Endorsements related.

    data_management = models.TextField(
        blank=True,
        null=True,
        help_text="Describe how and where data will be maintained, archived, cataloged. Read DBCA guideline 16.",
    )

    no_specimens = models.TextField(
        blank=True,
        null=True,
        help_text="Estimate the number of collected vouchered specimens. Provide any additional info required for the Harbarium Curator's endorsement.",
    )

    # Budget

    operating_budget = models.TextField(
        blank=True,
        null=True,
        help_text="Estimated budget: consolidated DBCA funds",
        default=json.dumps(
            [
                ["Source", "Year 1", "Year 2", "Year 3"],
                ["FTE Scientist", "", "", ""],
                ["FTE Technical", "", "", ""],
                ["Equipment", "", "", ""],
                ["Vehicle", "", "", ""],
                ["Travel", "", "", ""],
                ["Other", "", "", ""],
                ["Total", "", "", ""],
            ],
            cls=DjangoJSONEncoder,
        ),
    )

    operating_budget_external = models.TextField(
        blank=True,
        null=True,
        help_text="Estimated budget: external funds",
        default=json.dumps(
            [
                ["Source", "Year 1", "Year 2", "Year 3"],
                ["Salaries, Wages, Overtime", "", "", ""],
                ["Overheads", "", "", ""],
                ["Equipment", "", "", ""],
                ["Vehicle", "", "", ""],
                ["Travel", "", "", ""],
                ["Other", "", "", ""],
                ["Total", "", "", ""],
            ],
            cls=DjangoJSONEncoder,
        ),
    )

    def __str__(self) -> str:
        return f"PROJECT PLAN - {self.project}"

    class Meta:
        verbose_name = "Project Plan"
        verbose_name_plural = "Project Plans"


class ProgressReportDetail(models.Model):
    """
    Model Definition for Progress Reports
    """

    # Plural reportsss (per year)
    document = models.ForeignKey(
        "documents.ProjectDocument",
        on_delete=models.CASCADE,
        related_name="progress_report_details",
    )

    # ======

    year = models.PositiveIntegerField(
        editable=False,
        default=dt.today().year,
        help_text="The year on which this progress report reports on with four digits, e.g. 2014 for FY 2013/14.",
    )

    is_final_report = models.BooleanField(
        default=False,
        help_text="Whether this report is the final progress report after submitting a project closure request.",
    )

    report = models.ForeignKey(
        "reports.AnnualReport",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="The annual report publishing this Report",
    )

    context = models.TextField(
        blank=True,
        null=True,
        help_text="A shortened introduction / background for the annual activity update. Aim for 100 to 150 words.",
    )

    aims = models.TextField(
        blank=True,
        null=True,
        help_text="A bullet point list of aims for the annual activity update. Aim for 100 to 150 words. One bullet point per aim.",
    )

    progress = models.TextField(
        blank=True,
        null=True,
        help_text="Current progress and achievements for the annual activity update. Aim for 100 to 150 words. One bullet point per achievement.",
    )

    implications = models.TextField(
        blank=True,
        null=True,
        help_text="Management implications for the annual activity update. Aim for 100 to 150 words. One bullet point per implication.",
    )

    future = models.TextField(
        blank=True,
        null=True,
        help_text="Future directions for the annual activity update. Aim for 100 to 150 words. One bullet point per direction.",
    )

    def __str__(self) -> str:
        return f"PROGRESS REPORT - {self.project} | {self.year}"

    class Meta:
        verbose_name = "Progress Report"
        verbose_name_plural = "Progress Reports"


class ProjectClosureDetail(models.Model):
    """
    Project Closure Model Definition
    """

    document = models.ForeignKey(
        "documents.ProjectDocument",
        on_delete=models.CASCADE,
        related_name="project_closure_details",
    )

    # ===================

    # renamed from goal_coices

    class OutcomeChoices(models.TextChoices):
        COMPLETED = "completed", "Completed with final update"
        FORCE_COMPLETED = "forcecompleted", "Completed w/o Final Update"
        SUSPENDED = "suspended", "Suspended"
        TERMINATED = "terminated", "Terminated"

    # renamed from goal
    intended_outcome = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        default=OutcomeChoices.COMPLETED,
        choices=OutcomeChoices.choices,
        help_text="The intended project status outcome of this closure",
    )

    reason = models.TextField(
        blank=True,
        null=True,
        help_text="Reason for closure, provided by project team and/or program leader.",
    )

    scientific_outputs = models.TextField(
        blank=True,
        null=True,
        help_text="List key publications and documents.",
    )

    knowledge_transfer = models.TextField(
        blank=True,
        null=True,
        help_text="List knowledge transfer achievements.",
    )

    data_location = models.TextField(
        blank=True,
        null=True,
        help_text="Paste links to all datasets of this project on the http://internal-data.dpaw.wa.gov.au",
    )

    hardcopy_location = models.TextField(
        blank=True,
        null=True,
        help_text="Location of hardcopy of all project data.",
    )

    backup_location = models.TextField(
        blank=True,
        null=True,
        help_text="Location of electronic project data.",
    )

    def __str__(self) -> str:
        return f"CLOSURE - {self.project} | {self.intended_outcome}: {self.reason}"

    class Meta:
        verbose_name = "Project Closure"
        verbose_name_plural = "Project Closures"


class StudentReportDetail(models.Model):
    """
    Model Definition for Progress Reports of Student Projects
    """

    document = models.ForeignKey(
        "documents.ProjectDocument",
        on_delete=models.CASCADE,
        related_name="student_report_details",
    )

    # ===================

    year = models.PositiveIntegerField(
        editable=False,
        default=dt.today().year,
        help_text="The year on which this progress report reports on with four digits, e.g. 2014 for FY 2013/14.",
    )

    progress_report = models.TextField(
        blank=True,
        null=True,
        help_text="Report progress made this year in max. 150 words.",
    )

    report = models.ForeignKey(
        "reports.AnnualReport",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="The annual report publishing this StudentReport",
    )

    def __str__(self) -> str:
        return f"STUDENT REPORT - {self.project}"

    class Meta:
        verbose_name = "Student Report"
        verbose_name_plural = "Student Reports"
