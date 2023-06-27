from rest_framework import serializers
from .models import Branch, BusinessArea, DepartmentalService, Agency

# from users.serializers import TinyUserSerializer


class TinyAgencySerializer(serializers.ModelSerializer):
    # Get the related image from medias.AgencyImage (as it has reverse accessor/related name of image)
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        agency_image = obj.image.first()
        if agency_image:
            return agency_image.file
        return None

    class Meta:
        model = Agency
        fields = (
            "name",
            "key_stakeholder",
            "image",
        )


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = "__all__"


class TinyBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = [
            "name",
            "manager",
        ]


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class TinyBusinessAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessArea
        fields = (
            "name",
            "slug",
            "focus",
            "introduction",
        )


class BusinessAreaSerializer(serializers.ModelSerializer):
    # creator = TinyUserSerializer(read_only=True)
    # modifier = TinyUserSerializer(
    #     # read_only=True
    # )
    # leader = TinyUserSerializer(
    #     # read_only=True
    # )
    # data_custodian = TinyUserSerializer(
    #     # read_only=True
    # )

    class Meta:
        model = BusinessArea
        fields = "__all__"


# class TinyDivisionSerializer(serializers.ModelSerializer):
#     # director = TinyUserSerializer()
#     # approver = TinyUserSerializer()

#     class Meta:
#         model = Division
#         fields = (
#             "name",
#             "slug",
#             "director",
#             "approver",
#         )


# class DivisionSerializer(serializers.ModelSerializer):
#     # creator = TinyUserSerializer(read_only=True)
#     # director = TinyUserSerializer()
#     # approver = TinyUserSerializer()  # read_only=True

#     class Meta:
#         model = Division
#         fields = "__all__"


class TinyDepartmentalServiceSerializer(serializers.ModelSerializer):
    # director = serializers.SerializerMethodField()

    # def get_director(self, obj):
    #     d = obj.image.first()
    #     if d:
    #         return d
    #     return None

    class Meta:
        model = DepartmentalService
        fields = ("name", "director")


class DepartmentalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentalService
        fields = "__all__"
