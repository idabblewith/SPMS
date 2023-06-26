import csv
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import model_to_dict
from django.http import HttpResponse
from agencies.serializers import (
    TinyBranchSerializer,
    TinyBusinessAreaSerializer,
    TinyAgencySerializer,
)

from users.serializers import TinyUserSerializer
from .models import User, UserWork, UserProfile


# CREATE AN EXPORT TO CSV FILE FOR CURRENT ENTRIES IN DB
@admin.action(description="Selected Users to CSV")
def export_selected_users_to_csv(model_admin, req, selected):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="users.csv"'

    field_names = selected[
        0
    ]._meta.fields  # Get the field names from the model's metadata
    writer = csv.DictWriter(response, fieldnames=[field.name for field in field_names])
    writer.writeheader()

    for user in selected:
        user_data = model_to_dict(user, fields=[field.name for field in field_names])
        writer.writerow(user_data)

    return response


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    actions = [
        export_selected_users_to_csv,
    ]
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "username",
                    "password",
                    "email",
                    "first_name",
                    "last_name",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Important Dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),
    )

    list_display = [
        "pk",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
    ]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    user = TinyUserSerializer
    # agency = TinyAgencySerializer

    list_display = [
        "user",
        "about",
        # "agency",
    ]

    # list_filter = ["agency"]

    search_fields = [
        "name",
    ]


@admin.register(UserWork)
class UserWorkAdmin(admin.ModelAdmin):
    user = TinyUserSerializer
    # agency = TinyAgencySerializer
    branch = TinyBranchSerializer
    business_area = TinyBusinessAreaSerializer

    list_display = [
        "user",
        "agency",
        "branch",
        "business_area",
    ]

    list_filter = [
        "agency",
        "branch",
        "business_area",
    ]

    search_fields = [
        "business_area__name",
        "user__name",
        "branch__name",
    ]

    # """Custom UserAdmin."""

    # list_display = ('username', 'fullname', 'email', 'program', 'work_center')
    # list_per_page = 1000    # sod pagination
    # list_filter = ('program', 'is_external', 'is_group', 'agreed',
    #                'is_staff', 'is_superuser', 'is_active')
    # readonly_fields = ('username', 'is_active', 'is_staff', 'is_superuser',
    #                    'user_permissions', 'last_login', 'date_joined')

    # form = PythiaUserChangeForm
    # add_form = PythiaUserCreationForm
    # formats = ['xls', 'json', 'yaml', 'csv', 'html', ]

    # fieldsets = (
    #     ('Name', {
    #         'description': 'Details required for correct display of name',
    #         'fields': ('title', 'first_name', 'middle_initials',
    #                    'last_name', 'group_name', 'affiliation',
    #                    'is_group', 'is_external'), }),
    #     ('Contact Details', {
    #         'description': 'Optional profile information',
    #         'classes': ('collapse',),
    #         'fields': ('image', 'email', 'phone', 'phone_alt', 'fax'), }),
    #     # ('Staff Profile', {
    #     #    'description':'Staff profile - not used for now',
    #     #    'classes': ('collapse',),
    #     #    'fields': ('program', 'work_center', 'profile_text',
    #     #        'expertise', 'curriculum_vitae', 'projects',
    #     #        'author_code', 'publications_staff', 'publications_other'),
    #     # }),
    #     ('Administrative Details', {
    #         'description': 'Behind the scenes settings',
    #         'classes': ('collapse',),
    #         'fields': ('program', 'work_center',
    #                    'username', 'password',
    #                    'is_active', 'is_staff', 'is_superuser',
    #                    'date_joined', 'groups'), })
    # )

    # # def division(self, obj):
    # #     """Return the User's Division."""
    # #     return obj.pythia_profile.division

    # # def program(self, obj):
    # #     """Return the User's program."""
    # #     return obj.pythia_profile.program

    # # def work_center(self, obj):
    # #     """Return the User's workcenter."""
    # #     return obj.pythia_profile.work_center

    # def get_breadcrumbs(self, request, obj=None, add=False):
    #     """Override the base breadcrumbs."""
    #     return (
    #         Breadcrumb(_('Home'), reverse('admin:index')),
    #         Breadcrumb(_('All users'), reverse('admin:pythia_user_changelist'))
    #     )

    # def get_readonly_fields(self, request, obj=None):
    #     """Determine which fields a User can edit, depending on role and group.

    #     Superusers can set permissions and details.
    #     Users can update their own details, but not permissions.
    #     Users can view other user's profiles read-only.

    #     Introduces hack property to prevent infinite recursion
    #      get_fieldsets may call .get_form, which calls .get_readonly_fields
    #     """
    #     if request.user.is_superuser:
    #         # superuser can edit all fields
    #         return ()
    #     elif obj and obj.pk:
    #         return ('is_superuser', 'is_active', 'is_staff', 'date_joined',
    #                 'groups', 'username')
    #     else:
    #         return ('is_superuser', 'is_active', 'is_staff', 'date_joined',
    #                 'groups')

    #     # this would work if pythia.models.User would inherit from ActiveModel
    #     # elif (request.user == obj.creator) and getattr(self, 'hack', True)):
    #     #    # the user is viewing another profile he created
    #     #    return super(UserAdmin, self).get_readonly_fields(request, obj)

    # def get_fieldsets(self, request, obj=None):
    #     """Custom get_fieldsets."""
    #     fs = super(UserAdmin, self).get_fieldsets(request, obj)
    #     return fs

    # def get_form(self, request, obj=None, **kwargs):
    #     """Custom get_form."""
    #     Form = super(UserAdmin, self).get_form(request, obj, **kwargs)

    #     class PythiaUserForm(Form):
    #         # shim to work around broken saving of form as normal user
    #         # (username should be RO to begin with, no harm done)

    #         def __init__(self, *args, **kwargs):
    #             super(PythiaUserForm, self).__init__(*args, **kwargs)
    #             self.fields['username'].required = False

    #         def clean_first_name(self):
    #             first_name = self.cleaned_data['first_name']
    #             # if not first_name:
    #             #    raise forms.ValidationError("First name cannot be blank.")
    #             return first_name

    #         def clean_last_name(self):
    #             last_name = self.cleaned_data['last_name']
    #             # if not last_name:
    #             #    raise forms.ValidationError("Last name cannot be blank.")
    #             return last_name

    #     return PythiaUserForm
