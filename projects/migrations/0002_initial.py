# Generated by Django 4.2.2 on 2023-07-08 02:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0001_initial"),
        ("locations", "0001_initial"),
        ("agencies", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="researchfunction",
            name="leader",
            field=models.ForeignKey(
                blank=True,
                help_text="The scientist in charge of the Research Function",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="research_functions_led",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Function Leader",
            ),
        ),
        migrations.AddField(
            model_name="projectmember",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="members",
                to="projects.project",
            ),
        ),
        migrations.AddField(
            model_name="projectmember",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="member_of",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="projectdetail",
            name="creator",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="projects_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="projectdetail",
            name="data_custodian",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="projects_where_data_custodian",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="projectdetail",
            name="modifier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="projects_modified",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="projectdetail",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="projects_owned",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="projectdetail",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="details",
                to="projects.project",
            ),
        ),
        migrations.AddField(
            model_name="projectdetail",
            name="research_function",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="projects.researchfunction",
            ),
        ),
        migrations.AddField(
            model_name="projectdetail",
            name="site_custodian",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="projects_where_site_custodian",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="projectarea",
            name="area",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="projects_in_area",
                to="locations.area",
            ),
        ),
        migrations.AddField(
            model_name="projectarea",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="areas",
                to="projects.project",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="business_area",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="agencies.businessarea",
            ),
        ),
        migrations.AddField(
            model_name="externalprojectdetails",
            name="project",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="external_project_info",
                to="projects.project",
            ),
        ),
    ]
