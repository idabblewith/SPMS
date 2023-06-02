from django.http import HttpResponse
from django.shortcuts import render
from .models import ARARReport
from .serializers import ARARReportSerializer

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
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.utils import timezone
from django.db import transaction
from django.conf import settings

from medias.serializers import BusinessAreaPhotoSerializer

import time

# Create your views here.


class DownloadARAR(APIView):
    def get(self, req):
        pass
        # try:
        #     # Retrieve projects data from the database
        #     core_projects = CoreFunctionProject.objects.all()

        #     # Create a response object with CSV content type
        #     res = HttpResponse(content_type="text/csv")
        #     res["Content-Disposition"] = 'attachment; filename="projects.csv"'

        #     # Create a CSV writer
        #     writer = csv.writer(res)
        #     writer.writerow(["-----", "Core Function Projects", "-----"])

        #     # Get field names (CoreFunctionProject)
        #     core_field_names = [
        #         field.name for field in CoreFunctionProject._meta.fields
        #     ]

        #     # Write CSV headers (CoreFunctionProject)
        #     writer.writerow(core_field_names)
        #     # print(res.data)

        #     # Write project data rows
        #     for project in core_projects:
        #         row = [getattr(project, field) for field in core_field_names]
        #         writer.writerow(row)

        #     # Add an empty row for separation
        #     writer.writerow([])
        #     writer.writerow(["-----", "Science Projects", "-----"])

        #     science_projects = ScienceProject.objects.all()

        #     # Get field names (ScienceProject)
        #     science_field_names = [field.name for field in ScienceProject._meta.fields]

        #     # Write CSV headers for (Science Project)
        #     writer.writerow(science_field_names)

        #     # Write project data rows
        #     for project in science_projects:
        #         row = [getattr(project, field) for field in science_field_names]
        #         writer.writerow(row)

        #     # Add an empty row for separation
        #     writer.writerow([])
        #     writer.writerow(["-----", "Student Projects", "-----"])

        #     student_projects = StudentProject.objects.all()

        #     # Get field names (StudentProject)
        #     student_field_names = [field.name for field in StudentProject._meta.fields]

        #     # Write CSV headers (StudentProject)
        #     writer.writerow(student_field_names)

        #     # Write project data rows
        #     for project in student_projects:
        #         row = [getattr(project, field) for field in student_field_names]
        #         writer.writerow(row)

        #     # Add an empty row for separation
        #     writer.writerow([])
        #     writer.writerow(["-----", "External Projects", "-----"])

        #     external_projects = ExternalProject.objects.all()

        #     # Get field names (ExternalProject)
        #     external_field_names = [
        #         field.name for field in ExternalProject._meta.fields
        #     ]

        #     # Write CSV headers (StudentProject)
        #     writer.writerow(external_field_names)

        #     # Write project data rows
        #     for project in external_projects:
        #         row = [getattr(project, field) for field in external_field_names]
        #         writer.writerow(row)

        #     return res

        # # If server is down or otherwise error
        # except Exception as e:
        #     print(e)
        #     return HttpResponse(status=500, content="Error generating CSV")


class Reports(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def go(self, pk):
        try:
            obj = ARARReport.objects.get(pk=pk)
        except ARARReport.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req):
        all_reports = ARARReport.objects.all()
        ser = ARARReportSerializer(
            all_reports,
            many=True,
            context={"request": req},
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    # def post(self, req):
    #     ser = ARARReportSerializer(
    #         data=req.data,
    #     )
    #     if ser.is_valid(

    #     )
