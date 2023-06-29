from rest_framework.serializers import ModelSerializer, IntegerField, CharField
from .models import ProjectArea


class TinyProjectAreaSerializer(ModelSerializer):
    # user = TinyUserSerializer()
    class Meta:
        model = ProjectArea
        fields = [
            "pk",
            "name",
            "area_type",
            "old_id",
        ]


class ProjectAreaSerializer(ModelSerializer):
    # user = TinyUserSerializer()
    class Meta:
        model = ProjectArea
        fields = "__all__"
