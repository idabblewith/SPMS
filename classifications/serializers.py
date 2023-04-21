from rest_framework import serializers
from .models import BusinessArea, Division, ResearchFunction
from users.serializers import TinyUserSerializer


class SimpleBusinessAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessArea
        fields = (
            "name",
            "slug",
            "focus",
            "introduction",
        )


class FullBusinessAreaSerializer(serializers.ModelSerializer):
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
