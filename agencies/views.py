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

from .models import Branch, BusinessArea, DepartmentalService, Agency
from .serializers import (
    BranchSerializer,
    AgencySerializer,
    DepartmentalServiceSerializer,
    TinyBranchSerializer,
    TinyBusinessAreaSerializer,
    BusinessAreaSerializer,
    TinyDepartmentalServiceSerializer,
    TinyAgencySerializer,
)

# Using APIView to ensure that we can easily edit and understand the code


class Agencies(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, req):
        all = Agency.objects.all()
        ser = TinyAgencySerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = AgencySerializer(
            data=req.data,
        )
        if ser.is_valid():
            Agency = ser.save()
            return Response(
                TinyAgencySerializer(Agency).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class Branches(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, req):
        all = Branch.objects.all()
        ser = TinyBranchSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = BranchSerializer(
            data=req.data,
        )
        if ser.is_valid():
            branch = ser.save()
            return Response(
                TinyBranchSerializer(branch).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


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


# class Divisions(APIView):
#     def get(self, req):
#         all = Division.objects.all()
#         ser = TinyDivisionSerializer(
#             all,
#             many=True,
#         )
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )

#     def post(self, req):
#         ser = DivisionSerializer(
#             data=req.data,
#         )
#         if ser.is_valid():
#             div = ser.save()
#             return Response(
#                 TinyDivisionSerializer(div).data,
#                 status=HTTP_201_CREATED,
#             )
#         else:
#             return Response(
#                 ser.errors,
#                 status=HTTP_400_BAD_REQUEST,
#             )


class DepartmentalServices(APIView):
    def get(self, req):
        all = DepartmentalService.objects.all()
        ser = TinyDepartmentalServiceSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = DepartmentalServiceSerializer(
            data=req.data,
        )
        if ser.is_valid():
            service = ser.save()
            return Response(
                TinyDepartmentalServiceSerializer(service).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


# ======================================================================


class AgencyDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def go(self, pk):
        try:
            obj = Agency.objects.get(pk=pk)
        except Agency.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        Agency = self.go(pk)
        ser = AgencySerializer(Agency)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        Agency = self.go(pk)
        Agency.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        Agency = self.go(pk)
        ser = AgencySerializer(
            Agency,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated_Agency = ser.save()
            return Response(
                TinyAgencySerializer(updated_Agency).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class BranchDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def go(self, pk):
        try:
            obj = Branch.objects.get(pk=pk)
        except Branch.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        branch = self.go(pk)
        ser = BranchSerializer(branch)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        branch = self.go(pk)
        branch.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        branch = self.go(pk)
        ser = BranchSerializer(
            branch,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated_branch = ser.save()
            return Response(
                TinyBranchSerializer(updated_branch).data,
                status=HTTP_202_ACCEPTED,
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


# class DivisionDetail(APIView):
#     def go(self, req, pk):
#         try:
#             obj = Division.objects.get(pk=pk)
#         except Division.DoesNotExist:
#             raise NotFound
#         return obj

#     def get(self, req, pk):
#         div = self.go(pk)
#         ser = DivisionSerializer(div)
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )

#     def delete(self, req, pk):
#         div = self.go(pk)
#         div.delete()
#         return Response(
#             status=HTTP_204_NO_CONTENT,
#         )

#     def put(self, req, pk):
#         div = self.go(pk)
#         ser = DivisionSerializer(
#             div,
#             data=req.data,
#             partial=True,
#         )
#         if ser.is_valid():
#             udiv = ser.save()
#             return Response(
#                 TinyDivisionSerializer(udiv).data,
#                 status=HTTP_202_ACCEPTED,
#             )
#         else:
#             return Response(
#                 ser.errors,
#                 status=HTTP_400_BAD_REQUEST,
#             )


class DepartmentalServiceDetail(APIView):
    def go(self, req, pk):
        try:
            obj = DepartmentalService.objects.get(pk=pk)
        except DepartmentalService.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        service = self.go(pk)
        ser = DepartmentalServiceSerializer(service)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        service = self.go(pk)
        service.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        service = self.go(pk)
        ser = DepartmentalServiceSerializer(
            service,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            uservice = ser.save()
            return Response(
                TinyDepartmentalServiceSerializer(uservice).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )
