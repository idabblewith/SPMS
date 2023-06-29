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
    old_id = models.IntegerField()

    class Meta:
        verbose_name = "Research Function"
        verbose_name_plural = "Research Functions"

    def __str__(self) -> str:
        return f"{self.name}"

    # ------------------------------
    # Section: Abstract Project Models
    # ------------------------------

    # class BaseProjectWithStartDate(BaseProject):
    # start_date = models.DateField()
    # end_date = models.DateField()

    # class Meta:
    #     abstract = True


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
        CLOSURE = ("closure_requested", "Closure Requested")
        CLOSING = ("closing", "Closure Pending Final Update")
        FINAL_UPDATE = ("final_update", "Final Update Requested")
        COMPLETED = ("completed", "Completed and Closed")
        TERMINATED = ("terminated", "Terminated and Closed")
        SUSPENDED = ("suspended", "Suspended")

    old_id = models.IntegerField()
    kind = models.CharField(
        choices=CategoryKindChoices.choices,
        # "categories.ProjectCategory",
        # on_delete=models.SET_NULL,
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
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    tagline = models.CharField(max_length=500)
    keywords = models.CharField(
        max_length=500
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

    # class Meta:
    #     abstract = True

    def __str__(self) -> str:
        return f"{self.kind} {self.title}"


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
