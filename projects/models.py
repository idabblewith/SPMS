from django.db import models
import categories
from common.models import CommonModel
from datetime import datetime as dt

# ------------------------------
# Section: Research Function Model
# ------------------------------


class ResearchFunction(CommonModel):
    """
    Research functions categorise projects in the ARAR;

    """

    name = models.CharField(max_length=150)
    description = models.TextField(
        null=True,
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
    is_active = models.BooleanField(
        default=False,
        help_text="Whether this research function has been deprecated or not.",
    )
    old_id = models.BigIntegerField()

    class Meta:
        verbose_name = "Research Function"
        verbose_name_plural = "Research Functions"

    def __str__(self) -> str:
        return f"{self.name}"


# ------------------------------
# Section: Project Models
# ------------------------------


def get_next_available_number_for_year():
    """Return the lowest available project number for a given project year."""

    year = dt.today().year
    project_numbers = Project.objects.filter(year=year).values("number")
    if project_numbers.count() == 0:
        return 1
    else:
        return max([x["number"] for x in list(project_numbers)]) + 1


class Project(CommonModel):
    """
    Model Definition for Project
    """

    class CategoryKindChoices(models.TextChoices):
        SCIENCE = "science", "Science"
        STUDENT = "student", "Student"
        EXTERNAL = "external", "External"
        COREFUNCTION = "core_function", "Core Function"

    class StatusChoices(models.TextChoices):
        NEW = ("new", "New")
        PENDING = ("pending", "Pending Project Plan")
        ACTIVE = ("active", "Active (Approved)")
        UPDATING = ("updating", "Update Requested")
        CLOSUREREQ = ("closure_requested", "Closure Requested")
        CLOSING = ("closing", "Closure Pending Final Update")
        FINAL_UPDATE = ("final_update", "Final Update Requested")
        COMPLETED = ("completed", "Completed and Closed")
        TERMINATED = ("terminated", "Terminated and Closed")
        SUSPENDED = ("suspended", "Suspended")

    ACTIVE_ONLY = (
        StatusChoices.NEW,
        StatusChoices.PENDING,
        StatusChoices.ACTIVE,
        StatusChoices.UPDATING,
        StatusChoices.CLOSUREREQ,
        StatusChoices.CLOSING,
        StatusChoices.FINAL_UPDATE,
    )

    PUBLISHED_ONLY = (
        StatusChoices.ACTIVE,
        StatusChoices.UPDATING,
        StatusChoices.CLOSUREREQ,
        StatusChoices.CLOSING,
        StatusChoices.FINAL_UPDATE,
        StatusChoices.COMPLETED,
    )

    CLOSED_ONLY = (
        StatusChoices.COMPLETED,
        StatusChoices.TERMINATED,
        StatusChoices.SUSPENDED,
    )

    old_id = models.BigIntegerField()
    kind = models.CharField(
        choices=CategoryKindChoices.choices,
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
    status = models.CharField(
        max_length=50,
        choices=StatusChoices.choices,
        default=StatusChoices.NEW,
    )
    year = models.PositiveIntegerField(
        default=dt.today().year,
        help_text="The project year with four digits, e.g. 2014",
    )
    number = models.PositiveIntegerField(
        default=get_next_available_number_for_year,
        help_text="The running project number within the project year.",
    )

    title = models.CharField(
        max_length=500,
        unique=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    tagline = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )
    keywords = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )  # will extract as semicolon seperated values like linkedin skills

    start_date = models.DateField(
        blank=True,
        null=True,
    )  # Clarify if these two required
    end_date = models.DateField(
        blank=True,
        null=True,
    )

    business_area = models.ForeignKey(
        "agencies.BusinessArea",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        #  related_name='business'
    )

    # image = models.ForeignKey(
    #     "medias.ProjectPhoto",
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL
    #     #  related_name='business'
    # )

    def __str__(self) -> str:
        return f"({self.kind.upper()}) {self.title}"


class ProjectArea(CommonModel):
    old_id = models.BigIntegerField()
    project = models.ForeignKey(
        "projects.Project",
        related_name="areas",
        on_delete=models.CASCADE,
    )
    area = models.ForeignKey(
        "locations.Area",
        related_name="projects_in_area",
        on_delete=models.CASCADE,
    )


# class ProjectTeam(models.Model):
#     project = models.ForeignKey(
#         "projects.Project",
#         related_name="team",
#         on_delete=models.CASCADE,
#     )
#     members = models.ManyToManyField(
#         "projects.ProjectMember",
#         related_name="team_member_of",
#     )


class ProjectMember(CommonModel):
    class RoleChoices(models.TextChoices):
        SUPERVISING = ("supervising", "Supervising Scientist")
        RESEARCH = ("research", "Research Scientist")
        TECHNICAL = ("technical", "Technical Officer")
        EXTERNALCOL = ("externalcol", "External Collaborator")
        ACADEMICSUPER = ("academicsuper", "Academic Supervisor")
        STUDENT = ("superstudent", "Supervised Student")
        EXTERNALPEER = ("externalpeer", "External Peer")
        CONSULTED = ("consulted", "Consulted Peer")
        GROUP = ("group", "Involved Group")

    STAFF_ROLES = (
        RoleChoices.SUPERVISING,
        RoleChoices.RESEARCH,
        RoleChoices.TECHNICAL,
    )

    project = models.ForeignKey(
        "projects.Project",
        related_name="members",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        "users.User",
        related_name="member_of",
        on_delete=models.CASCADE,
    )
    role = models.CharField(
        max_length=50,
        choices=RoleChoices.choices,
    )
    time_allocation = models.FloatField(
        blank=True,
        null=True,
        default=0,
        verbose_name="Time allocation (0 to 1 FTE)",
        help_text="Indicative time allocation as a fraction of a Full Time Equivalent (210 person-days). Values between 0 and 1. Fill in estimated allocation for the next 12 months.",
    )
    position = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="List position",
        default=100,
        help_text="The lowest position number comes first in the team members list. Ignore to keep alphabetical order, increase to shift member towards the end of the list, decrease to promote member to beginning of the list.",
    )
    short_code = models.CharField(
        blank=True,
        null=True,
        max_length=500,
        verbose_name="Short code",
        help_text="Cost code for this project membership's salary. Allocated by divisional admin.",
    )
    comments = models.TextField(
        blank=True,
        null=True,
        help_text="Any comments clarifying the project membership.",
    )

    old_id = models.BigIntegerField()

    def __str__(self) -> str:
        return f"{self.user} ({self.project}) "

    class Meta:
        verbose_name = "Project Member"
        verbose_name_plural = "Project Members"


class ProjectDetails(models.Model):
    project = models.ForeignKey(
        "projects.Project",
        related_name="details",
        on_delete=models.CASCADE,
    )
    # image = models.ForeignKey(
    #     "medias.ProjectPhoto",
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    # )
    creator = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        related_name="projects_created",
        blank=True,
        null=True,
    )
    modifier = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        related_name="projects_modified",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        related_name="projects_owned",
        null=True,
    )
    data_custodian = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        related_name="projects_where_data_custodian",
        blank=True,
        null=True,
    )
    site_custodian = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        related_name="projects_where_site_custodian",
        blank=True,
        null=True,
    )

    research_function = models.ForeignKey(
        "projects.ResearchFunction",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    supervising_scientist_list = models.ManyToManyField(
        "users.User",
        related_name="projects_as_supervising_scientist",
    )
    area_list = models.ManyToManyField(
        "locations.Area",
        related_name="projects_location",
    )
    # output_program =

    pass


# Science Project CSV has no extra data
# Core Function Project has no extra data
# Student Project CSV has extra data: level, organisation, student_list_plain, academic_list_plain, academic_list_plain_no_affiliation
# Collaboration Project CSV has extra data: name, budget, staff_list, aims, description


class StudentProjectDetails(models.Model):
    pass


class ExternalProjectDetails(models.Model):
    pass
    # collaboration_with = models.CharField(
    #     max_length=300,
    # )
    # staff_list =
    # # renamed from 'name'
    # budget = models.CharField(
    #     max_length=250,
    #     null=True,
    #     blank=True,
    # )
    # description = models.CharField(
    #     max_length=500,
    #     null=True,
    #     blank=True,
    # )
    # aims = models.CharField(
    #     max_length=500,
    #     null=True,
    #     blank=True,
    # )


# class ProjectDetails(CommonModel):
#     """
#     Contains any additional fields for Projects (non-specific to type)
#     """

#     creator = models.ForeignKey(
#         "users.User",
#         on_delete=models.SET_NULL,  # Check if this is desired behaviour
#         null=True,
#         blank=True,
#         related_name="external_projects_created",
#     )
#     modifier = models.ForeignKey(
#         "users.User",
#         on_delete=models.SET_NULL,  # Check if this is desired behaviour
#         null=True,
#         blank=True,
#         related_name="external_projects_modified",
#     )
#     project_owner = models.ForeignKey(
#         "users.User",
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="projects_owned",
#     )


# class StudentProjectDetails(CommonModel):
#     """
#     Student Project Model Definition
#     """

#     class StudentLevelChoices(models.TextChoices):
#         PD = ("pd", "Post-Doc")
#         PHD = ("phd", "PhD")
#         MSC = ("msc", "MSc")
#         HON = ("honours", "BSc Honours")
#         YR4 = ("fourth_year", "Fourth Year")
#         YR3 = ("third_year", "Third Year")
#         UND = ("undergrad", "Undergradate")

#     project = models.OneToOneField(
#         "projects.Project",
#         on_delete=models.CASCADE,
#     )
#     level = models.CharField(
#         max_length=50,
#         choices=StudentLevelChoices.choices,
#         null=False,
#         blank=True,
#         default=StudentLevelChoices.PHD,
#         help_text="The academic qualification achieved through this project.",
#     )

#     organisation = models.TextField(
#         verbose_name="Academic Organisation",
#         blank=True,
#         null=True,
#         help_text="The full name of the academic organisation.",
#     )

#     class Meta:
#         verbose_name = "Student Project"
#         verbose_name_plural = "Student Projects"

#     def __str__(self) -> str:
#         return f"{self.title} | {self.organisation}"


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


# class ExternalProjectDetails(CommonModel):  # Formerly CollaborationProject
#     """
#     External Project Model Definition
#     """

#     project = models.OneToOneField(
#         'projects.Project',
#         on_delete=models.CASCADE,
#     )
#     creator = models.ForeignKey(
#         "users.User",
#         on_delete=models.SET_NULL,  # Check if this is desired behaviour
#         null=True,
#         blank=True,
#         related_name="external_projects_created",
#     )
#     modifier = models.ForeignKey(
#         "users.User",
#         on_delete=models.SET_NULL,  # Check if this is desired behaviour
#         null=True,
#         blank=True,
#         related_name="external_projects_modified",
#     )

#     # budget = models.TextField() # Seek clarification on whether there should be separate budgets e.g.

#     # time_budget = models.PositiveBigIntegerField()  # max_time_budget (cannot exceed)
#     # monetary_budget = models.DecimalField(
#     #     max_digits=10, decimal_places=2
#     # )  # in aud, cannot exceed
#     # aims = models.TextField(
#     #     verbose_name=("Project Aims"),
#     #     null=True,
#     #     blank=True,
#     #     help_text=("List the project aims."),
#     # )

#     class Meta:
#         verbose_name = "Exterrnal Project"
#         verbose_name_plural = "External Projects"

#     def __str__(self) -> str:
#         return f"{self.title}"

# CREATE SEPARATE TABLE FOR STUDENT AND STAFF LISTS
# Access collaborators in related_name (Staff_list_plain)
#   staff_list_plain = models.TextField(
#         verbose_name="DBCA Involvement",
#         editable=False,
#         null=True, blank=True,
#         help_text=_("Staff names in order of membership rank."
#                     " Update by adding DBCA staff as team members."))


# class BaseProject(CommonModel):
#     """
#     Model Definition for BaseProject
#     """

#     class StatusChoices(models.TextChoices):
#         NEW = ("new", "New")
#         PENDING = ("pending", "Pending Project Plan")
#         ACTIVE = ("active", "Active (Approved)")
#         UPDATING = ("updating", "Update Requested")
#         CLOSURE = ("closure_requested", "Closure Requested")
#         CLOSING = ("closing", "Closure Pending Final Update")
#         FINAL_UPDATE = ("final_update", "Final Update Requested")
#         COMPLETED = ("completed", "Completed and Closed")
#         TERMINATED = ("terminated", "Terminated and Closed")
#         SUSPENDED = ("suspended", "Suspended")

#     title = models.CharField(max_length=200)
#     description = models.TextField(
#         verbose_name=("Project Description"),
#         null=True,
#         blank=True,
#         help_text=("Describe the project in one to three paragraphs."),
#     )

#     tagline = models.CharField(max_length=200)
#     keywords = models.CharField(
#         max_length=300
#     )  # will extract as semicolon seperated values like linkedin skills


#     kind = models.ForeignKey(
#         "categories.ProjectCategory",
#         on_delete=models.SET_NULL,
#         blank=True,
#         null=True,
#         help_text="The project type determines the approval and \
#                     documentation requirements during the project's \
#                     life span. Choose wisely - you will not be able \
#                     to change the project type later. \
#                     If you get it wrong, create a new project of the \
#                     correct type and tell admins to delete the duplicate \
#                     project of the incorrect type.",
#     )
#     status = models.CharField(
#         max_length=50,
#         choices=StatusChoices.choices,
#         default=StatusChoices.NEW,
#     )

#     is_active = models.BooleanField(default=False)

#     # agency = models.ForeignKey(
#     #     "agencies.Agency",
#     #     null=True,
#     #     blank=True,

#     # )
#     effective_from = models.DateField()  # Clarify if these two required
#     effective_to = models.DateField()

#     # business_area_id = models.ForeignKey()

#     class Meta:
#         abstract = True
