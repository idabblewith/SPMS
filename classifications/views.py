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
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render
from django.db import transaction
from django.conf import settings
from django.utils import timezone

import time

from .models import BusinessArea, Division, ResearchFunction
from .serializers import SimpleBusinessAreaSerializer, FullBusinessAreaSerializer

# Using APIView to ensure that we can easily edit and understand the code


class BusinessAreas(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, req):
        all = BusinessArea.objects.all()
        ser = SimpleBusinessAreaSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = FullBusinessAreaSerializer(
            data=req.data,
        )
        if ser.is_valid():
            ba = ser.save()
            return Response(
                SimpleBusinessAreaSerializer(ba).data,
                status=HTTP_201_CREATED,
            )


class BusinessAreaDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def go(self, pk):
        try:
            obj = BusinessArea.objects.get(pk=pk)
        except BusinessArea.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        ba = self.go(pk)
        ser = FullBusinessAreaSerializer(ba)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        ba = self.go(pk)
        ba.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        ba = self.go(pk)
        ser = FullBusinessAreaSerializer(
            ba,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            uba = ser.save()
            return Response(
                SimpleBusinessAreaSerializer(uba).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                status=HTTP_400_BAD_REQUEST,
            )
