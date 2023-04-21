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
from .serializers import (
    TinyBusinessAreaSerializer,
    BusinessAreaSerializer,
    TinyDivisionSerializer,
    DivisionSerializer,
    TinyResearchFunctionSerializer,
    ResearchFunctionSerializer,
)

# Using APIView to ensure that we can easily edit and understand the code


class BusinessAreas(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, req):
        all = BusinessArea.objects.all()
        ser = TinyBusinessAreaSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = BusinessAreaSerializer(
            data=req.data,
        )
        if ser.is_valid():
            ba = ser.save()
            return Response(
                TinyBusinessAreaSerializer(ba).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
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
        ser = BusinessAreaSerializer(ba)
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
        ser = BusinessAreaSerializer(
            ba,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            uba = ser.save()
            return Response(
                TinyBusinessAreaSerializer(uba).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class Divisions(APIView):
    def get(self, req):
        all = Division.objects.all()
        ser = TinyDivisionSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = DivisionSerializer(
            data=req.data,
        )
        if ser.is_valid():
            div = ser.save()
            return Response(
                TinyDivisionSerializer(div).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class DivisionDetail(APIView):
    def go(self, req, pk):
        try:
            obj = Division.objects.get(pk=pk)
        except Division.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        div = self.go(pk)
        ser = DivisionSerializer(div)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        div = self.go(pk)
        div.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        div = self.go(pk)
        ser = DivisionSerializer(
            div,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            udiv = ser.save()
            return Response(
                TinyDivisionSerializer(udiv).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class ResearchFunctions(APIView):
    def get(self, req):
        all = ResearchFunction.objects.all()
        ser = TinyResearchFunctionSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = ResearchFunctionSerializer(
            data=req.data,
        )
        if ser.is_valid():
            rf = ser.save()
            return Response(
                rf.data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                HTTP_400_BAD_REQUEST,
            )


class ResearchFunctionDetail(APIView):
    def go(self, req, pk):
        try:
            obj = ResearchFunction.objects.get(pk=pk)
        except ResearchFunction.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        rf = self.go(pk)
        ser = ResearchFunctionSerializer(rf)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        rf = self.go(pk)
        rf.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        rf = self.go(pk)
        ser = ResearchFunctionSerializer(
            rf,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            urf = ser.save()
            return Response(
                TinyResearchFunctionSerializer(urf).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )
