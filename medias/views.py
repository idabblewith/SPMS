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

from .models import Photo
from .serializers import PhotoSerializer


class PhotoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def go(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise NotFound

    def delete(self, req, pk):
        photo = self.go(pk)

        # Reject if not admin or uploader
        # if (photo.uploader.is_admin == False and photo.uploader != req.user):
        #     raise PermissionDenied
        photo.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )


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
