from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("@<str:username>", views.PublicUserDetail.as_view()),
    path("userworks", views.UserWorks.as_view()),
    path("userworks/<int:pk>", views.UserWorkDetail.as_view()),
    path("userprofiles", views.UserProfiles.as_view()),
    path("userprofiles/<int:pk>", views.UserProfileDetail.as_view()),
    # path("sso-login", views.SSOLogin.as_view()),
    # path("log-in", views.Login.as_view()),
    path("jwt-login", views.JWTLogin.as_view()),
    path("log-out", views.Logout.as_view()),
    path("change-password", views.ChangePassword.as_view()),
]
