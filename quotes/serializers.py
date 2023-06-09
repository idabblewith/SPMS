from rest_framework.serializers import ModelSerializer, SerializerMethodField

from users.serializers import TinyUserSerializer
from .models import Quote, QuoteReport
from rest_framework.exceptions import NotFound


class QuoteListSerializer(ModelSerializer):
    reports_count = SerializerMethodField()

    def get_reports_count(self, quote):
        return quote.reports.count()

    class Meta:
        model = Quote
        fields = [
            "pk",
            "text",
            "author",
            "created_at",
            "reports_count",
        ]


class QuoteReportSerializer(ModelSerializer):
    quote = QuoteListSerializer()
    reporter = TinyUserSerializer(read_only=True)
    viewing_user_reported = SerializerMethodField()

    def get_viewing_user_reported(self, quotereport):
        req = self.context["request"]
        user = req.user
        if user.pk == quotereport.reporter.pk:
            return True
        else:
            return False

    class Meta:
        model = QuoteReport
        fields = [
            "pk",
            "quote",
            "reporter",
            "reason",
            "viewing_user_reported",
        ]


class TinyQuoteReportSerializer(ModelSerializer):
    quote = QuoteListSerializer()
    reporter = TinyUserSerializer(read_only=True)

    class Meta:
        model = QuoteReport
        fields = [
            "pk",
            "quote",
            "reporter",
            "reason",
        ]


class QuoteDetailSerializer(ModelSerializer):
    reports_count = SerializerMethodField()
    viewing_user_reported = SerializerMethodField()

    def get_reports_count(self, quote):
        return quote.reports.count()

    def get_viewing_user_reported(self, quote):
        req = self.context["request"]
        user = req.user
        answer = QuoteReport.objects.filter(quote=quote, reporter=user)
        if answer:
            return True
        else:
            return False
        # return request.user

    reports = TinyQuoteReportSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Quote
        fields = [
            "pk",
            "text",
            "author",
            "created_at",
            "reports_count",
            "viewing_user_reported",
            "reports",
        ]
