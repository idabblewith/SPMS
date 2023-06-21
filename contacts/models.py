from django.db import models
from common.models import CommonModel


class Address(CommonModel):

    """
    Model Definition for addresses of entities and their branches
    """

    entity = models.ForeignKey(
        "entities.Entity",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="address",
    )
    branch = models.ForeignKey(
        "entities.Branch",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="address",
    )
    street = models.CharField(max_length=140)
    suburb = models.CharField(
        max_length=140,
        null=True,
        blank=True,
    )
    city = models.CharField(max_length=140)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=140)
    country = models.CharField(max_length=140)
    pobox = models.CharField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.street} | {self.state}"

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"


class UserContact(CommonModel):
    user_id = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="contact",
    )
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    alt_phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.user_id.username} Contact"

    class Meta:
        verbose_name = "User Contact"
        verbose_name_plural = "User Contacts"


class EntityContact(CommonModel):
    """
    Model definition for contact details of Entity
    """

    entity = models.OneToOneField(
        "entities.Entity",
        on_delete=models.CASCADE,
        related_name="contact",
    )
    email = (models.EmailField(),)
    phone = models.CharField(max_length=20)
    alt_phone = models.CharField(max_length=20)
    fax = models.CharField(max_length=20)
    address = models.ForeignKey(
        "contacts.Address",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.entity_id.name} Contact"

    class Meta:
        verbose_name = "Entity Contact"
        verbose_name_plural = "Entity Contacts"


class BranchContact(CommonModel):
    """
    Model definition for contact details of Entity Branch
    """

    branch_id = models.OneToOneField(
        "entities.Branch",
        on_delete=models.CASCADE,
        related_name="contact",
    )
    email = (models.EmailField(),)
    phone = (models.CharField(max_length=20),)
    alt_phone = (models.CharField(max_length=20),)
    fax = models.CharField(max_length=20)
    address = models.ForeignKey(
        "contacts.Address",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.branch_id.name} Contact"

    class Meta:
        verbose_name = "Branch Contact"
        verbose_name_plural = "Branch Contacts"
