# Generated by Django 4.2.2 on 2023-07-07 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("agencies", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("medias", "0001_initial"),
    ]

    operations = [
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
            model_name="departmentalservice",
            name="director",
            field=models.ForeignKey(
                blank=True,
                help_text="The Service's Director",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="services_led",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="businessarea",
            name="agency",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="agencies.agency"
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
            name="agency",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="agencies.agency",
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
        migrations.AddField(
            model_name="agency",
            name="key_stakeholder",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
