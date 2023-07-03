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
from math import ceil
from django.db.models import Q

import time
from django.http import HttpResponse

from .serializers import (
    # TinyCoreFunctionProjectSerializer,
    # CoreFunctionProjectSerializer,
    # TinyExternalProjectSerializer,
    # ExternalProjectSerializer,
    # TinyScienceProjectSerializer,
    # ScienceProjectSerializer,
    # TinyStudentProjectSerializer,
    # StudentProjectSerializer,
    ProjectSerializer,
    TinyProjectSerializer,
    TinyResearchFunctionSerializer,
    ResearchFunctionSerializer,
)

from users.models import User
from .models import (
    Project,
    ResearchFunction,
)
import csv


class DownloadAllProjectsAsCSV(APIView):
    def get(self, req):
        # TODO: Make it join with the other project-related tables.
        try:
            # Retrieve projects data from the database
            projects = Project.objects.all()

            # Create a response object with CSV content type
            res = HttpResponse(content_type="text/csv")
            res["Content-Disposition"] = 'attachment; filename="projects.csv"'

            # Create a CSV writer
            writer = csv.writer(res)
            # writer.writerow(["-----", "Projects", "-----"])

            # Get field names
            field_names = [field.name for field in Project._meta.fields]

            # Write CSV headers (CoreFunctionProject)
            writer.writerow(field_names)
            # print(res.data)

            # Write project data rows
            for project in projects:
                row = [getattr(project, field) for field in field_names]
                writer.writerow(row)

            return res

        # If server is down or otherwise error
        except Exception as e:
            print(e)
            return HttpResponse(status=500, content="Error generating CSV")


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
                TinyResearchFunctionSerializer(rf).data,
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


class Projects(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        # TODO: Also get by Business Area and categorize the projects into
        # Business Area arrays and send back an array of ba arrays containing the projects.
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            # If the user sends a non-integer value as the page parameter
            page = 1

        page_size = 12
        # settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        search_term = request.GET.get("searchTerm")

        # Get the values of the checkboxes
        only_active = bool(request.GET.get("only_active", False))
        only_inactive = bool(request.GET.get("only_inactive", False))
        ba_slug = request.GET.get("businessarea", "All")

        if ba_slug != "All":
            projects = Project.objects.filter(business_area__slug=ba_slug)
        else:
            projects = Project.objects.all()

        # Interaction logic between checkboxes
        if only_active:
            only_inactive = False
        elif only_inactive:
            only_active = False

        if search_term:
            projects = projects.filter(
                Q(title__icontains=search_term)
                | Q(description__icontains=search_term)
                | Q(tagline__icontains=search_term)
                | Q(keywords__icontains=search_term)
            )

        # Filter projects based on checkbox values (this checks whether in an array of status' considered
        # active)

        if only_active:
            projects = projects.filter(status__in=Project.ACTIVE_ONLY)
        elif only_inactive:
            projects = projects.exclude(status__in=Project.ACTIVE_ONLY)

        # # Sort projects alphabetically based on title
        # projects = projects.order_by("title")

        total_projects = projects.count()
        total_pages = ceil(total_projects / page_size)

        serialized_projects = ProjectSerializer(
            projects[start:end],
            many=True,
            context={
                "request": request,
                "projects": projects[start:end],
            },
        )

        response_data = {
            "projects": serialized_projects.data,
            "total_pages": total_pages,
        }

        return Response(response_data, status=HTTP_200_OK)

    def post(self, req):
        ser = ProjectSerializer(
            data=req.data,
        )
        if ser.is_valid():
            proj = ser.save()
            return Response(
                TinyProjectSerializer(proj).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                HTTP_400_BAD_REQUEST,
            )


class ProjectDetail(APIView):
    def go(self, req, pk):
        try:
            obj = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        proj = self.go(pk)
        ser = ProjectSerializer(proj)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        proj = self.go(pk)
        proj.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        proj = self.go(pk)
        ser = ProjectSerializer(
            proj,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            uproj = ser.save()
            return Response(
                TinyProjectSerializer(uproj).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


# GETS
class CoreFunctionProjects(APIView):
    def get(self, req):
        all = Project.objects.filter(kind="core_function").all()
        ser = TinyProjectSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )


class ScienceProjects(APIView):
    def get(self, req):
        all = Project.objects.filter(kind="science").all()
        ser = TinyProjectSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )


class StudentProjects(APIView):
    def get(self, req):
        all = Project.objects.filter(kind="student").all()
        ser = TinyProjectSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )


class ExternalProjects(APIView):
    def get(self, req):
        all = Project.objects.filter(kind="external").all()
        ser = TinyProjectSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )


# class CoreFunctionProjects(APIView):
#     def get(self, req):
#         all = CoreFunctionProject.objects.all()
#         ser = TinyCoreFunctionProjectSerializer(
#             all,
#             many=True,
#         )
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )

#     def post(self, req):
#         ser = CoreFunctionProjectSerializer(data=req.data)
#         if ser.is_valid():
#             cf = ser.save()
#             return Response(
#                 TinyCoreFunctionProjectSerializer(cf).data,
#                 status=HTTP_201_CREATED,
#             )
#         else:
#             return Response(
#                 ser.errors,
#                 status=HTTP_400_BAD_REQUEST,
#             )


# class CoreFunctionProjectDetail(APIView):
#     def go(self, req, pk):
#         try:
#             obj = CoreFunctionProject.objects.get(pk=pk)
#         except CoreFunctionProject.DoesNotExist:
#             raise NotFound
#         return obj

#     def get(self, req, pk):
#         cf = self.go(pk)
#         ser = CoreFunctionProjectSerializer(cf)
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )

#     def delete(self, req, pk):
#         cf = self.go(pk)
#         cf.delete()
#         return Response(
#             status=HTTP_204_NO_CONTENT,
#         )

#     def put(self, req, pk):
#         cf = self.go(pk)
#         ser = CoreFunctionProjectSerializer(
#             cf,
#             data=req.data,
#             partial=True,
#         )
#         if ser.is_valid():
#             updated = ser.save()
#             return Response(
#                 TinyCoreFunctionProjectSerializer(updated).data,
#                 status=HTTP_202_ACCEPTED,
#             )
#         else:
#             return Response(
#                 ser.errors,
#                 status=HTTP_400_BAD_REQUEST,
#             )


# class StudentProjects(APIView):
#     def get(self, req):
#         all = StudentProject.objects.all()
#         ser = StudentProjectSerializer(
#             all,
#             many=True,
#         )
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )

#     def post(self, req):
#         ser = StudentProjectSerializer(data=req.data)
#         if ser.is_valid():
#             sp = ser.save()
#             return Response(
#                 TinyStudentProjectSerializer(sp).data,
#                 status=HTTP_201_CREATED,
#             )
#         else:
#             return Response(
#                 ser.errors,
#                 status=HTTP_400_BAD_REQUEST,
#             )


# class StudentProjectDetail(APIView):
#     def go(self, req, pk):
#         try:
#             obj = StudentProject.objects.get(pk=pk)
#         except StudentProject.DoesNotExist:
#             raise NotFound
#         return obj

#     def get(self, req, pk):
#         sp = self.go(pk)
#         ser = StudentProjectSerializer(sp)
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )

#     def delete(self, req, pk):
#         sp = self.go(pk)
#         sp.delete()
#         return Response(
#             status=HTTP_204_NO_CONTENT,
#         )

#     def put(self, req, pk):
#         sp = self.go(pk)
#         ser = StudentProjectSerializer(
#             sp,
#             data=req.data,
#             partial=True,
#         )
#         if ser.is_valid():
#             updated = ser.save()
#             return Response(
#                 TinyStudentProjectSerializer(updated).data,
#                 status=HTTP_202_ACCEPTED,
#             )
#         else:
#             return Response(
#                 ser.errors,
#                 status=HTTP_400_BAD_REQUEST,
#             )


# class ExternalProjects(APIView):
#     def get(self, req):
#         all = ExternalProject.objects.all()
#         ser = ExternalProjectSerializer(
#             all,
#             many=True,
#         )
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )

#     def post(self, req):
#         ser = ExternalProjectSerializer(data=req.data)
#         if ser.is_valid():
#             ep = ser.save()
#             return Response(
#                 TinyExternalProjectSerializer(ExternalProject).data,
#                 status=HTTP_201_CREATED,
#             )
#         else:
#             return Response(
#                 ser.errors,
#                 status=HTTP_400_BAD_REQUEST,
#             )


# class ExternalProjectDetail(APIView):
#     def go(self, req, pk):
#         try:
#             obj = ExternalProject.objects.get(pk=pk)
#         except ExternalProject.DoesNotExist:
#             raise NotFound
#         return obj

#     def get(self, req, pk):
#         ep = self.go(pk)
#         ser = ExternalProjectSerializer(ep)
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )

#     def delete(self, req, pk):
#         ep = self.go(pk)
#         ep.delete()
#         return Response(
#             status=HTTP_204_NO_CONTENT,
#         )

#     def put(self, req, pk):
#         ep = self.go(pk)
#         ser = ExternalProjectSerializer(
#             ep,
#             data=req.data,
#             partial=True,
#         )
#         if ser.is_valid():
#             updated = ser.save()
#             return Response(
#                 TinyExternalProjectSerializer(updated).data,
#                 status=HTTP_202_ACCEPTED,
#             )
#         else:
#             return Response(
#                 ser.errors,
#                 status=HTTP_400_BAD_REQUEST,
#             )


# class ScienceProjects(APIView):
#     def get(self, req):
#         all = ScienceProject.objects.all()
#         ser = ScienceProjectSerializer(
#             all,
#             many=True,
#         )
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )

#     def post(self, req):
#         ser = ScienceProjectSerializer(data=req.data)
#         if ser.is_valid():
#             sp = ser.save()
#             return Response(
#                 TinyScienceProjectSerializer(sp).data,
#                 status=HTTP_201_CREATED,
#             )
#         else:
#             return Response(
#                 ser.errors,
#                 status=HTTP_400_BAD_REQUEST,
#             )


# class ScienceProjectDetail(APIView):
#     def go(self, req, pk):
#         try:
#             obj = ScienceProject.objects.get(pk=pk)
#         except ScienceProject.DoesNotExist:
#             raise NotFound
#         return obj

#     def get(self, req, pk):
#         sp = self.go(pk)
#         ser = ScienceProjectSerializer(sp)
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )

#     def delete(self, req, pk):
#         sp = self.go(pk)
#         sp.delete()
#         return Response(
#             status=HTTP_204_NO_CONTENT,
#         )

#     def put(self, req, pk):
#         sp = self.go(pk)
#         ser = ScienceProjectSerializer(
#             sp,
#             data=req.data,
#             partial=True,
#         )
#         if ser.is_valid():
#             updated = ser.save()
#             return Response(
#                 TinyScienceProjectSerializer(updated).data,
#                 status=HTTP_202_ACCEPTED,
#             )
#         else:
#             return Response(
#                 ser.errors,
#                 status=HTTP_400_BAD_REQUEST,
#             )
