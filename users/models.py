from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    A custom user model for SDIS.

    Mostly intended to make profile modification simpler as the project grows.

    A user can have contact details, affiliations, research profiles and publications.
    """

    username = models.CharField(
        ("username"),
        unique=True,
        max_length=150,
        help_text=(
            "Required. 30 characters or fewer. Letters, digits and " "@/./+/-/_ only."
        ),
        # validators=[
        #     validators.RegexValidator(
        #         regex=r"^[\w.@+-]+\Z",
        #         message=(
        #             "Enter a valid username. \
        #             This value may contain only letters, numbers, and @/./+/-/_ characters."
        #         ),
        #     )
        # ],
    )

    # Administrative details -------------------------------------------------#
    is_staff = models.BooleanField(
        ("staff status"),
        default=True,
        help_text=("Designates whether the user can log into this admin " "site."),
    )

    is_active = models.BooleanField(
        ("active"),
        default=True,
        help_text=(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )

    is_external = models.BooleanField(
        default=False,
        verbose_name=("External to DBCA"),
        help_text=("Is the user external to DBCA?"),
    )

    agreed = models.BooleanField(
        default=False,
        editable=False,
        verbose_name=("Agreed to the Terms and Conditions"),
        help_text=("Has the user agreed to the Terms and Conditions?"),
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    # Name -------------------------------------------------------------------#
    title = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=("Academic Title"),
        help_text=(
            "Optional academic title, shown in team lists only if \
            supplied, and only for external team members."
        ),
    )

    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=("First Name"),
        help_text=("First name or given name."),
    )

    middle_initials = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=("Initials"),
        help_text=(
            "Initials of first and middle names. Will be used in \
            team lists with abbreviated names."
        ),
    )

    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=("Last Name"),
        help_text=("Last name or surname."),
    )

    is_group = models.BooleanField(
        default=False,
        verbose_name=("Show as Group"),
        help_text=(
            "Whether this profile refers to a group, rather than a \
            natural person. Groups are referred to with their group \
            name,  whereas first and last name refer to the group's \
            contact person."
        ),
    )

    group_name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=("Group Name"),
        help_text=(
            "Group name, if this profile is not a natural \
            person. E.g., 'Goldfields Regional Office'."
        ),
    )

    affiliation = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=("Affiliation"),
        help_text=(
            "Optional affiliation, not required for DBCA. \
            If provided, the affiliation will be appended to the \
            person or group name in parentheses."
        ),
    )

    # division = models.ForeignKey(
    #     Division,
    #     verbose_name=("Departmental Division"),
    #     blank=True, null=True,
    #     help_text=("The Departmental Division of this User. "
    #                 "Only applies to DBCA staff."))

    # # Contact details --------------------------------------------------------#
    # image = models.ImageField(
    #     upload_to="profiles",
    #     null=True,
    #     blank=True,
    #     help_text=("If you wish, provide us with a face to the name!"),
    # )

    # email = models.EmailField(("email address"), null=True, blank=True)

    # phone = models.CharField(
    #     max_length=100,
    #     null=True,
    #     blank=True,
    #     verbose_name=("Primary Phone Number"),
    #     help_text=("The primary phone number during work hours."),
    # )

    # phone_alt = models.CharField(
    #     max_length=100,
    #     null=True,
    #     blank=True,
    #     verbose_name=("Alternative Phone Number"),
    #     help_text=("An alternative phone number during work hours."),
    # )

    # fax = models.CharField(
    #     max_length=100,
    #     null=True,
    #     blank=True,
    #     verbose_name=("Fax Number"),
    #     help_text=("The fax number."),
    # )

    # # Academic profile -------------------------------------------------------#
    # profile_text = models.TextField(
    #     blank=True,
    #     null=True,
    #     help_text=(
    #         "A profile text for the staff members, roughly three paragraphs long."
    #     ),
    # )

    # expertise = models.TextField(
    #     blank=True,
    #     null=True,
    #     help_text=("A bullet point list of skills and expertise."),
    # )

    # curriculum_vitae = models.TextField(
    #     blank=True,
    #     null=True,
    #     help_text=(
    #         "A brief curriculum vitae of academic qualifications and \
    #         professional memberships."
    #     ),
    # )

    # projects = models.TextField(
    #     blank=True,
    #     null=True,
    #     verbose_name=("Projects outside SPMS"),
    #     help_text=("Tell us about your other projects outside SPMS."),
    # )

    # # Affiliation: spatial, organizational -----------------------------------#
    # program = models.ForeignKey(
    #     Program,
    #     blank=True,
    #     null=True,  # optional for migrations
    #     help_text=("The main Program affilitation."),
    # )

    # work_center = models.ForeignKey(
    #     WorkCenter,
    #     null=True,
    #     blank=True,
    #     help_text=("The work center where most time is spent. Staff only."),
    # )

    # # Publications -----------------------------------------------------------#
    # # Publications should be models in their own module really
    # author_code = models.CharField(
    #     max_length=255,
    #     null=True,
    #     blank=True,
    #     verbose_name=("Author code"),
    #     help_text=("The author code links users to their publications. Staff only."),
    # )

    # publications_staff = models.TextField(
    #     blank=True,
    #     null=True,
    #     verbose_name=("Staff publications"),
    #     help_text=(
    #         "A list of publications produced for the Department. Staff only."
    #     ),
    # )

    # publications_other = models.TextField(
    #     blank=True,
    #     null=True,
    #     verbose_name=("Other publications"),
    #     help_text=(
    #         "A list of publications produced under external \
    #         affiliation, in press or otherwise unregistered as \
    #         staff publication."
    #     ),
    # )

    # objects = UserManager()

    # DEFAULT_GROUP = "Users"
    # USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = []

    # class Meta:
    #     """Class opts."""

    #     verbose_name = "User"
    #     verbose_name_plural = "Users"

    # # def save(self, *args, **kwargs):
    # #     """Try to add the user to the default group on save."""
    # #     created = True if not self.pk else False

    # #     if not self.middle_initials:
    # #         try:
    # #             self.middle_initials = self.guess_first_initial()
    # #         except:
    # #             logger.warning(
    # #                 "Something went wrong trying to guess"
    # #                 " the initials from first name"
    # #             )

    # #     super(User, self).save(*args, **kwargs)

    # #     if created:
    # #         try:
    # #             group = Group.objects.get(name__iexact=self.DEFAULT_GROUP)
    # #         except Group.DoesNotExist:
    # #             logger.warning(
    # #                 "Failed to assign group `%s' to user `%s', "
    # #                 "group does not exist." % (self.DEFAULT_GROUP, self.email)
    # #             )
    # #         else:
    # #             self.groups.add(group)

    # # Helper functions -----------------------------------------------------------#

    # def get_title(self):
    #     """Return the title if supplied and user is_external.

    #     SANITY WARNING this function will HIDE the title for internal staff
    #     """
    #     return self.title if (self.title and self.is_external) else ""

    # def get_middle_initials(self):
    #     """Return middle initials or an empty string."""
    #     i = self.middle_initials if self.middle_initials else ""
    #     if len(i) > 1:
    #         return " {0}".format(i[1:])
    #     else:
    #         return ""

    # def guess_first_initial(self):
    #     """Return first element of first name or an empty string."""
    #     return self.first_name[0] if self.first_name else ""

    # def get_affiliation(self):
    #     """Return the affiliation in parentheses or an empty string."""
    #     a = "({0})".format(self.affiliation) if self.affiliation else ""
    #     return a

    # @property
    # def fullname(self):
    #     """Return a User's full name with title and affiliation."""
    #     return self.get_full_name()

    # def get_full_name(self):
    #     """
    #     Return title, first name, middle initials, last name, affiliation.

    #     Middle initials bring their own prefixed whitespace.
    #     """
    #     if self.is_group:
    #         full_name = "{0} {1}".format(self.group_name, self.get_affiliation())
    #     else:
    #         full_name = (
    #             "{0} {1} {2} {3} {4}".format(
    #                 self.get_title(),
    #                 self.first_name,
    #                 self.get_middle_initials(),
    #                 self.last_name,
    #                 self.get_affiliation(),
    #             )
    #             .strip()
    #             .replace("  ", " ")
    #         )
    #     return full_name

    # @property
    # def short_name(self):
    #     """Short name."""
    #     return self.first_name if self.first_name else self.fullname

    # def get_short_name(self):
    #     """Return the short name for the user."""
    #     return self.first_name

    # @property
    # def abbreviated_name(self):
    #     """String representation."""
    #     return self.get_abbreviated_name()

    # def get_abbreviated_name(self):
    #     """
    #     Abbreviated name.

    #     The first name is initialed.
    #     Middle initials are excluded.
    #     """
    #     if self.is_group:
    #         return self.get_full_name()
    #     else:
    #         full_name = f"{self.get_title()} {self.guess_first_initial()} {self.last_name} {self.get_affiliation()}"
    #     return full_name.replace("  ", " ").strip()

    # @property
    # def abbreviated_name_no_affiliation(self):
    #     """Abbreviated name."""
    #     return self.get_abbreviated_name_no_affiliation()

    # def get_abbreviated_name_no_affiliation(self):
    #     """Abbreviated name: title, initial of first name, last name."""
    #     if self.is_group:
    #         return self.get_full_name()
    #     else:
    #         full_name = f"{self.get_title()} {self.guess_first_initial()} {self.last_name}"
    #     return full_name.strip()

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this User."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

    # def __str_(self):
    #     """String representation."""
    #     slug = (
    #         f"({self.program.cost_center}-{self.program.slug})"
    #         if self.program
    #         else ""
    #     )
    #     return f"{self.get_full_name()}{slug}"

    # @property
    # def supervisor(self):
    #     """Return the Program Leader as User object, falls back to the User."""
    #     return self.program.program_leader if self.program else self

    # @property
    # def division(self):
    #     """The Division of the User's Program."""
    #     if self.program and self.program.division:
    #         return self.program.division
    #     else:
    #         return Division.objects.first()

    # @property
    # def registration_complete(self):
    #     """Return whether registration is complete.

    #     Return True if the user is registered, but not yet cleared to use the
    #     site.
    #     """
    #     if self.user.is_superuser:
    #         return False
    #     return self.is_external and not self.is_staff

    # @property
    # def tasklist(self):
    #     """Return documents which require input from the current user."""
    #     from pythia.projects.models import Project, ProjectMembership
    #     from pythia.documents.models import Document, ProjectPlan

    #     groups = [g.name for g in self.groups.all()]
    #     is_bm = "BM" in groups
    #     is_hc = "HC" in groups
    #     is_ae = "AE" in groups
    #     is_scd = "SCD" in groups

    #     excludes = set()
    #     # Project Plans pending endorsement/approval
    #     pplan_list = ProjectPlan.objects.filter(project__status=Project.STATUS_PENDING)
    #     for doc in pplan_list:
    #         if (
    #             (doc.bm_endorsement == Document.ENDORSEMENT_REQUIRED)
    #             or (doc.hc_endorsement == Document.ENDORSEMENT_REQUIRED)
    #             or (doc.ae_endorsement == Document.ENDORSEMENT_REQUIRED)
    #         ):
    #             excludes.add(doc)

    #     endorsements = set()
    #     needed = Document.ENDORSEMENT_REQUIRED

    #     if is_bm:
    #         logger.debug(type(pplan_list))
    #         endorsements.update(
    #             pplan_list.filter(bm_endorsement=needed).select_related("project")
    #         )

    #     if is_hc:
    #         endorsements.update(
    #             pplan_list.filter(hc_endorsement=needed).select_related("project")
    #         )

    #     if is_ae:
    #         endorsements.update(
    #             pplan_list.filter(ae_endorsement=needed).select_related("project")
    #         )

    #     approvals = set()

    #     # documents in review need PL attention
    #     program_list = self.leads_programs.all()
    #     # program -> projects is a reverse foreign key lookup,
    #     # we can't batch this, so do one query per program
    #     for prog in program_list:
    #         projects = prog.project_set.prefetch_related("documents")
    #         for proj in projects:
    #             approvals.update(
    #                 proj.documents.filter(
    #                     status=Document.STATUS_INREVIEW
    #                 ).select_related("project")
    #             )

    #     member_list = ProjectMembership.objects.prefetch_related(
    #         "project", "project__documents"
    #     ).filter(user=self)

    #     for member in member_list:
    #         approvals.update(
    #             member.project.documents.filter(
    #                 status=Document.STATUS_NEW
    #             ).select_related("project")
    #         )

    #     # documents in approval need SCD attention
    #     if is_scd:
    #         documents = Document.objects.filter(
    #             status=Document.STATUS_INAPPROVAL
    #         ).select_related("project")
    #         approvals.update(documents)

    #     #  deduplicate approvals pool with endorsements
    #     approvals.difference_update(excludes)

    #     # TODO: presort the output lists by descending project ID
    #     return {
    #         "approvals": list(approvals),
    #         "endorsements": list(endorsements),
    #         "count": len(approvals) + len(endorsements),
    #     }

    # @property
    # def portfolio(self):
    #     """
    #     Return projects supervised or participated in by current user.

    #     Required for index.html's My Tasks/Projects/Collaborations.
    #     If it's just for index.html (a template) consider making it a template
    #     tag!
    #     """
    #     from pythia.projects.models import (
    #         Project,
    #         ProjectMembership,
    #         # ScienceProject, CoreFunctionProject,
    #         # CollaborationProject, StudentProject
    #     )
    #     from pythia.documents.models import ConceptPlan, ProjectPlan
    #     from datetime import datetime, timedelta

    #     groups = [g.name for g in self.groups.all()]
    #     is_scd = "SCD" in groups

    #     # Fun fact: Django polymorphism casts the returned items from a
    #     # Project.objects query into the highest subclass, but does not
    #     # rig it for private key lookups. This is why we need to hit the
    #     # database again with pm_list to fetch the correctly casted object.

    #     best_before = datetime.now() - timedelta(days=60)
    #     pm_list = (
    #         ProjectMembership.objects.select_related("project")
    #         .order_by("-project__year", "-project__number")
    #         .filter(user=self, project__status__in=Project.ACTIVE)
    #     )
    #     projects = Project.objects.order_by("-year", "-number").filter(
    #         effective_to__isnull=True, project_owner=self
    #     )
    #     own_list = projects.filter(status__in=Project.ACTIVE)
    #     stuck_new = projects.filter(
    #         status__in=Project.STATUS_NEW, created__lt=best_before
    #     )
    #     stuck_pending = projects.filter(
    #         status__in=Project.STATUS_PENDING, created__lt=best_before
    #     )
    #     result = {"projects": {}, "collabs": {}, "stuck": {}}
    #     proj_result = {"super": [], "regular": []}
    #     collab_result = {"super": [], "regular": []}
    #     stuck_result = {"new": [], "pending": []}

    #     for x in stuck_new:
    #         # Projects stuck in approval for more than three months need a
    #         # kick up the rear end
    #         doc = x.documents.instance_of(ConceptPlan).get()
    #         stuck_result["new"].append(doc)

    #     for x in stuck_pending:
    #         doc = x.documents.instance_of(ProjectPlan).get()
    #         stuck_result["pending"].append(doc)

    #     for x in own_list:
    #         if x.type in (Project.SCIENCE_PROJECT, Project.CORE_PROJECT):
    #             proj_result["super"].append(x)
    #         elif x.type in (Project.COLLABORATION_PROJECT, Project.STUDENT_PROJECT):
    #             collab_result["super"].append(x)

    #     for x in pm_list:
    #         res = None
    #         proj = None

    #         try:
    #             if x.project.type == Project.SCIENCE_PROJECT:
    #                 res = proj_result
    #                 # proj = ScienceProject.objects.get(pk=x.project.pk)
    #                 proj = Project.objects.get(pk=x.project.pk)
    #             elif x.project.type == Project.CORE_PROJECT:
    #                 res = proj_result
    #                 # proj = CoreFunctionProject.objects.get(pk=x.project.pk)
    #                 proj = Project.objects.get(pk=x.project.pk)
    #             elif x.project.type == Project.COLLABORATION_PROJECT:
    #                 res = collab_result
    #                 # proj = CollaborationProject.objects.get(pk=x.project.pk)
    #                 proj = Project.objects.get(pk=x.project.pk)
    #             elif x.project.type == Project.STUDENT_PROJECT:
    #                 res = collab_result
    #                 # proj = StudentProject.objects.get(pk=x.project.pk)
    #                 proj = Project.objects.get(pk=x.project.pk)
    #             else:
    #                 continue

    #             if not (proj in res["super"]):
    #                 if x.role in [
    #                     ProjectMembership.ROLE_SUPERVISING_SCIENTIST,
    #                     ProjectMembership.ROLE_ACADEMIC_SUPERVISOR,
    #                 ]:
    #                     res["super"].append(proj)
    #                 else:
    #                     res["regular"].append(proj)

    #         except:
    #             logger.warning("Project lookup for User portfolio" " failed: " + str(x))

    #     if proj_result["super"] or proj_result["regular"]:
    #         result["projects"] = proj_result

    #     if collab_result["super"] or collab_result["regular"]:
    #         result["collabs"] = collab_result

    #     # Only SCD should worry about stuck projects
    #     if (stuck_result["new"] or stuck_result["pending"]) and is_scd:
    #         result["stuck"] = stuck_result

    #     # https://github.com/dbca-wa/sdis/issues/184
    #     if not self.show_docs:
    #         result["stuck"] = {"new": [], "pending": []}

    #     return result

    # @property
    # def show_docs(self):
    #     """Whether to show Documents to the User.

    #     Currently, documents are only shown to BCS members.
    #     In future, all users should see Documents, and this test should be retired.

    #     See https://github.com/dbca-wa/sdis/issues/184
    #     """
    #     return self.division and self.division.slug == "BCS"

    # @property
    # def is_admin(self):
    #     """Return True if the User is in Group "admins"."""
    #     return "admins" in [g.name for g in self.groups.all()]
