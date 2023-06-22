# BranchContactSerializer,
# TinyBranchContactSerializer,
# UserContactSerializer,
# TinyUserContactSerializer,
# AgencyContactSerializer,
# TinyAgencyContactSerializer,
# AddressSerializer,
# TinyAddressSerializer,

from rest_framework import serializers

from agencies.serializers import TinyBranchSerializer, TinyAgencySerializer
from .models import Address, AgencyContact, UserContact, BranchContact
from users.serializers import TinyUserSerializer


class TinyAddressSerializer(serializers.ModelSerializer):
    agency = TinyAgencySerializer()
    branch = TinyBranchSerializer()

    class Meta:
        model = Address
        fields = (
            "street",
            "city",
            "country",
        )


class AddressSerializer(serializers.ModelSerializer):
    agency = TinyAgencySerializer()
    branch = TinyBranchSerializer()

    class Meta:
        model = Address
        fields = "__all__"


class TinyUserContactSerializer(serializers.ModelSerializer):
    user_id = TinyUserSerializer()

    class Meta:
        model = UserContact
        fields = (
            "user_id",
            "email",
        )


class UserContactSerializer(serializers.ModelSerializer):
    user_id = TinyUserSerializer()

    class Meta:
        model = UserContact
        fields = "__all__"


class TinyAgencyContactSerializer(serializers.ModelSerializer):
    agency_id = TinyAgencySerializer()
    address = TinyAddressSerializer()

    class Meta:
        model = AgencyContact
        fields = (
            "agency_id",
            "email",
        )


class AgencyContactSerializer(serializers.ModelSerializer):
    agency_id = TinyAgencySerializer()
    address = TinyAddressSerializer()

    class Meta:
        model = AgencyContact
        fields = "__all__"


class TinyBranchContactSerializer(serializers.ModelSerializer):
    branch_id = TinyBranchSerializer()
    address = TinyAddressSerializer()

    class Meta:
        model = BranchContact
        fields = [
            "branch_id",
            "email",
        ]


class BranchContactSerializer(serializers.ModelSerializer):
    branch_id = TinyBranchSerializer()
    address = TinyAddressSerializer()

    class Meta:
        model = BranchContact
        fields = "__all__"
