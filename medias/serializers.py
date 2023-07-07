from rest_framework.serializers import ModelSerializer
from .models import (
    AnnualReportImage,
    BusinessAreaPhoto,
    ReportPDF,
    UserAvatar,
    AgencyImage,
    ProjectPhoto,
)


class ReportPDFSerializer(ModelSerializer):
    class Meta:
        model = ReportPDF
        fields = [
            "pk",
            "year",
            "file",
            "created_at",
        ]


class AnnualReportImageSerializer(ModelSerializer):
    class Meta:
        model = AnnualReportImage
        fields = [
            "pk",
            "year",
            "kind",
            "file",
            "uploader",
        ]


class BusinessAreaPhotoSerializer(ModelSerializer):
    # user = TinyUserSerializer(read_only=True)

    class Meta:
        model = BusinessAreaPhoto
        fields = [
            "pk",
            "file",
            "year",
            "business_area",
            "uploader",
        ]


class UserAvatarSerializer(ModelSerializer):
    # user = TinyUserSerializer()
    class Meta:
        model = UserAvatar
        fields = [
            "pk",
            "file",
            "user",
        ]


class ProjectImageSerializer(ModelSerializer):
    class Meta:
        model = ProjectPhoto
        fields = [
            "pk",
            "file",
        ]


class AgencyImageSerializer(ModelSerializer):
    # user = TinyUserSerializer()
    class Meta:
        model = AgencyImage
        fields = [
            "pk",
            "file",
            "agency",
        ]
