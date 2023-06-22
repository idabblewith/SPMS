from rest_framework import serializers
from .models import Branch, BusinessArea, Division, Agency, ResearchFunction

# from users.serializers import TinyUserSerializer


class TinyAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = (
            "name",
            "key_stakeholder",
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


class TinyDivisionSerializer(serializers.ModelSerializer):
    # director = TinyUserSerializer()
    # approver = TinyUserSerializer()

    class Meta:
        model = Division
        fields = (
            "name",
            "slug",
            "director",
            "approver",
        )


class DivisionSerializer(serializers.ModelSerializer):
    # creator = TinyUserSerializer(read_only=True)
    # director = TinyUserSerializer()
    # approver = TinyUserSerializer()  # read_only=True

    class Meta:
        model = Division
        fields = "__all__"


class TinyResearchFunctionSerializer(serializers.ModelSerializer):
    # leader = TinyUserSerializer()

    class Meta:
        model = ResearchFunction
        fields = (
            "name",
            "description",
            "leader",
            "association",
        )


class ResearchFunctionSerializer(serializers.ModelSerializer):
    # creator = TinyUserSerializer(read_only=True)
    # leader = TinyUserSerializer()

    class Meta:
        model = ResearchFunction
        fields = "__all__"
