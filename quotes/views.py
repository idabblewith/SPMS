import os
import random
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from django.db import transaction
from .models import Quote, QuoteReport
from .serializers import (
    QuoteListSerializer,
    QuoteDetailSerializer,
    QuoteReportSerializer,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AddQuotesFromUniques(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, req):
        print(req.data)

        def clean_quotes():
            print(os.path.dirname(os.path.realpath(__file__)))
            with open(
                os.path.dirname(os.path.realpath(__file__)) + "/unique_quotes.txt"
            ) as quotesfile:
                processed_1 = []
                duplicates = []
                unique_quotes = []
                array_of_raw_quotes = quotesfile.readlines()
                for line in array_of_raw_quotes:
                    line.strip()
                    line.lower()
                    if line not in processed_1:
                        processed_1.append(line)
                    else:
                        duplicates.append(line)
                for p1 in processed_1:
                    line_array = p1.split(" - ")
                    check = len(line_array)
                    if check <= 2:
                        quote = line_array[0]
                        author = line_array[1]
                    else:
                        quote_array = line_array[:-1]
                        quote = " - ".join(item for item in quote_array)
                        quote.strip()
                        author = line_array[-1]
                    unique_quotes.append({"text": quote, "author": author})

                print(f"\n\n\nFormatting: {unique_quotes[0]}\n")
                print(f"Uniques: {len(unique_quotes)}/{len(array_of_raw_quotes)}\n")
                print(f"Duplicates: {duplicates}\n")
                return unique_quotes

        uniques = clean_quotes()
        try:
            for obj in uniques:
                ser = QuoteListSerializer(data=obj)
                if ser.is_valid():
                    # with transaction.atomic():
                    ser.save()
                else:
                    print(f"ERROR: {ser.errors}")
            print("SUCCESS: GENERATED")
        except Exception as e:
            print(f"ERROR: {e}")
        return Response(
            status=HTTP_201_CREATED,
        )


class Quotes(APIView):
    def get(self, req):
        try:
            page = int(req.query_params.get("page", 1))
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size
        all = Quote.objects.all()
        ser = QuoteListSerializer(all[start:end], many=True)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        if not req.user.is_authenticated:
            raise NotAuthenticated
        ser = QuoteListSerializer(data=req.data)
        if ser.is_valid():
            a = ser.save()
            return Response(
                QuoteListSerializer(a).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class QuoteRandom(APIView):
    def go(self, pk):
        try:
            return Quote.objects.get(pk=pk)
        except Quote.DoesNotExist:
            raise NotFound

    def get(self, req):
        count = Quote.objects.count()
        quote = self.go(pk=random.randint(0, count))
        ser = QuoteDetailSerializer(quote, context={"request": req})
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )


class QuoteDetail(APIView):
    def go(self, pk):
        try:
            return Quote.objects.get(pk=pk)
        except Quote.DoesNotExist:
            raise NotFound

    def get(self, req, pk):
        quote = self.go(pk)
        ser = QuoteDetailSerializer(quote, context={"request": req})
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        if not req.user.is_authenticated:
            raise NotAuthenticated
        a = self.go(pk)
        a.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        if not req.user.is_authenticated:
            raise NotAuthenticated
        a = self.go(pk)
        ser = QuoteDetailSerializer(
            a,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated = ser.save()
            return Response(
                QuoteDetailSerializer(updated).data,
                status=HTTP_202_ACCEPTED,
            )


class QuoteReports(APIView):
    def get(self, req):
        try:
            page = int(req.query_params.get("page", 1))
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size
        all = QuoteReport.objects.all()
        ser = QuoteReportSerializer(all[start:end], many=True)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        if not req.user.is_authenticated:
            raise NotAuthenticated
        ser = QuoteReportSerializer(data=req.data)
        if ser.is_valid():
            # Remove Report if already reported
            count = QuoteReport.objects.filter(
                quote=req.data["quote"], reporter=req.user
            ).count()
            if count >= 1:
                QuoteReport.objects.filter(
                    quote=req.data["quote"], reporter=req.user
                ).delete()
                return Response(
                    status=HTTP_204_NO_CONTENT,
                )
            else:
                # Ordinary report
                a = ser.save()
                return Response(
                    QuoteReportSerializer(a).data,
                    status=HTTP_201_CREATED,
                )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class QuoteReportDetail(APIView):
    def go(self, pk):
        try:
            return QuoteReport.objects.get(pk=pk)
        except QuoteReport.DoesNotExist:
            raise NotFound

    def get(self, req, pk):
        quote = self.go(pk)
        ser = QuoteReportSerializer(quote, context={"request": req})
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        if not req.user.is_authenticated:
            raise NotAuthenticated
        a = self.go(pk)
        a.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        if not req.user.is_authenticated:
            raise NotAuthenticated
        a = self.go(pk)
        ser = QuoteListSerializer(
            a,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated = ser.save()
            return Response(
                QuoteReportSerializer(updated).data,
                status=HTTP_202_ACCEPTED,
            )
