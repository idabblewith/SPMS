from django.db import models
from common.models import CommonModel

# from django.contrib.gis.db.models.fields import MultiPolygonField

# Create your models here.


class ProjectArea(CommonModel):
    """
    Model Definition for Areas Project exist in
    """

    class AreaTypeChoices(models.TextChoices):
        AREA_TYPE_RELEVANT = "relevantarea", "Relevant Area"
        # AREA_TYPE_FIELDWORK = "fieldworkarea", "Fieldwork Area"
        AREA_TYPE_DBCA_REGION = "dbcaregion", "DBCA Region"  # Changed from DPAW_REGION
        AREA_TYPE_DBCA_DISTRICT = (
            "dbcadistrict",
            "DBCA District",
        )  # Changed from DPAW_DISTRICT
        AREA_TYPE_IBRA_REGION = (
            "ibra",
            "IBRA Region (Interim Biogeographic Regionalisation for Australia)",
        )
        AREA_TYPE_IMCRA_REGION = (
            "imcra",
            "IMCRA Region (Integrated Marine and Coastal Regionalisation of Australia)",
        )
        AREA_TYPE_NRM_REGION = "nrm", "Natural Resource Management Region"

    # AREA_TYPE_RELEVANT = 1
    # AREA_TYPE_FIELDWORK = 2
    # AREA_TYPE_DPAW_REGION = 3
    # AREA_TYPE_DPAW_DISTRICT = 4
    # AREA_TYPE_IBRA_REGION = 5
    # AREA_TYPE_IMCRA_REGION = 6
    # AREA_TYPE_NRM_REGION = 7

    name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        help_text="A human-readable, short but descriptive name.",
    )

    area_type = models.CharField(
        max_length=25,
        verbose_name="Area Type",
        choices=AreaTypeChoices.choices,
        default=AreaTypeChoices.AREA_TYPE_RELEVANT,
    )

    source_id = models.PositiveIntegerField(
        blank=True,
        null=True,
        help_text="The Source ID",
    )

    # northern_extend = models.FloatField(
    #     blank=True,
    #     null=True,
    #     help_text="The maximum northern extent of an Area,useful for sorting by geographic latitude.",
    # )

    # Changed from 'mpoly'
    # spatial_extent = MultiPolygonField(
    #     blank=True,
    #     null=True,
    #     srid=4326,
    #     verbose_name="Spacial Extent",
    #     help_text="The spatial extent of this locaiton, stored as WKT",
    # )

    old_id = models.IntegerField()

    class Meta:
        verbose_name = "Project Area"
        verbose_name_plural = "Project Areas"

    def __str__(self) -> str:
        return self.name

    def get_northern_extent(self):
        return self.spatial_extent.extent[3] if self.spatial_extent else None

    # area_type = models.


class DBCARegion(CommonModel):
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
