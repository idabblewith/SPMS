from rest_framework.serializers import ModelSerializer, IntegerField, CharField
from .models import BusinessAreaPhoto, UserAvatar, AgencyImage, ProjectPhoto

# from users.serializers import TinyUserSerializer


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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     model = self.context.get("model")

    #     if model:
    #         if issubclass(model, BusinessAreaPhoto):
    #             self.fields["year"] = IntegerField()
    #             self.fields["business_area"] = CharField()
    #             # self.fields["uploader"] = TinyUserSerializer(read_only=True)

    # def create(self, validated_data):
    #     model = self.context.get("model")

    #     # Handle model-specific create logic if needed
    #     if model and issubclass(model, BusinessAreaPhoto):
    #         year = validated_data.pop("year")
    #         business_area = validated_data.pop("business_area")
    #         uploader = validated_data.pop("uploader")

    #         photo = BusinessAreaPhoto.objects.create(
    #             year=year, business_area=business_area, **validated_data
    #         )

    #         # Set the uploader relationship
    #         photo.uploader = uploader
    #         photo.save()

    #         return photo

    #     # Default create logic for the generic photo model
    #     return super().create(validated_data)
