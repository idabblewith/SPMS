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

from .models import ScienceProject, StudentProject, ExternalProject, CoreFunctionProject
from .serializers import (
    TinyCoreFunctionProjectSerializer,
    CoreFunctionProjectSerializer,
    TinyExternalProjectSerializer,
    ExternalProjectSerializer,
    TinyScienceProjectSerializer,
    ScienceProjectSerializer,
    TinyStudentProjectSerializer,
    StudentProjectSerializer,
)

from users.models import User


class DownloadAllProjects(APIView):
    def get_user(self, req, pk):
        try:
            obj = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound
        return obj

    def post(self, req):
        # user = self.get_user(pk=req.data.userID)
        print(req.data)
        # print(user)
        # pass


class CoreFunctionProjects(APIView):
    def get(self, req):
        all = CoreFunctionProject.objects.all()
        ser = TinyCoreFunctionProjectSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = CoreFunctionProjectSerializer(data=req.data)
        if ser.is_valid():
            cf = ser.save()
            return Response(
                TinyCoreFunctionProjectSerializer(cf).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class CoreFunctionProjectDetail(APIView):
    def go(self, req, pk):
        try:
            obj = CoreFunctionProject.objects.get(pk=pk)
        except CoreFunctionProject.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        cf = self.go(pk)
        ser = CoreFunctionProjectSerializer(cf)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        cf = self.go(pk)
        cf.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        cf = self.go(pk)
        ser = CoreFunctionProjectSerializer(
            cf,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated = ser.save()
            return Response(
                TinyCoreFunctionProjectSerializer(updated).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class StudentProjects(APIView):
    def get(self, req):
        all = StudentProject.objects.all()
        ser = StudentProjectSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = StudentProjectSerializer(data=req.data)
        if ser.is_valid():
            sp = ser.save()
            return Response(
                TinyStudentProjectSerializer(sp).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class StudentProjectDetail(APIView):
    def go(self, req, pk):
        try:
            obj = StudentProject.objects.get(pk=pk)
        except StudentProject.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        sp = self.go(pk)
        ser = StudentProjectSerializer(sp)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        sp = self.go(pk)
        sp.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        sp = self.go(pk)
        ser = StudentProjectSerializer(
            sp,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated = ser.save()
            return Response(
                TinyStudentProjectSerializer(updated).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class ExternalProjects(APIView):
    def get(self, req):
        all = ExternalProject.objects.all()
        ser = ExternalProjectSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = ExternalProjectSerializer(data=req.data)
        if ser.is_valid():
            ep = ser.save()
            return Response(
                TinyExternalProjectSerializer(ExternalProject).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class ExternalProjectDetail(APIView):
    def go(self, req, pk):
        try:
            obj = ExternalProject.objects.get(pk=pk)
        except ExternalProject.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        ep = self.go(pk)
        ser = ExternalProjectSerializer(ep)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        ep = self.go(pk)
        ep.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        ep = self.go(pk)
        ser = ExternalProjectSerializer(
            ep,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated = ser.save()
            return Response(
                TinyExternalProjectSerializer(updated).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class ScienceProjects(APIView):
    def get(self, req):
        all = ScienceProject.objects.all()
        ser = ScienceProjectSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = ScienceProjectSerializer(data=req.data)
        if ser.is_valid():
            sp = ser.save()
            return Response(
                TinyScienceProjectSerializer(sp).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class ScienceProjectDetail(APIView):
    def go(self, req, pk):
        try:
            obj = ScienceProject.objects.get(pk=pk)
        except ScienceProject.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        sp = self.go(pk)
        ser = ScienceProjectSerializer(sp)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        sp = self.go(pk)
        sp.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        sp = self.go(pk)
        ser = ScienceProjectSerializer(
            sp,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated = ser.save()
            return Response(
                TinyScienceProjectSerializer(updated).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )
