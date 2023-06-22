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

from .models import UserContact, BranchContact, AgencyContact, Address
from .serializers import (
    BranchContactSerializer,
    TinyBranchContactSerializer,
    UserContactSerializer,
    TinyUserContactSerializer,
    AgencyContactSerializer,
    TinyAgencyContactSerializer,
    AddressSerializer,
    TinyAddressSerializer,
)

# Using APIView to ensure that we can easily edit and understand the code


class Addresses(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, req):
        all = Address.objects.all()
        ser = TinyAgencyContactSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = AddressSerializer(
            data=req.data,
        )
        if ser.is_valid():
            address = ser.save()
            return Response(
                TinyAddressSerializer(address).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class AgencyContacts(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, req):
        all = AgencyContact.objects.all()
        ser = TinyAgencyContactSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = AgencyContactSerializer(
            data=req.data,
        )
        if ser.is_valid():
            Agency_contact = ser.save()
            return Response(
                TinyAgencyContactSerializer(Agency_contact).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class BranchContacts(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, req):
        all = BranchContact.objects.all()
        ser = TinyBranchContactSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = BranchContactSerializer(
            data=req.data,
        )
        if ser.is_valid():
            branch_contact = ser.save()
            return Response(
                TinyBranchContactSerializer(branch_contact).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class UserContacts(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, req):
        all = UserContact.objects.all()
        ser = TinyUserContactSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = UserContactSerializer(
            data=req.data,
        )
        if ser.is_valid():
            user_contact = ser.save()
            return Response(
                TinyUserContactSerializer(user_contact).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


# ======================================================================


class AddressDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def go(self, pk):
        try:
            obj = Address.objects.get(pk=pk)
        except Address.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        address = self.go(pk)
        ser = AddressSerializer(address)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        address = self.go(pk)
        address.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        address = self.go(pk)
        ser = AddressSerializer(
            address,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated_address = ser.save()
            return Response(
                TinyAddressSerializer(updated_address).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class BranchContactDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def go(self, pk):
        try:
            obj = BranchContact.objects.get(pk=pk)
        except BranchContact.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        branch_contact = self.go(pk)
        ser = BranchContactSerializer(branch_contact)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        branch_contact = self.go(pk)
        branch_contact.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        branch_contact = self.go(pk)
        ser = BranchContactSerializer(
            branch_contact,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated_branch = ser.save()
            return Response(
                TinyBranchContactSerializer(updated_branch).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class AgencyContactDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def go(self, pk):
        try:
            obj = AgencyContact.objects.get(pk=pk)
        except AgencyContact.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        Agency_contact = self.go(pk)
        ser = AgencyContactSerializer(Agency_contact)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        Agency_contact = self.go(pk)
        Agency_contact.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        Agency_contact = self.go(pk)
        ser = AgencyContactSerializer(
            Agency_contact,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated_Agency_contact = ser.save()
            return Response(
                TinyAgencyContactSerializer(updated_Agency_contact).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class UserContactDetail(APIView):
    def go(self, req, pk):
        try:
            obj = UserContact.objects.get(pk=pk)
        except UserContact.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        uc = self.go(pk)
        ser = UserContactSerializer(uc)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        uc = self.go(pk)
        uc.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        uc = self.go(pk)
        ser = UserContactSerializer(
            uc,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated_uc = ser.save()
            return Response(
                TinyUserContactSerializer(updated_uc).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )
