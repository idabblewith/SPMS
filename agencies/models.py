from django.db import models
from common.models import CommonModel


class Affiliation(CommonModel):

    """Model Definition for Affiliation for external users (Previously defined on UserModel)"""

    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Affiliation"
        verbose_name_plural = "Affiliations"


class Agency(CommonModel):

    """Model Definition for Agency (Previously defined on UserModel)"""

    name = models.CharField(max_length=140)
    key_stakeholder = models.ForeignKey(
        "users.User",
        # Potentially change from nullable to default superuser
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Agency"
        verbose_name_plural = "Agencies"


# Renamed from workcenter
class Branch(CommonModel):

    """Model Definition for Business Area (Previously Workcenter)"""

    old_id = models.IntegerField()
    agency = models.ForeignKey(
        "agencies.Agency",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=140)
    manager = models.ForeignKey(
        "users.User",
        # Potentially change from nullable to default superuser
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"


# Renamed from program
class BusinessArea(CommonModel):

    """Model Definition for Business Area (Previously Program)"""

    agency = models.ForeignKey(
        "agencies.Agency",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=140)
    slug = models.SlugField(
        help_text="A URL-sage acronym of the BA's name without whitespace",
    )

    published = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    leader = models.ForeignKey(  # Renamed from program_leader
        "users.User",
        default=1,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,  # Prevents deletion of model object if leader deleted
        related_name="business_areas_led",
    )
    finance_admin = models.ForeignKey(
        "users.User",
        default=1,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="business_area_finances_handled",
    )

    data_custodian = models.ForeignKey(
        "users.User",
        default=1,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="business_area_data_handled",
    )

    cost_center = models.IntegerField(
        null=True,
        blank=True,
    )
    old_leader_id = models.IntegerField(
        null=True,
        blank=True,
    )
    old_finance_admin_id = models.IntegerField(
        null=True,
        blank=True,
    )
    old_data_custodian_id = models.IntegerField(
        null=True,
        blank=True,
    )

    old_id = models.IntegerField()

    focus = models.CharField(
        max_length=1250,
        blank=True,
        null=True,
    )  # NOTE SPECIES AND COMMUNITIES 1230 words (this was originally 250 words)
    introduction = models.TextField(
        blank=True,
        null=True,
    )
    image = models.ForeignKey(
        "medias.BusinessAreaPhoto",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    # MISSING COST CENTER
    # MISSING FINANCE ADMIN

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


class Division(CommonModel):
    """
    The primary departments which projects/research functions belong to.
    Projects are separated into blocks/fields in the report - these are departments.

    These Divisions are the organizational units of the Department.
    Each Division has an Executive Director, who is the approver of all Divisional projects.
    Each Divisional Program belongs to exactly one Division.
    """

    old_id = models.IntegerField()
    name = models.CharField(max_length=150)
    slug = models.SlugField(
        help_text="A URL-sage acronym of the Division's name without whitespace",
    )

    director = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
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

    # creator =models.ForeignKey(
    #     "users.User",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="divisions_created",
    # )
    # modifier =models.ForeignKey(
    #     "users.User",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="divisions_modified",
    # )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Derpartment Division"
        verbose_name_plural = "Department Divisions"


class DepartmentalService(CommonModel):
    """Departmental services.

    SPMS Science projects provide value to a defined selection of the Departmental Services.
    """

    name = models.CharField(max_length=320)
    director = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="services_led",
        help_text="The Service's Director",
    )
    old_id = models.IntegerField()

    # creator = models.ForeignKey(
    #     "users.User",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="services_created",
    # )
    # modifier = models.ForeignKey(
    #     "users.User",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="services_modified",
    # )
    # slug removes as just a number with no relation.

    class Meta:
        verbose_name = "Departmental Service"
        verbose_name_plural = "Departmental Services"

    def __str__(self):
        return f"Dept. Service {self.slug} {self.name}"
