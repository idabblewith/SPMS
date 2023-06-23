# Generated by Django 4.2.2 on 2023-06-23 02:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("categories", "0001_initial"),
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentproject",
            name="creator_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_projects_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="studentproject",
            name="kind",
            field=models.ForeignKey(
                blank=True,
                help_text="The project type determines the approval and                     documentation requirements during the project's                     life span. Choose wisely - you will not be able                     to change the project type later.                     If you get it wrong, create a new project of the                     correct type and tell admins to delete the duplicate                     project of the incorrect type.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.projectcategory",
            ),
        ),
        migrations.AddField(
            model_name="studentproject",
            name="modifier_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_projects_modified",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="scienceproject",
            name="creator_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="science_projects_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="scienceproject",
            name="kind",
            field=models.ForeignKey(
                blank=True,
                help_text="The project type determines the approval and                     documentation requirements during the project's                     life span. Choose wisely - you will not be able                     to change the project type later.                     If you get it wrong, create a new project of the                     correct type and tell admins to delete the duplicate                     project of the incorrect type.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.projectcategory",
            ),
        ),
        migrations.AddField(
            model_name="scienceproject",
            name="modifier_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="science_projects_modified",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="externalproject",
            name="creator_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="external_projects_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="externalproject",
            name="kind",
            field=models.ForeignKey(
                blank=True,
                help_text="The project type determines the approval and                     documentation requirements during the project's                     life span. Choose wisely - you will not be able                     to change the project type later.                     If you get it wrong, create a new project of the                     correct type and tell admins to delete the duplicate                     project of the incorrect type.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.projectcategory",
            ),
        ),
        migrations.AddField(
            model_name="externalproject",
            name="modifier_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="external_projects_modified",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="corefunctionproject",
            name="creator_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="core_function_projects_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="corefunctionproject",
            name="kind",
            field=models.ForeignKey(
                blank=True,
                help_text="The project type determines the approval and                     documentation requirements during the project's                     life span. Choose wisely - you will not be able                     to change the project type later.                     If you get it wrong, create a new project of the                     correct type and tell admins to delete the duplicate                     project of the incorrect type.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.projectcategory",
            ),
        ),
        migrations.AddField(
            model_name="corefunctionproject",
            name="modifier_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="core_function_projects_modified",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
