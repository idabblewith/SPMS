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
    ProjectAreaSerializer,
    ProjectSerializer,
    ProjectMemberSerializer,
    TinyProjectSerializer,
    TinyResearchFunctionSerializer,
    ResearchFunctionSerializer,
)

from users.models import User
from .models import (
    Project,
    ProjectArea,
    ProjectMember,
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


class ProjectTeam(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def go(self, req, pk):
        try:
            obj = ProjectMember.objects.get(project_id=pk)
        except ProjectMember.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        team = self.go(pk)
        ser = ProjectMemberSerializer(team)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = ProjectMemberSerializer(
            data=req.data,
        )
        if ser.is_valid():
            team = ser.save()
            return Response(
                ProjectMemberSerializer(team).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                HTTP_400_BAD_REQUEST,
            )

    def delete(self, req, pk):
        team = self.go(pk)
        team.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        team = self.go(pk)
        ser = ProjectMemberSerializer(
            team,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            uteam = ser.save()
            return Response(
                ProjectMemberSerializer(uteam).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class ProjectAreas(APIView):
    def get(self, req):
        all = ProjectArea.objects.all()
        ser = ProjectAreaSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = ProjectAreaSerializer(
            data=req.data,
        )
        if ser.is_valid():
            projectarea = ser.save()
            return Response(
                ProjectAreaSerializer(projectarea).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                HTTP_400_BAD_REQUEST,
            )


class ProjectAreaDetail(APIView):
    def go(self, req, pk):
        try:
            obj = ProjectArea.objects.get(pk=pk)
        except ProjectArea.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        projarea = self.go(pk)
        ser = ProjectAreaSerializer(projarea)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        projarea = self.go(pk)
        projarea.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        projarea = self.go(pk)
        ser = ProjectAreaSerializer(
            projarea,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            uprojarea = ser.save()
            return Response(
                ProjectAreaSerializer(uprojarea).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class AreasForProject(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def go(self, req, pk):
        try:
            obj = ProjectArea.objects.get(project_id=pk)
        except ProjectArea.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        project_areas = self.go(pk)
        ser = ProjectAreaSerializer(
            project_areas,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    # def post(self, req):
    #     ser = ProjectAreaSerializer(
    #         data=req.data,
    #     )
    #     if ser.is_valid():
    #         project_area = ser.save()
    #         return Response(
    #             ProjectAreaSerializer(project_area).data,
    #             status=HTTP_201_CREATED,
    #         )
    #     else:
    #         return Response(
    #             HTTP_400_BAD_REQUEST,
    #         )

    # def delete(self, req, pk):
    #     team = self.go(pk)
    #     team.delete()
    #     return Response(
    #         status=HTTP_204_NO_CONTENT,
    #     )

    # def put(self, req, pk):
    #     team = self.go(pk)
    #     ser = ProjectAreaSerializer(
    #         team,
    #         data=req.data,
    #         partial=True,
    #     )
    #     if ser.is_valid():
    #         uteam = ser.save()
    #         return Response(
    #             ProjectAreaSerializer(uteam).data,
    #             status=HTTP_202_ACCEPTED,
    #         )
    #     else:
    #         return Response(
    #             ser.errors,
    #             status=HTTP_400_BAD_REQUEST,
    #         )


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
