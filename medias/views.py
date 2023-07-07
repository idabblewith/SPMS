from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import render
from django.db import transaction
from django.conf import settings
from django.utils import timezone

import requests
import time

from .models import BusinessAreaPhoto
from .serializers import BusinessAreaPhotoSerializer


# ==================================================================================================


class GetUploadURL(APIView):
    def post(self, req):
        # UPDATE WITH AZURE STYLE
        pass
        # # f"https://api.cloudflare.com/client/v4/accounts/{settings.CF_ID}/images/v1"

        # url = f"https://api.cloudflare.com/client/v4/accounts/{settings.CF_ID}/images/v2/direct_upload"
        # one_time_url = requests.post(
        #     url,
        #     headers={
        #         "Authorization": f"Bearer {settings.CF_IMAGES_TOKEN}",
        #         # "Content-Type": "multipart/form-data",
        #     },
        # )
        # one_time_url = one_time_url.json()
        # result = one_time_url.get("result")
        # print(result)
        # return Response(
        #     {
        #         "uploadURL": result.get("uploadURL"),
        #     }
        # )


# ==================================================================================================


# class BusinessAreaPhotos(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, req):
#         pass

#     def post(self, req):
#         pass


class BusinessAreaPhotoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def go(self, pk):
        try:
            return BusinessAreaPhoto.objects.get(pk=pk)
        except BusinessAreaPhoto.DoesNotExist:
            raise NotFound

    def delete(self, req, pk):
        business_photo = self.go(pk)

        if (
            business_photo.uploader.is_admin == False
            and business_photo.uploader != req.user
        ):
            raise PermissionDenied
        business_photo.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )
