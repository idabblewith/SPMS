from rest_framework.views import APIView
from math import ceil

from contacts.models import UserContact
from .models import User, UserProfile, UserWork
from rest_framework.exceptions import NotFound
from .serializers import (
    PrivateTinyUserSerializer,
    ProfilePageSerializer,
    TinyUserSerializer,
    UpdateMembershipSerializer,
    UpdatePISerializer,
    UpdateProfileSerializer,
    # TinyUserProfileSerializer,
    # TinyUserWorkSerializer,
    # UserProfileSerializer,
    # UserSerializer,
    # UserWorkSerializer,
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
from django.db.models import Q
from django.db import transaction
from django.utils.text import capfirst


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


class CheckEmailExists(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        email = request.data.get("email")
        if not email:
            raise ParseError("Email not provided")

        user_exists = User.objects.filter(email=email).exists()
        return Response(
            {"exists": user_exists},
            status=HTTP_200_OK,
        )


class CheckNameExists(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        if not first_name or not last_name:
            raise ParseError("First name or last name not provided")

        # Capitalize the first letter of first_name and last_name
        capitalized_first_name = capfirst(first_name)
        capitalized_last_name = capfirst(last_name)

        user_exists = User.objects.filter(
            first_name__iexact=capitalized_first_name,
            last_name__iexact=capitalized_last_name,
        ).exists()
        return Response(
            {"exists": user_exists},
            status=HTTP_200_OK,
        )


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, req):
        user = req.user
        ser = ProfilePageSerializer(user)
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


class Users(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            # If the user sends a non-integer value as the page parameter
            page = 1

        page_size = settings.PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        search_term = request.GET.get("searchTerm")

        # Get the values of the checkboxes
        only_superuser = bool(request.GET.get("only_superuser", False))
        only_staff = bool(request.GET.get("only_staff", False))
        only_external = bool(request.GET.get("only_external", False))

        # Interaction logic between checkboxes
        if only_external:
            only_staff = False
            only_superuser = False
        elif only_staff or only_superuser:
            only_external = False

        if search_term:
            # Apply filtering based on the search term
            users = User.objects.filter(
                Q(first_name__icontains=search_term)
                | Q(last_name__icontains=search_term)
                | Q(email__icontains=search_term)
                | Q(username__icontains=search_term)
            )
        else:
            users = User.objects.all()

        # Filter users based on checkbox values
        if only_external:
            users = users.filter(is_staff=False)
        elif only_staff:
            users = users.filter(is_staff=True)
        elif only_superuser:
            users = users.filter(is_superuser=True)

        # Sort users alphabetically based on email
        users = users.order_by("email")

        total_users = users.count()
        total_pages = ceil(total_users / page_size)

        serialized_users = TinyUserSerializer(
            users[start:end], many=True, context={"request": request}
        ).data

        response_data = {"users": serialized_users, "total_pages": total_pages}

        return Response(response_data, status=HTTP_200_OK)

    def post(self, req):
        print(req.data)
        ser = PrivateTinyUserSerializer(
            data=req.data,
        )
        if ser.is_valid():
            # print("Serializer legit")
            try:
                # Ensures everything is rolled back if there is an error.
                with transaction.atomic():
                    new_user = ser.save(
                        first_name=req.data.get("firstName"),
                        last_name=req.data.get("lastName"),
                    )

                    # Creates UserWork entry
                    UserWork.objects.create(user=new_user)
                    # Creates UserProfile entry
                    UserProfile.objects.create(user=new_user)
                    # Creates UserContact entry
                    UserContact.objects.create(user=new_user)

                    new_user.set_password(settings.EXTERNAL_PASS)
                    new_user.save()
                    print(new_user)
                    ser = TinyUserSerializer(new_user)
                    return Response(
                        ser.data,
                        status=HTTP_201_CREATED,
                    )
            except Exception as e:
                # print("exxxxxxxxx")
                print(e)
                raise ParseError(e)
        else:
            return Response(
                ser.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class UserProfileView(APIView):
    def go(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, req, pk):
        user = self.go(pk)
        ser = ProfilePageSerializer(user)
        return Response(
            ser.data,
            status=HTTP_202_ACCEPTED,
        )


class UpdatePersonalInformation(APIView):
    def go(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, req, pk):
        user = self.go(pk)
        ser = UpdatePISerializer(user)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def put(self, req, pk):
        title = req.data.get("title")
        phone = req.data.get("phone")
        fax = req.data.get("fax")

        updated_data = {
            "title": title,
            "phone": phone,
            "fax": fax,
        }

        # Remove empty variables from updated_data
        updated_data = {
            key: value
            for key, value in updated_data.items()
            if value is not None and value != ""
        }

        user = self.go(pk)
        ser = UpdatePISerializer(user)
        return Response(
            ser.data,
            status=HTTP_202_ACCEPTED,
        )


class UpdateProfile(APIView):
    def go(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, req, pk):
        user = self.go(pk)
        ser = UpdateProfileSerializer(user)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def put(self, req, pk):
        user = self.go(pk)
        ser = UpdateProfileSerializer(user)
        return Response(
            ser.data,
            status=HTTP_202_ACCEPTED,
        )


class UpdateMembership(APIView):
    def go(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, req, pk):
        user = self.go(pk)
        ser = UpdateMembershipSerializer(user)
        return Response(
            ser.data,
            status=HTTP_200_OK,
        )

    def put(self, req, pk):
        user = self.go(pk)
        ser = UpdateMembershipSerializer(user)
        return Response(
            ser.data,
            status=HTTP_202_ACCEPTED,
        )


# class UserProfile(APIView):
#     def go(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise NotFound

#     def get(self, req, pk):
#         user = self.go(pk)
#         ser = ProfilePageSerializer(user)
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )
# class UserProfile(APIView):
#     def go(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise NotFound

#     def get(self, req, pk):
#         user = self.go(pk)
#         ser = ProfilePageSerializer(user)
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )


# class UserWorks(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get(self, req):
#         all = UserWork.objects.all()
#         ser = TinyUserWorkSerializer(
#             all,
#             many=True,
#         )
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )

#     def post(self, req):
#         ser = UserWorkSerializer(
#             data=req.data,
#         )
#         if ser.is_valid():
#             uw = ser.save()
#             return Response(
#                 TinyUserWorkSerializer(uw).data,
#                 status=HTTP_201_CREATED,
#             )
#         else:
#             return Response(
#                 HTTP_400_BAD_REQUEST,
#             )


# class UserProfiles(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get(self, req):
#         all = UserProfile.objects.all()
#         ser = TinyUserProfileSerializer(
#             all,
#             many=True,
#         )
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )

#     def post(self, req):
#         ser = UserProfileSerializer(
#             data=req.data,
#         )
#         if ser.is_valid():
#             up = ser.save()
#             return Response(
#                 TinyUserProfileSerializer(up).data,
#                 status=HTTP_201_CREATED,
#             )
#         else:
#             return Response(
#                 HTTP_400_BAD_REQUEST,
#             )


# class UserWorkDetail(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def go(self, pk):
#         try:
#             obj = UserWork.objects.get(pk=pk)
#         except UserWork.DoesNotExist:
#             raise NotFound
#         return obj

#     def get(self, req, pk):
#         uw = self.go(pk)
#         ser = UserWorkSerializer(uw)
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )

#     def delete(self, req, pk):
#         uw = self.go(pk)
#         uw.delete()
#         return Response(
#             status=HTTP_204_NO_CONTENT,
#         )

#     def put(self, req, pk):
#         uw = self.go(pk)
#         ser = UserWorkSerializer(
#             uw,
#             data=req.data,
#             partial=True,
#         )
#         if ser.is_valid():
#             updated_uw = ser.save()
#             return Response(
#                 TinyUserWorkSerializer(updated_uw).data,
#                 status=HTTP_202_ACCEPTED,
#             )
#         else:
#             return Response(
#                 ser.errors,
#                 status=HTTP_400_BAD_REQUEST,
#             )


# class UserProfileDetail(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def go(self, pk):
#         try:
#             obj = UserProfile.objects.get(pk=pk)
#         except UserProfile.DoesNotExist:
#             raise NotFound
#         return obj

#     def get(self, req, pk):
#         up = self.go(pk)
#         ser = UserProfileSerializer(up)
#         return Response(
#             ser.data,
#             status=HTTP_200_OK,
#         )

#     def delete(self, req, pk):
#         up = self.go(pk)
#         up.delete()
#         return Response(
#             status=HTTP_204_NO_CONTENT,
#         )

#     def put(self, req, pk):
#         up = self.go(pk)
#         ser = UserProfileSerializer(
#             up,
#             data=req.data,
#             partial=True,
#         )
#         if ser.is_valid():
#             updated_up = ser.save()
#             return Response(
#                 TinyUserProfileSerializer(updated_up).data,
#                 status=HTTP_202_ACCEPTED,
#             )
#         else:
#             return Response(
#                 ser.errors,
#                 status=HTTP_400_BAD_REQUEST,
#             )
