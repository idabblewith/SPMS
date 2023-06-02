from rest_framework.serializers import ModelSerializer
from .models import BusinessAreaPhoto
from users.serializers import TinyUserSerializer


class BusinessAreaPhotoSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = BusinessAreaPhoto
        fields = [
            "pk",
            "file",
            "year",
            "business_area",
            "uploader",
        ]
