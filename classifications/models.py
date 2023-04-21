from django.db import models
from common.models import CommonModel


# ----------------------------------
# Section: Business Area Models
# ----------------------------------


class BusinessArea(CommonModel):
    """Model Definition for Business Area (Previously Program)"""

    name = models.CharField(max_length=140)
    slug = models.CharField(max_length=20)
    focus = models.CharField(max_length=250)
    introduction = models.TextField()
    published = models.BooleanField(default=False)

    effective_from = models.DateField()

    creator = models.ForeignKey(
        "users.User",
        default=1,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,  # Check if this is desired behaviour
        related_name="business_areas_created",
    )
    modifier = models.ForeignKey(
        "users.User",
        default=1,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,  # Check if this is desired behaviour
        related_name="business_areas_modified",
    )

    leader = models.ForeignKey(
        "users.User",
        default=1,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,  # Deletes model object if leader deleted
        related_name="business_areas_led",
    )

    data_custodian = models.ForeignKey(
        "users.User",
        default=1,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="business_area_data_handled",
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Business Area"
        verbose_name_plural = "Business Areas"

    # finance_admin_id = models.ForeignKey(
    #     "users.User",
    #     on_delete=models.CASCADE,
    #     related_name="projects_financing",
    # )

    # cost_center = models.ForeignKey()


# position, ...


# ----------------------------------
# Section: Research Function Models
# ----------------------------------


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


# ----------------------------------
# Section: Department Division Models
# ----------------------------------


class Division(CommonModel):
    """
    The primary departments which projects/research functions belong to.
    ARAR Projects are separated into blocks/fields - these are departments.

    These Divisions are the organizational units of the Department.
    Each Division has an Executive Director, who is the approver of all Divisional projects.
    Each Divisional Program belongs to exactly one Division.
    """

    name = models.CharField(max_length=150)
    slug = models.SlugField(
        help_text="A URL-sage acronym of the Division's name without whitespace",
    )
    director = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,  # CONFIRM
        blank=True,
        null=True,
        related_name="divisions_led",
        help_text="The Division's director is attributed as head of the Division in reports",
    )
    approver = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="divisions_approved",
        help_text="The Approver receives notifications about outstanding requests and has permission \
            to approve documents. The approver can be anyone in a supervisory role, including the Director.",
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Derpartment Division"
        verbose_name_plural = "Department Divisions"
