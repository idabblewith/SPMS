from django.db import models

from common.models import CommonModel

# Create your models here.


class StatusChoices(models.TextChoices):
    TODO = "todo", "To Do"
    INPROGRESS = "inprogress", "In Progress"
    DONE = "done", "Done"


class PersonalTask(CommonModel):
    user_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="personal_tasks",
    )
    name = models.CharField(
        max_length=50,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.user_id} | {self.name}"

    class Meta:
        verbose_name = "Personal Task"
        verbose_name_plural = "Personal Tasks"


class ProjectTask(CommonModel):
    user_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="personal_tasks",
    )
    project_id = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="project_tasks",
    )
    name = models.CharField(
        max_length=50,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    notes = models.TextField(
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
    )

    def __str__(self) -> str:
        return f"{self.project_id} - {self.user_id} | {self.name}"

    class Meta:
        verbose_name = "Project Task"
        verbose_name_plural = "Project Tasks"
