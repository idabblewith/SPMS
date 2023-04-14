from django.db import models
from common.models import CommonModel


class Project(CommonModel):
    """Model Definition for Project"""

    name = models.CharField(max_length=140)
