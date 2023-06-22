from django.db import models
from common.models import CommonModel

# Create your models here.


class Region(CommonModel):
    """
    Model Definition for Department of Biodiversity, Conservation, and Attractions Regions

    All
    Goldfields
    Kimberly
    Midwest
    Pilbara
    South Coast
    South West
    Swan
    Warren
    Wheatbelt
    """

    name = models.CharField(
        max_length=50,
    )
    value = models.CharField(
        max_length=50,
    )
    long = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    lat = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"


class District(CommonModel):
    """
    Model defintion for DBCA Districts

    All
    Albany
    Blackwood
    Central Wheatbelt
    Donnelly
    East Kimberly
    Esperance
    Exmouth
    Frankland
    Geraldton
    Goldfields
    Great Southern
    Moora
    Perth Hills
    Pilbara East
    Shark Bay
    Swan Coastal
    Wellington
    West Kimberly
    """

    name = models.CharField(
        max_length=50,
    )
    value = models.CharField(
        max_length=50,
    )
    long = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    lat = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"


class IBRARegion(CommonModel):
    """
    Model definition for IBRA Regions
    (Interim Biogeographic Regionalisation for Australia)


    All
    Avon Wheatbelt
    Dampierland
    Carnarvon
    Central Kimberly
    Central Ranges
    Coolgardie
    Esperance Plains
    Gascoyne
    Geraldton Sandplains
    Gibson Desert
    Great Sandy Desert
    Great Victoria Desert
    Hampton
    Indian Tropical Islands
    Jarrah Forest
    Little Sandy Desert
    Mallee
    Murchison
    Northern Kimberly
    Nullarbor
    Ord Victoria Plain
    Pilbara
    Swan Coastal Plain
    Tanami
    Victoria Bonaparte
    Warren
    Yalgoo
    """

    name = models.CharField(
        max_length=50,
    )
    value = models.CharField(
        max_length=50,
    )
    long = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    lat = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"


class IMCRARegion(CommonModel):
    """
    Model definition for IMCRA Regions
    (Integrated Marine and Coastal Regionalisation of Australia)

    All
    Abrolhos Islands
    Bonaparte Gulf
    Cambridge Bonaparte
    Canning
    Central West Coast
    Eighty Mile Beach
    Eucla
    Kimberly
    King Sound
    Leeuwin-Naturaliste
    Ningaloo
    Northwestern Shelf
    Oceanic Shoals
    Pilbara (Offshore)
    Pilbara (Nearshore)
    Shark Bay
    WA South Coast
    Zuytdorp
    """

    name = models.CharField(
        max_length=50,
    )
    value = models.CharField(
        max_length=50,
    )
    long = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    lat = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"


class NaturalResourceManagementRegion(CommonModel):
    """
    Model definition for Natural Resource Management Region

    All
    Ashmore and Cartier Islands
    Avon
    Christmas Islands
    Cocos Keeling Islands
    Northern Agriculrural
    Rangelands
    Southcoast
    Southwest
    Swan
    Wheatbelt
    """

    name = models.CharField(
        max_length=50,
    )
    value = models.CharField(
        max_length=50,
    )
    long = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    lat = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.name}"
