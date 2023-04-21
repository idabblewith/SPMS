from rest_framework import serializers
from .models import BusinessArea, Division, ResearchFunction
from users.serializers import TinyUserSerializer


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
    creator = TinyUserSerializer(read_only=True)
    modifier = TinyUserSerializer(
        # read_only=True
    )
    leader = TinyUserSerializer(
        # read_only=True
    )
    data_custodian = TinyUserSerializer(
        # read_only=True
    )

    class Meta:
        model = BusinessArea
        fields = "__all__"


class TinyDivisionSerializer(serializers.ModelSerializer):
    director = TinyUserSerializer()
    approver = TinyUserSerializer()

    class Meta:
        model = Division
        fields = (
            "name",
            "slug",
            "director",
            "approver",
        )


class DivisionSerializer(serializers.ModelSerializer):
    creator = TinyUserSerializer(read_only=True)
    director = TinyUserSerializer()
    approver = TinyUserSerializer()  # read_only=True

    class Meta:
        model = Division
        fields = "__all__"


class TinyResearchFunctionSerializer(serializers.ModelSerializer):
    leader = TinyUserSerializer()

    class Meta:
        model = ResearchFunction
        fields = (
            "name",
            "description",
            "leader",
            "association",
        )


class ResearchFunctionSerializer(serializers.ModelSerializer):
    creator = TinyUserSerializer(read_only=True)
    leader = TinyUserSerializer()

    class Meta:
        model = ResearchFunction
        fields = "__all__"
