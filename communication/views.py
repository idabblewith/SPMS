from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render
from django.db import transaction
from django.conf import settings
from django.utils import timezone

import time

from .models import Comment
from .serializers import (
    CommentSerializer,
    TinyCommentSerializer,
)


class Comments(APIView):
    def get(self, req):
        all = Comment.objects.all()
        ser = CommentSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = CommentSerializer(data=req.data)
        if ser.is_valid():
            comment = ser.save()
            return Response(
                TinyCommentSerializer(comment).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class CommentDetail(APIView):
    def go(self, req, pk):
        try:
            obj = Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        comment = self.go(pk)
        ser = CommentSerializer(comment)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        comment = self.go(pk)
        comment.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        comment = self.go(pk)
        ser = CommentSerializer(
            comment,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated = ser.save()
            return Response(
                TinyCommentSerializer(updated).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )
