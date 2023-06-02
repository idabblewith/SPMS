from django.urls import path
from . import views

urlpatterns = [
    path("photos/<int:pk>", views.BusinessAreaPhotoDetail.as_view()),
]
