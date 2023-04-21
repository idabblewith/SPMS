from . import views
from django.urls import path

urlpatterns = [
    path("business_areas", views.BusinessAreas.as_view()),
    path("business_areas/<int:pk>", views.BusinessAreaDetail.as_view()),
]
