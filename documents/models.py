from django.db import models

# Create your models here.

# Abstract Document Model
#    """
#     An abstract base class for documents.
#     This base class provides completion totals through the ContextStatusMixin.
#     """

#     STATUS_NEW = 'new'
#     STATUS_INREVIEW = 'inreview'
#     STATUS_INAPPROVAL = 'inapproval'
#     STATUS_APPROVED = 'approved'

#     STATUS_CHOICES = (
#         (STATUS_NEW, _("New document")),
#         (STATUS_INREVIEW, _("Review requested")),
#         (STATUS_INAPPROVAL, _("Approval requested")),
#         (STATUS_APPROVED, _("Approved"))
#     )

#     STATUS_LABELS = {
#         STATUS_NEW: "danger",
#         STATUS_INREVIEW: "warning",
#         STATUS_INAPPROVAL: "info",
#         STATUS_APPROVED: "success"
#     }

#     ENDORSEMENT_NOTREQUIRED = 'not required'
#     ENDORSEMENT_REQUIRED = 'required'
#     ENDORSEMENT_DENIED = 'denied'
#     ENDORSEMENT_GRANTED = 'granted'

#     ENDORSEMENT_CHOICES = (
#         (ENDORSEMENT_REQUIRED, _('required')),
#         (ENDORSEMENT_DENIED, _('denied')),
#         (ENDORSEMENT_GRANTED, _('granted'))
#     )

#     ENDORSEMENT_NULL_CHOICES = (
#         (ENDORSEMENT_NOTREQUIRED, _('not required')),
#         (ENDORSEMENT_REQUIRED, _('required')),
#         (ENDORSEMENT_DENIED, _('denied')),
#         (ENDORSEMENT_GRANTED, _('granted'))
#     )

#     template = None
#     template_tex = None

#     project = models.ForeignKey('projects.Project', related_name='documents')

#     status = FSMField(
#         default=STATUS_NEW, choices=STATUS_CHOICES,
#         verbose_name=_("Document Status"))
#     pdf = models.FileField(
#         upload_to=documents_upload_to, blank=True, null=True,
#         editable=False,
#         help_text="The latest, greatest and PDFest version of all times")

#     objects = DocumentManager()

# Concept Plan
# template = "admin/pythia/ararreport/includes/conceptplan.html"
# template_tex = "latex/includes/conceptplan.tex"

# # summary = PythiaTextField(
# background = models.TextField(
#     verbose_name=_("Background"), blank=True, null=True,
#     help_text=_("Provide background in up to 500 words."))
# summary = models.TextField(
#     verbose_name=_("Aims"), blank=True, null=True,
#     help_text=_("List the aims in up to 500 words."))
# outcome = models.TextField(
#     verbose_name=_("Expected outcome"), blank=True, null=True,
#     help_text=_("Summarise expected outcome in up to 500 words."))
# collaborations = models.TextField(
#     verbose_name=_("Expected collaborations"), blank=True, null=True,
#     help_text=_("List expected collaborations in up to 500 words."))
# strategic = models.TextField(
#     verbose_name=_("Strategic context"), blank=True, null=True,
#     help_text=_("Describe strategic context and management "
#                 "implications in up to 500 words."))
# staff = PythiaArrayField(
#     verbose_name=_("Staff time allocation"), blank=True, null=True,
#     help_text=_("Summarise staff time allocation by role for the "
#                 "first three years, or for a time span appropriate for "
#                 "the Project's life time."),
#     # default = '<table style="width:400px;" border="1" cellpadding="2">'
#     #           '<tbody><tr><td>Role</td><td>Year 1</td><td>Year 2</td>'
#     #           '<td>Year 3</td></tr><tr><td>Scientist</td><td></td>'
#     #           '<td></td><td></td></tr><tr><td>Technical</td><td>'
#     #           '</td><td></td><td></td></tr><tr><td>Volunteer</td>'
#     #           '<td></td><td></td><td></td></tr><tr><td>Collaborator</td>'
#     #           '<td></td><td></td><td></td></tr></tbody></table>'
#     default=json.dumps([
#         ['Role', 'Year 1', 'Year 2', 'Year 3'],
#         ['Scientist', '', '', ''],
#         ['Technical', '', '', ''],
#         ['Volunteer', '', '', ''],
#         ['Collaborator', '', '', ''],
#     ], cls=DjangoJSONEncoder)
# )
# budget = PythiaArrayField(
#     verbose_name=_("Indicative operating budget"),
#     blank=True, null=True,
#     help_text=_("Indicate the operating budget for the first three years, "
#                 "or for a time span appropriate for the Project's life "
#                 "time."),
#     default=json.dumps([
#         ['Source', 'Year 1', 'Year 2', 'Year 3'],
#         ['Consolidated Funds (DBCA)', '', '', ''],
#         ['External Funding', '', '', ''],
#     ], cls=DjangoJSONEncoder)
# )
# # Currently not desired:
# director_scd_comment = models.TextField(
#     editable=False,  # remove to unhide
#     verbose_name=_("Director's Comment"),
#     help_text=_("Optional comment to clarify endorsement or provide "
#                 "feedback"), blank=True, null=True)
# director_outputprogram_comment = models.TextField(
#     editable=False,  # remove to unhide
#     verbose_name=_("Comment of the Output Program's Director"),
#     help_text=_("Optional comment to clarify endorsement or provide "
#                 "feedback"), blank=True, null=True)


# Project Plan
# template = "admin/pythia/ararreport/includes/projectplan.html"
# template_tex = "latex/includes/projectplan.tex"

# related_projects = models.TextField(
#     verbose_name=_("Related Science Projects"),
#     blank=True, null=True,
#     editable=True,
#     help_text=_("Name related SPPs and the extent you have consulted with "
#                 "their project leaders (SPP A6)."))

# # Part C: Relevance and outcomes #
# background = models.TextField(
#     verbose_name=_("Background"),
#     blank=True, null=True,
#     help_text=_("Describe project background (SPP C16) including a "
#                 "literature review."))
# aims = models.TextField(
#     verbose_name=_("Aims"),
#     blank=True, null=True,
#     help_text=_("List project aims (SPP C17)."))
# outcome = models.TextField(
#     verbose_name=_("Expected outcome"),
#     blank=True, null=True,
#     help_text=_("Describe expected project outcome."))
# knowledge_transfer = models.TextField(
#     verbose_name=_("Knowledge transfer"),
#     blank=True, null=True,
#     help_text=_("Anticipated users of the knowledge to be gained, and "
#                 "technology transfer strategy (SPP C19)."))
# project_tasks = models.TextField(
#     verbose_name=_("Tasks and Milestones"),
#     blank=True, null=True,
#     help_text=_("Major tasks, milestones and outputs (SPP C20). "
#                 "Indicate delivery time frame for each task."))
# references = models.TextField(
#     verbose_name=_("References"),
#     blank=True, null=True,
#     help_text=_("Paste in the bibliography of your literature research "
#                 "(SPP C21)."))

# # Part D: Study design #
# methodology = models.TextField(
#     verbose_name=_("Methodology"),
#     blank=True, null=True,
#     help_text=_("Describe the study design and statistical analysis"
#                 " (SPP D22)."))
# bm_endorsement = models.CharField(
#     verbose_name=_("Biometrician's Endorsement"),
#     blank=True, null=True,
#     max_length=100,
#     default=Document.ENDORSEMENT_REQUIRED,
#     choices=Document.ENDORSEMENT_CHOICES,
#     help_text=_("The Biometrician's endorsement of the methodology's "
#                 "statistical validity."))

# # Part E: data management and budget #
# involves_plants = models.BooleanField(
#     verbose_name=_("Involves plant specimen collection"),
#     blank=False, null=False,
#     default=False,
#     help_text=_("Tick to indicate that this project will collect plant "
#                 "specimens, which will require endorsement by the "
#                 "Herbarium Curator."))
# no_specimens = models.TextField(
#     verbose_name=_("No. specimens"),
#     blank=True, null=True,
#     help_text=_("Estimate the number of collected vouchered specimens "
#                 "(SPP E23). Provide any additional info required for "
#                 "the Harbarium Curator's endorsement."))
# hc_endorsement = models.CharField(
#     verbose_name=_("Herbarium Curator's Endorsement"),
#     blank=True, null=True,
#     max_length=100,
#     default=Document.ENDORSEMENT_NOTREQUIRED,
#     choices=Document.ENDORSEMENT_NULL_CHOICES,
#     help_text=_("The Herbarium Curator's endorsement of the planned "
#                 "collection of voucher specimens."))

# # New one! Animal Ethics Committee approval
# involves_animals = models.BooleanField(
#     verbose_name=_("Involves interaction with vertebrate animals"),
#     blank=False, null=False,
#     default=False,
#     help_text=_("Tick to indicate that this project will involve "
#                 "direct interaction with animals, which will require "
#                 "endorsement by the Animal Ethics Committee."))
# ae_endorsement = models.CharField(
#     verbose_name=_("Animal Ethics Committee's Endorsement"),
#     blank=True, null=True,
#     max_length=100,
#     default=Document.ENDORSEMENT_NOTREQUIRED,
#     choices=Document.ENDORSEMENT_NULL_CHOICES,
#     help_text=_("The Animal Ethics Committee's endorsement of the"
#                 " planned direct interaction with animals. "
#                 "Approval process is currently handled outside "
#                 "of SPMS."))

# data_management = models.TextField(
#     verbose_name=_("Data management"), blank=True, null=True,
#     help_text=_("Describe how and where data will be maintained, archived,"
#                 " cataloged (SPP E24). Read DBCA guideline 16."))
# # Data manager's endorsement!!!
# data_manager_endorsement = models.CharField(
#     editable=False,  # uncomment to unleash data management goodness
#     verbose_name=_("Data Manager's Endorsement"),
#     blank=True, null=True,
#     max_length=100,
#     choices=Document.ENDORSEMENT_NULL_CHOICES,
#     help_text=_("The Data Manager's endorsement of the project's "
#                 "data management. The DM will help to set up Wiki"
#                 "pages, data catalogue permissions, scientific sites, "
#                 "and advise on metadata creation."))

# operating_budget = PythiaArrayField(
#     verbose_name=_("Consolidated Funds"),
#     blank=True, null=True,
#     help_text=_("Estimated budget: consolidated DBCA funds"),
#     default=json.dumps([
#         ['Source', 'Year 1', 'Year 2', 'Year 3'],
#         ['FTE Scientist', '', '', ''],
#         ['FTE Technical', '', '', ''],
#         ['Equipment', '', '', ''],
#         ['Vehicle', '', '', ''],
#         ['Travel', '', '', ''],
#         ['Other', '', '', ''],
#         ['Total', '', '', ''],
#     ], cls=DjangoJSONEncoder))

# operating_budget_external = PythiaArrayField(
#     verbose_name=_("External Funds"), blank=True, null=True,
#     help_text=_("Estimated budget: external funds"),
#     default=json.dumps([
#         ['Source', 'Year 1', 'Year 2', 'Year 3'],
#         ['Salaries, Wages, Overtime', '', '', ''],
#         ['Overheads', '', '', ''],
#         ['Equipment', '', '', ''],
#         ['Vehicle', '', '', ''],
#         ['Travel', '', '', ''],
#         ['Other', '', '', ''],
#         ['Total', '', '', ''],
#     ], cls=DjangoJSONEncoder))


# Progress Report
#       template = "admin/pythia/ararreport/includes/progressreport.html"
#       template_tex = "latex/includes/progressreport.tex"
#       is_final_report = models.BooleanField(
#         verbose_name=_("Is final report"),
#         default=False, editable=False,
#         help_text=_("Whether this report is the final progress report "
#                     "after submitting a project closure request."))
#     year = models.PositiveIntegerField(
#         verbose_name=_("Report year"),
#         editable=False,
#         default=lambda: date.today().year,
#         help_text=_("The year on which this progress report reports on "
#                     "with four digits, e.g. 2014 for FY 2013/14."))
#     report = models.ForeignKey(
#         ARARReport,
#         blank=True, null=True,
#         editable=False,
#         help_text=_("The annual report publishing this StudentReport"))
#     context = models.TextField(
#         verbose_name=_("Context"),
#         blank=True, null=True,
#         help_text=_("A shortened introduction / background for the annual "
#                     "activity update. Aim for 100 to 150 words."))
#     aims = models.TextField(
#         verbose_name=_("Aims"),
#         blank=True, null=True,
#         help_text=_("A bullet point list of aims for the annual activity "
#                     "update. Aim for 100 to 150 words. One bullet point per "
#                     "aim."))
#     progress = models.TextField(
#         verbose_name=_("Progress"),
#         blank=True, null=True,
#         help_text=_("Current progress and achievements for the annual "
#                     "activity update. Aim for 100 to 150 words. One bullet "
#                     "point per achievement."))
#     implications = models.TextField(
#         verbose_name=_("Management implications"),
#         blank=True, null=True,
#         help_text=_("Management implications for the annual activity update. "
#                     "Aim for 100 to 150 words. One bullet point per "
#                     "implication."))
#     future = models.TextField(
#         verbose_name='Future directions',
#         blank=True, null=True,
#         help_text=_("Future directions for the annual activity update. Aim "
#                     "for 100 to 150 words. One bullet point per direction."))


# ProjectClosure
# template = "admin/pythia/ararreport/includes/projectclosure.html"
# template_tex = "latex/includes/projectclosure.tex"
# goal (choices - completed, force_completed, terminated, suspended: The intended project status outcome of this closure)
# reason / justification ("Why is this project being closed?")
# scientific_outputs = (List of publications/docs belonging to this. CREATE PUBLICATIONS MODEL)
# knowledge_transfer (List of knowledge transfer achievements)
# data_location (text field of links to the projects - href=\"http://internal-data.dpaw.wa.gov.au)
# hardcopy_location (textfield)
# backup_location (location of electronic backup data) POTENTIALLY MAKE A PROJECT_DATA table


# StudentReport
# template = "admin/pythia/ararreport/includes/studentreport.html"
# template_tex = "latex/includes/studentreport.tex"
# year (default auto add now)
# progress_report (max 150 words)
# report (ARARReport FK - the annual report it belongs to)


# Abstract Audit Model (Management?) - creator, modifier: pythia.models.260
# StaffTimeEstimate(Audit)
# creator, modifier
# document
# role
# staff
# year 1
# year 2
# year 3
