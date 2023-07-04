from django.urls import path
from . import views

urlpatterns = [
    path("", views.Projects.as_view()),
    path("<int:pk>", views.ProjectDetail.as_view()),
    path("<int:pk>/team", views.ProjectTeam.as_view()),
    path("external", views.ExternalProjects.as_view()),
    path("student", views.StudentProjects.as_view()),
    path("science", views.ScienceProjects.as_view()),
    path("core_function", views.CoreFunctionProjects.as_view()),
    path("download", views.DownloadAllProjectsAsCSV.as_view()),
    path("research_functions", views.ResearchFunctions.as_view()),
    path("research_functions/<int:pk>", views.ResearchFunctionDetail.as_view()),
]
