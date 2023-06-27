from django.db import models
from common.models import CommonModel


# ------------------------------
# Section: Research Function Model
# ------------------------------


class ResearchFunction(CommonModel):
    """
    Research functions categorise projects in the ARAR;

    """

    name = models.CharField(max_length=150)
    description = models.TextField(
        null=False,
        blank=True,
    )
    association = models.TextField(
        null=True,
        blank=True,
        help_text="The research function's association with departmental programs/divisions.",
    )
    leader = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  # Double check policy
        related_name="research_functions_led",
        verbose_name="Function Leader",
        help_text="The scientist in charge of the Research Function",
    )
    active = models.BooleanField(
        default=True,
        help_text="Whether this research function has been deprecated or not.",
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Research Function"
        verbose_name_plural = "Research Functions"


# ------------------------------
# Section: Abstract Project Models
# ------------------------------


class BaseProject(CommonModel):
    """
    Model Definition for BaseProject

    This model is abstract.
    Inherited directly by BaseProjectWithStartDate and CoreFunctionProject.

    A Project is an endeavour of a team of staff, where staff and financial
    resources are allocated to address a specific problem and achieve an
    outcome that reflects the priorities of divisional strategy.

    The life cycle stage of a project is indicated by its status field.
    The life cycle stage transitions are under control by its own can_<action>
    methods, which test whether a certain action is permitted considering
    the project's document approval statuses.

    """

    class StatusChoices(models.TextChoices):
        NEW = ("new", "New")
        PENDING = ("pending", "Pending Project Plan")
        ACTIVE = ("active", "Active (Approved)")
        UPDATING = ("updating", "Update Requested")
        CLOSURE = ("closure_requested", "Closure Requested")
        CLOSING = ("closing", "Closure Pending Final Update")
        FINAL_UPDATE = ("final_update", "Final Update Requested")
        COMPLETED = ("completed", "Completed and Closed")
        TERMINATED = ("terminated", "Terminated and Closed")
        SUSPENDED = ("suspended", "Suspended")

    # class TypeChoices(models.TextChoices):
    #     EXTERNAL = ("external", "External Project")
    #     SCIENCE = ("science", "Science Project")
    #     CORE = ("core", "Core Project")
    #     STUDENT = ("student", "Student Project")

    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    description = models.TextField(
        verbose_name=("Project Description"),
        null=True,
        blank=True,
        help_text=("Describe the project in one to three paragraphs."),
    )
    keywords = models.CharField(
        max_length=300
    )  # will extract as semicolon seperated values like linkedin skills

    kind = models.ForeignKey(
        "categories.ProjectCategory",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="The project type determines the approval and \
                    documentation requirements during the project's \
                    life span. Choose wisely - you will not be able \
                    to change the project type later. \
                    If you get it wrong, create a new project of the \
                    correct type and tell admins to delete the duplicate \
                    project of the incorrect type.",
    )
    active = models.BooleanField(default=False)
    status = models.CharField(
        max_length=50,
        choices=StatusChoices.choices,
        default=StatusChoices.NEW,
    )
    # agency = models.ForeignKey(
    #     "agencies.Agency",
    #     null=True,
    #     blank=True,

    # )
    effective_from = models.DateField()  # Clarify if these two required
    effective_to = models.DateField()

    # business_area_id = models.ForeignKey()

    class Meta:
        abstract = True


class BaseProjectWithStartDate(BaseProject):
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        abstract = True


# ------------------------------
# Section: Project Models
# ------------------------------


class ExternalProject(BaseProjectWithStartDate):  # Formerly CollaborationProject
    """
    External Project Model Definition

    An external Collaboration with academia, industry or government
    requires only registration, but no Progress Reports.
    """

    creator_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # Check if this is desired behaviour
        related_name="external_projects_created",
    )
    modifier_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # Check if this is desired behaviour
        related_name="external_projects_modified",
    )
    # formatted_title/name = models.TextField() # check if this is necessary, as title already present

    # budget = models.TextField() # Seek clarification on whether there should be separate budgets e.g.

    time_budget = models.PositiveBigIntegerField()  # max_time_budget (cannot exceed)
    monetary_budget = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # in aud, cannot exceed
    aims = models.TextField(
        verbose_name=("Project Aims"),
        null=True,
        blank=True,
        help_text=("List the project aims."),
    )

    class Meta:
        verbose_name = "Exterrnal Project"
        verbose_name_plural = "External Projects"

    def __str__(self) -> str:
        return f"{self.title}"

    # CREATE SEPARATE TABLE FOR STUDENT AND STAFF LISTS
    # Access collaborators in related_name (Staff_list_plain)
    #   staff_list_plain = models.TextField(
    #         verbose_name="DBCA Involvement",
    #         editable=False,
    #         null=True, blank=True,
    #         help_text=_("Staff names in order of membership rank."
    #                     " Update by adding DBCA staff as team members."))


class StudentProject(BaseProjectWithStartDate):
    """
    Student Project Model Definition

    Student Projects are academic collaborations involving a student's
    work, can be started without divisional approval and only require
    annual Progress Reports.
    """

    class StudentLevelChoices(models.TextChoices):
        PD = ("pd", "Post-Doc")
        PHD = ("phd", "PhD")
        MSC = ("msc", "MSc")
        HON = ("honours", "BSc Honours")
        YR4 = ("fourth_year", "Fourth Year")
        YR3 = ("third_year", "Third Year")
        UND = ("undergrad", "Undergradate")

    creator_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # Check if this is desired behaviour
        related_name="student_projects_created",
    )
    modifier_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # Check if this is desired behaviour
        related_name="student_projects_modified",
    )

    level = models.CharField(
        max_length=50,
        choices=StudentLevelChoices.choices,
        null=False,
        blank=True,
        default=StudentLevelChoices.PHD,
        help_text="The academic qualification achieved through this project.",
    )

    organisation = models.TextField(
        verbose_name="Academic Organisation",
        blank=True,
        null=True,
        help_text="The full name of the academic organisation.",
    )

    class Meta:
        verbose_name = "Student Project"
        verbose_name_plural = "Student Projects"

    def __str__(self) -> str:
        return f"{self.title} | {self.organisation}"

    # CREATE SEPARATE TABLE FOR STUDENT AND STAFF LISTS
    # Access collaborators in related_name (student_list_plain)
    #   student_list_plain = models.TextField(
    #         verbose_name="Student list",
    #         editable=False,
    #         null=True, blank=True,
    #         help_text=_("Student names in order of membership rank.")
    # )
    #   academic_list_plain = models.TextField(
    #         verbose_name="Academic",
    #         editable=False,
    #         null=True, blank=True,
    #         help_text=_("Academic supervisors in order of membership rank."
    #                     " Update by adding team members as academic "
    #                     "supervisors."))
    #     academic_list_plain_no_affiliation = models.TextField(
    #         verbose_name="Academic without affiliation",
    #         editable=False,
    #         null=True, blank=True,
    #         help_text=_("Academic supervisors without their affiliation "
    #                     "in order of membership rank. Update by adding team "
    #                     "members as academic supervisors."))


class ScienceProject(BaseProjectWithStartDate):
    """
    Science Project Model Definition

    A Science Project is proposed by a Concept Plan, defined by a Project Plan,
    reported on annually by a Progress Report, and closed by a Closure Form
    after the last Progress Report.

    """

    creator_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # Check if this is desired behaviour
        related_name="science_projects_created",
    )
    modifier_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # Check if this is desired behaviour
        related_name="science_projects_modified",
    )

    class Meta:
        verbose_name = "Science Project"
        verbose_name_plural = "Science Projects"

    def __str__(self) -> str:
        return f"{self.title}"


class CoreFunctionProject(BaseProject):
    """
    Core Function Project Model Definition

    A Core Function is without beginning.
    A Core Function is without end.
    There is no approval.
    There is no closure.
    Change comes from within.
    The Core Function answers only to the mighty ARARReport.
    """

    creator_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # Check if this is desired behaviour
        related_name="core_function_projects_created",
    )
    modifier_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # Check if this is desired behaviour
        related_name="core_function_projects_modified",
    )

    class Meta:
        verbose_name = "Core Function"
        verbose_name_plural = "Core Functions"

    def __str__(self) -> str:
        return f"{self.title}"
