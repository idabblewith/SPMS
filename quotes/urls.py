from django.urls import path
from . import views

urlpatterns = [
    path("", views.Quotes.as_view()),
    path("create/", views.AddQuotesFromUniques.as_view()),
    path("random/", views.QuoteRandom.as_view()),
    path("reports/", views.QuoteReports.as_view()),
    path("<int:pk>", views.QuoteDetail.as_view()),
    path("<int:pk>/reports", views.QuoteReportDetail.as_view()),
]
