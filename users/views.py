from rest_framework.views import APIView
from .models import User, UserProfile, UserWork
from rest_framework.exceptions import NotFound
from .serializers import (
    TinyUserProfileSerializer,
    TinyUserSerializer,
    TinyUserWorkSerializer,
    UserProfileSerializer,
    UserSerializer,
    UserWorkSerializer,
)
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_202_ACCEPTED,
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ParseError
from django.contrib.auth import authenticate, login, logout
import jwt
from django.conf import settings


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        user = req.user
        ser = TinyUserSerializer(user)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def put(self, req):
        user = req.user
        ser = TinyUserSerializer(
            user,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated = ser.save()
            return Response(
                TinyUserSerializer(updated).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class JWTLogin(APIView):
    def post(self, req):
        username = req.data.get("username")
        password = req.data.get("password")
        if not username or not password:
            raise ParseError("Username and Password must both be provided!")
        user = authenticate(username=username, password=password)
        if user:
            token = jwt.encode(
                {"pk": user.pk},
                settings.SECRET_KEY,
                algorithm="HS256",
            )
            return Response({"token": token})
        else:
            return Response({"error": "Incorrect Password"})


class SSOLogin(APIView):
    pass


class Login(APIView):
    def post(self, req):
        # print(req.data)
        username = req.data.get("username")
        password = req.data.get("password")
        if not username or not password:
            # print("No username and password")
            raise ParseError("Username and Password must both be provided!")
        user = authenticate(username=username, password=password)
        if user:
            # print("User legit")
            login(req, user)
            # print("Login Performed")
            return Response({"ok": "Welcome"})
        else:
            print("Password Error")
            return Response({"error": "Incorrect Password"})


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, req):
        logout(req)
        return Response({"ok": "Bye"})


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, req):
        user = req.user
        old_password = req.data.get("old_password")
        new_password = req.data.get("new_password")
        if not old_password or not new_password:
            raise ParseError("Passwords not provieded")
        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return Response(status=HTTP_200_OK)
        else:
            raise ParseError("Passwords not provieded")


class Users(APIView):
    def get(self, req):
        users = User.objects.all()
        ser = TinyUserSerializer(
            users,
            many=True,
            context={"request": req},
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        password = req.data.get("password")
        if not password:
            raise ParseError("No password provided!")
        ser = TinyUserSerializer(
            data=req.data,
        )
        if ser.is_valid():
            new_user = ser.save()
            new_user.set_password(password)
            new_user.save()
            return Response(
                TinyUserSerializer(new_user).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class PublicUserDetail(APIView):
    def go(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound

    def get(self, req, username):
        user = self.go(username)
        ser = UserSerializer(user)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, username):
        user = self.go(username)
        user.delete
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, username):
        user = self.go(username)
        ser = FullUserSerializer(
            user,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated = ser.save()
            return Response(
                FullUserSerializer(updated).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                status=HTTP_400_BAD_REQUEST,
            )


class UserWorks(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, req):
        all = UserWork.objects.all()
        ser = TinyUserWorkSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = UserWorkSerializer(
            data=req.data,
        )
        if ser.is_valid():
            uw = ser.save()
            return Response(
                TinyUserWorkSerializer(uw).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                HTTP_400_BAD_REQUEST,
            )


class UserProfiles(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, req):
        all = UserProfile.objects.all()
        ser = TinyUserProfileSerializer(
            all,
            many=True,
        )
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def post(self, req):
        ser = UserProfileSerializer(
            data=req.data,
        )
        if ser.is_valid():
            up = ser.save()
            return Response(
                TinyUserProfileSerializer(up).data,
                status=HTTP_201_CREATED,
            )
        else:
            return Response(
                HTTP_400_BAD_REQUEST,
            )


class UserWorkDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def go(self, pk):
        try:
            obj = UserWork.objects.get(pk=pk)
        except UserWork.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        uw = self.go(pk)
        ser = UserWorkSerializer(uw)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        uw = self.go(pk)
        uw.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        uw = self.go(pk)
        ser = UserWorkSerializer(
            uw,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated_uw = ser.save()
            return Response(
                TinyUserWorkSerializer(updated_uw).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class UserProfileDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def go(self, pk):
        try:
            obj = UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            raise NotFound
        return obj

    def get(self, req, pk):
        up = self.go(pk)
        ser = UserProfileSerializer(up)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def delete(self, req, pk):
        up = self.go(pk)
        up.delete()
        return Response(
            status=HTTP_204_NO_CONTENT,
        )

    def put(self, req, pk):
        up = self.go(pk)
        ser = UserProfileSerializer(
            up,
            data=req.data,
            partial=True,
        )
        if ser.is_valid():
            updated_up = ser.save()
            return Response(
                TinyUserProfileSerializer(updated_up).data,
                status=HTTP_202_ACCEPTED,
            )
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )
