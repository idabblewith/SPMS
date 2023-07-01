from rest_framework.serializers import ModelSerializer, IntegerField, CharField
from .models import Area


class TinyAreaSerializer(ModelSerializer):
    # user = TinyUserSerializer()
    class Meta:
        model = Area
        fields = [
            "pk",
            "name",
            "area_type",
            "old_id",
        ]


class AreaSerializer(ModelSerializer):
    # user = TinyUserSerializer()
    class Meta:
        model = Area
        fields = "__all__"
