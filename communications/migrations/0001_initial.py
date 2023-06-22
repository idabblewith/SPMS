# Generated by Django 4.2.2 on 2023-06-21 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChatRoom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Chat Room",
                "verbose_name_plural": "Chat Rooms",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("text", models.CharField(max_length=500)),
                ("ip_address", models.CharField(blank=True, max_length=45, null=True)),
                ("is_public", models.BooleanField(default=True)),
                ("is_removed", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
            },
        ),
        migrations.CreateModel(
            name="CommentReaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "reaction",
                    models.CharField(
                        choices=[
                            ("thumbup", "Thumbs Up"),
                            ("thumbdown", "Thumbs Down"),
                            ("heart", "Heart"),
                            ("brokenheart", "Broken Heart"),
                            ("hundred", "Hundred"),
                            ("confused", "Confused"),
                            ("funny", "Funny"),
                            ("suprised", "Suprised"),
                        ],
                        max_length=30,
                    ),
                ),
            ],
            options={
                "verbose_name": "Comment Reaction",
                "verbose_name_plural": "Comment Reactions",
            },
        ),
        migrations.CreateModel(
            name="DirectMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("text", models.TextField()),
                ("ip_address", models.CharField(blank=True, max_length=45, null=True)),
                ("is_public", models.BooleanField(default=True)),
                ("is_removed", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Direct Message",
                "verbose_name_plural": "Direct Messages",
            },
        ),
        migrations.CreateModel(
            name="DirectMessageReaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "reaction",
                    models.CharField(
                        choices=[
                            ("thumbup", "Thumbs Up"),
                            ("thumbdown", "Thumbs Down"),
                            ("heart", "Heart"),
                            ("brokenheart", "Broken Heart"),
                            ("hundred", "Hundred"),
                            ("confused", "Confused"),
                            ("funny", "Funny"),
                            ("suprised", "Suprised"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "direct_message",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dm_reactions",
                        to="communications.directmessage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Direct Message Reaction",
                "verbose_name_plural": "Direct Message Reactions",
            },
        ),
    ]
