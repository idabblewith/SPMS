from rest_framework import serializers
from .models import AnnualReport


class AnnualReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualReport
        fields = "__all__"
