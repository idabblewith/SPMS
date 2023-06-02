from django.urls import path
from . import views

urlpatterns = [
    path("download", views.DownloadAllProjectsAsCSV.as_view()),
    path("external", views.ExternalProjects.as_view()),
    path("external/<int:pk>", views.ExternalProjectDetail.as_view()),
    path("student", views.StudentProjects.as_view()),
    path("student/<int:pk>", views.StudentProjectDetail.as_view()),
    path("science", views.ScienceProjects.as_view()),
    path("science/<int:pk>", views.ScienceProjectDetail.as_view()),
    path("core_function", views.CoreFunctionProjects.as_view()),
    path("core_function/<int:pk>", views.CoreFunctionProjectDetail.as_view()),
]
