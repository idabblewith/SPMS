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

from .models import (
    ProjectDocumentComment,
    DirectMessage,
    ChatRoom,
    CommentReaction,
    DirectMessageReaction,
)
from .serializers import (
    ChatRoomSerializer,
    DirectMessageReactionSerializer,
    CommentReactionSerializer,
    CommentSerializer,
    DirectMessageSerializer,
    TinyChatRoomSerializer,
    TinyCommentReactionSerializer,
    TinyCommentSerializer,
    TinyDirectMessageReactionSerializer,
    TinyDirectMessageSerializer,
)


class ChatRooms(APIView):
    def get(self, req):
        all = ChatRoom.objects.all()
        ser = TinyChatRoomSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = ChatRoomSerializer(data=req.data)
        if ser.is_valid():
            cr = ser.save()
            return Response(
                TinyChatRoomSerializer(cr).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class DirectMessages(APIView):
    def get(self, req):
        all = DirectMessage.objects.all()
        ser = TinyDirectMessageSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = DirectMessageSerializer(data=req.data)
        if ser.is_valid():
            dm = ser.save()
            return Response(
                TinyDirectMessageSerializer(dm).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class Comments(APIView):
    def get(self, req):
        all = ProjectDocumentComment.objects.all()
        ser = TinyCommentSerializer(
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


class CommentReactions(APIView):
    def get(self, req):
        all = CommentReaction.objects.all()
        ser = TinyCommentReactionSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = CommentReactionSerializer(data=req.data)
        if ser.is_valid():
            comment_reaction = ser.save()
            return Response(
                TinyCommentSerializer(comment_reaction).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class DirectMessageReactions(APIView):
    def get(self, req):
        all = DirectMessageReaction.objects.all()
        ser = TinyDirectMessageReactionSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = DirectMessageReactionSerializer(data=req.data)
        if ser.is_valid():
            dm_reaction = ser.save()
            return Response(
                TinyDirectMessageSerializer(dm_reaction).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


# Details


class ChatRoomDetail(APIView):
    def go(self, req, pk):
        try:
            obj = ChatRoom.objects.get(pk=pk)
        except ChatRoom.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        cr = self.go(pk)
        ser = ChatRoomSerializer(cr)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        cr = self.go(pk)
        cr.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        cr = self.go(pk)
        ser = ChatRoomSerializer(
            cr,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated = ser.save()
            return Response(
                TinyChatRoomSerializer(updated).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class DirectMessageDetail(APIView):
    def go(self, req, pk):
        try:
            obj = DirectMessage.objects.get(pk=pk)
        except DirectMessage.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        dm = self.go(pk)
        ser = DirectMessageSerializer(dm)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        dm = self.go(pk)
        dm.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        dm = self.go(pk)
        ser = DirectMessageSerializer(
            dm,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated = ser.save()
            return Response(
                TinyDirectMessageSerializer(updated).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class CommentDetail(APIView):
    def go(self, req, pk):
        try:
            obj = ProjectDocumentComment.objects.get(pk=pk)
        except ProjectDocumentComment.DoesNotExist:
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


class DirectMessageReactionDetail(APIView):
    def go(self, req, pk):
        try:
            obj = DirectMessageReaction.objects.get(pk=pk)
        except DirectMessageReaction.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        dmr = self.go(pk)
        ser = DirectMessageReactionSerializer(dmr)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        dmr = self.go(pk)
        dmr.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        dmr = self.go(pk)
        ser = DirectMessageReactionSerializer(
            dmr,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated = ser.save()
            return Response(
                TinyDirectMessageReactionSerializer(updated).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class CommentReactionDetail(APIView):
    def go(self, req, pk):
        try:
            obj = CommentReaction.objects.get(pk=pk)
        except CommentReaction.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        dmr = self.go(pk)
        ser = CommentReactionSerializer(dmr)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        dmr = self.go(pk)
        dmr.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        dmr = self.go(pk)
        ser = CommentReactionSerializer(
            dmr,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated = ser.save()
            return Response(
                TinyCommentReactionSerializer(updated).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )
