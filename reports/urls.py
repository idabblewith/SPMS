from django.urls import path
from . import views

urlpatterns = [
    path("download", views.DownloadARAR.as_view()),
]
