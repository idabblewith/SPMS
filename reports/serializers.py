from rest_framework import serializers
from .models import ARARReport


class ARARReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ARARReport
        fields = "__all__"
