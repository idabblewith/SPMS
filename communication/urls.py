from django.urls import path
from . import views

urlpatterns = [
    path("comments", views.Comments.as_view()),
    path("comments/<int:pk>", views.CommentDetail.as_view()),
]
