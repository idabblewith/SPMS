from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import CommonModel


# WHAT COMES WITH DJANGO:
# id, password, last_login, is_superuser
# is_staff, is_active, date_joined, username,
# first_name, last_name, email,


# Add middle initials, is_external.
# is_staff set to false by default unless email ends with dpaw or dbca var
# AND ONLY WHEN MOVING DATA
# is_external set to true if same as above (no sso)

# username, last_name first_name, email == REQUIRED FOR SSO


class User(AbstractUser):
    """
    Custom User Model - references old pk for migration
    """

    # Base information

    # make user's username = to email address if none provided
    username = models.CharField(
        ("username"),
        unique=True,
        max_length=150,
        help_text=(
            "Required. 30 characters or fewer. Letters, digits and " "@/./+/-/_ only."
        ),
    )
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=("First Name"),
        help_text=("First name or given name."),
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=("Last Name"),
        help_text=("Last name or surname."),
    )
    email = models.EmailField(
        ("email address"),
        null=True,
        blank=True,
    )

    old_pk = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="Old Primary Key",
        help_text="The primary key used in the outdated SPMS",
    )

    def __str__(self) -> str:
        return f"{self.username}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class UserWork(CommonModel):
    user = models.OneToOneField(
        "users.User",
        unique=True,
        on_delete=models.CASCADE,
        related_name="work",
    )
    # Previously work_center_id
    branch = models.ForeignKey(
        "entities.Branch",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    # Previously program_id
    business_area = models.ForeignKey(
        "entities.BusinessArea",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.user_id} | Work Detail"

    class Meta:
        verbose_name = "User Work Detail"
        verbose_name_plural = "User Work Details"


class UserProfile(CommonModel):
    class TitleChoices(models.TextChoices):
        MR = "mr", "Mr."
        MS = "ms", "Ms."
        MRS = "mrs", "Mrs."
        MAS = "master", "Master"
        DR = "dr", "Dr."

    class RoleChoices(models.TextChoices):
        ECODEV = "Ecoinformatics Developer", "Ecoinformatics Developer"
        EXECDIR = "Executive Director", "Executive Director"
        ASSEXECDIR = "Assistant Executive Director", "Assistant Executive Director"
        BALEAD = "Business Area Leader", "Business Area Leader"
        ADMIN = "Admin", "Admin"
        DBCA = "DBCA Member", "DBCA Member"
        EXTERNAL = "External User", "External User"

    user = models.OneToOneField(
        "users.User",
        unique=True,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    role = models.CharField(
        max_length=30,
        default=RoleChoices.EXTERNAL,
    )
    title = models.CharField(
        choices=TitleChoices.choices,
        max_length=20,
        null=True,
        blank=True,
    )
    profile_text = models.TextField(
        null=True,
        blank=True,
    )
    curriculum_vitae = models.FileField(
        null=True,
        blank=True,
    )
    expertise = models.CharField(
        max_length=140,
        null=True,
        blank=True,
    )
    member_of = models.ForeignKey(
        "entities.Entity",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    image = models.ForeignKey(
        "medias.UserAvatar",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    # is_group,
    # affiliation

    def __str__(self) -> str:
        return f"{self.user_id} | Profile"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


# THEREFORE, WHAT NEEDS TO BE ADDED:
# old_pk
# projects, author_code,
# publications_staff, publications_other,
# is_external, agreed,
#
