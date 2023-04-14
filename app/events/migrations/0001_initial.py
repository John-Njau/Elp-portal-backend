# Generated by Django 4.1.7 on 2023-04-13 21:13

import app.user_auth.models
import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Updated at"
                    ),
                ),
                (
                    "id",
                    models.CharField(
                        editable=False,
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("venue", models.CharField(max_length=100)),
                (
                    "poster",
                    cloudinary.models.CloudinaryField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Event Poster",
                    ),
                ),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                (
                    "charges",
                    models.FloatField(blank=True, null=True, verbose_name="charges"),
                ),
                ("description", models.TextField()),
                (
                    "event_organizer",
                    models.CharField(
                        choices=[
                            ("hub", "Hub"),
                            ("chapter", "Chapter"),
                            ("user", "User"),
                        ],
                        default=app.user_auth.models.User,
                        max_length=10,
                    ),
                ),
            ],
            options={
                "verbose_name": "Event",
                "verbose_name_plural": "Events",
                "ordering": ["-date", "-time"],
            },
        ),
        migrations.CreateModel(
            name="EventAttendees",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Updated at"
                    ),
                ),
            ],
            options={
                "verbose_name": "Event Attendee",
                "verbose_name_plural": "Event Attendees",
                "ordering": ["-created_at"],
            },
        ),
    ]