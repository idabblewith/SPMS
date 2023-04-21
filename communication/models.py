from django.db import models
from common.models import CommonModel

# Create your models here.

# type of project is nullable as the comment


class Comment(CommonModel):
    user = models.ForeignKey(
        "users.User",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,  # OR DELETE - CLARIFY
    )
    category = models.ForeignKey(
        "categories.ProjectCategory",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    science_project = models.ForeignKey(
        "projects.ScienceProject",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    core_function_project = models.ForeignKey(
        "projects.CoreFunctionProject",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    student_project = models.ForeignKey(
        "projects.StudentProject",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    external_project = models.ForeignKey(
        "projects.ExternalProject",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    payload = models.CharField(max_length=500)
    ip_address = models.CharField(
        max_length=45,
        null=True,
        blank=True,
    )  # Will be sent from front-end
    is_public = models.BooleanField(default=True)
    is_removed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user.first_name} | {self.category}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
