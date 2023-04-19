from django.db import models
from common.models import CommonModel


# ------------------------------
# Section: Business Area Models
# ------------------------------


class BusinessArea(CommonModel):
    """Model Definition for Business Area (Previously Program)"""

    name = models.CharField(max_length=140)
    slug = models.CharField(max_length=20)
    focus = models.CharField(max_length=250)
    introduction = models.TextField()
    published = models.BooleanField(default=False)

    effective_from = models.DateField()

    creator_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # Check if this is desired behaviour
        related_name="business_areas_created",
    )
    modifier_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # Check if this is desired behaviour
        related_name="business_areas_modified",
    )

    leader_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # Deletes model object if leader deleted
        related_name="business_areas_leading",
    )

    data_custodian_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="business_areas_handling_data",
    )

    # finance_admin_id = models.ForeignKey(
    #     "users.User",
    #     on_delete=models.CASCADE,
    #     related_name="projects_financing",
    # )

    # cost_center = models.ForeignKey()


# position, ...
