from django.db import models

from common.models import CommonModel

# Create your models here.


class StatusChoices(models.TextChoices):
    TODO = "todo", "To Do"
    INPROGRESS = "inprogress", "In Progress"
    DONE = "done", "Done"


class ProjectTaskCategories(models.TextChoices):
    pass


class ProjectTaskChoices(models.TextChoices):
    # TODO: Make deletion of projects limited to creator, directorate and admins
    # TODO: Make the deletion require project leader approval - submitted for deletion
    # TODO: Make the final deletion require directorate approval - submitted for deletion
    # TODO: Have users type in the name of the project next to the delete button (like gh)
    # to prevent errors.

    # PROJECT OWNERS

    # Add team members: A task given to users who start a new project.
    # The user who started the project will be auto added, and the task
    # will remain in the todo category unless more members are added or
    # the user manually moves the card.
    ADDTEAM = "addteam", "Add Team"
    AUTHORDOC = "authordoc", "Author Document"

    # Document Specific

    # User Initiated (Actions)
    SEEKAPPROVAL = "seekapproval", "Seek Approval"
    APPROVE = "approve", "Approve"  # Approve document
    DENY = "deny", "Deny"  # Deny document
    RECALL = "recall", "Recall"  # Recall from approval
    REQAUTHREV = "requestauthorrevision", "Request Author Revision"
    REQREVREV = "requestreviewerrevision", "Request Reviewer Revision"

    # System Issued
    REVIEW = "review", "Review"  # Asses document, and approve or deny.
    REVISE = "revise", "Revise"  # Revise document


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
