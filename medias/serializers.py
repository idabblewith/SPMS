from rest_framework.serializers import ModelSerializer
from .models import Photo
from users.serializers import TinyUserSerializer


class PhotoSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Photo
        fields = [
            "pk",
            "file",
            "description",
            "category",
            "uploader",
        ]
