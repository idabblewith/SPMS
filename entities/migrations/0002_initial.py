# Generated by Django 4.2.2 on 2023-06-22 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("entities", "0001_initial"),
        ("medias", "0001_initial"),
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
            model_name="entity",
            name="key_stakeholder",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="division",
            name="approver",
            field=models.ForeignKey(
                blank=True,
                help_text="The Approver receives notifications about outstanding requests and has permission             to approve documents. The approver can be anyone in a supervisory role, including the Director.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="divisions_approved",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="division",
            name="director",
            field=models.ForeignKey(
                blank=True,
                help_text="The Division's director is attributed as head of the Division in reports",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="divisions_led",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="businessarea",
            name="data_custodian",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="business_area_data_handled",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="businessarea",
            name="entity_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="entities.entity"
            ),
        ),
        migrations.AddField(
            model_name="businessarea",
            name="finance_admin",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="business_area_finances_handled",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="businessarea",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="medias.businessareaphoto",
            ),
        ),
        migrations.AddField(
            model_name="businessarea",
            name="leader",
            field=models.ForeignKey(
                blank=True,
                default=1,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="business_areas_led",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="branch",
            name="entity",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="entities.entity",
            ),
        ),
        migrations.AddField(
            model_name="branch",
            name="manager",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
