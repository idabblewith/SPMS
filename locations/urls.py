from . import views
from django.urls import path

urlpatterns = [
    path("", views.ProjectAreas.as_view()),
    path("<int:pk>", views.ProjectAreaDetail.as_view()),
    path("dbcaregions", views.DBCARegions.as_view()),
    path("dbcadistricts", views.DBCADistricts.as_view()),
    path("ibra", views.Ibras.as_view()),
    path("imcra", views.Imcras.as_view()),
    path("nrm", views.Nrms.as_view()),
]
