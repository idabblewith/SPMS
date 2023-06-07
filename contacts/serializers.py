# BranchContactSerializer,
# TinyBranchContactSerializer,
# UserContactSerializer,
# TinyUserContactSerializer,
# EntityContactSerializer,
# TinyEntityContactSerializer,
# AddressSerializer,
# TinyAddressSerializer,

from rest_framework import serializers

from entities.serializers import TinyBranchSerializer, TinyEntitySerializer
from .models import Address, EntityContact, UserContact, BranchContact
from users.serializers import TinyUserSerializer


class TinyAddressSerializer(serializers.ModelSerializer):
    entity = TinyEntitySerializer()
    branch = TinyBranchSerializer()

    class Meta:
        model = Address
        fields = (
            "street",
            "city",
            "country",
        )


class AddressSerializer(serializers.ModelSerializer):
    entity = TinyEntitySerializer()
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


class TinyEntityContactSerializer(serializers.ModelSerializer):
    entity_id = TinyEntitySerializer()
    address = TinyAddressSerializer()

    class Meta:
        model = EntityContact
        fields = (
            "entity_id",
            "email",
        )


class EntityContactSerializer(serializers.ModelSerializer):
    entity_id = TinyEntitySerializer()
    address = TinyAddressSerializer()

    class Meta:
        model = EntityContact
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
