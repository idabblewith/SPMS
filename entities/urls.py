from . import views
from django.urls import path

urlpatterns = [
    path("", views.Entities.as_view()),
    path("<int:pk>", views.EntityDetail.as_view()),
    path("branches", views.Branches.as_view()),
    path("branches/<int:pk>", views.BranchDetail.as_view()),
    path("business_areas", views.BusinessAreas.as_view()),
    path("business_areas/<int:pk>", views.BusinessAreaDetail.as_view()),
    path("divisions", views.Divisions.as_view()),
    path("divisions/<int:pk>", views.DivisionDetail.as_view()),
    path("research_functions", views.ResearchFunctions.as_view()),
    path("research_functions/<int:pk>", views.ResearchFunctionDetail.as_view()),
]
