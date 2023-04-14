# Generated by Django 4.1.7 on 2023-04-13 21:13

import app.user_auth.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("events", "0001_initial"),
        ("chapters", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hubs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventattendees",
            name="attendee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="eventattendees",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="events.event"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="chapters_invited",
            field=models.ManyToManyField(
                blank=True, related_name="events_invited_to", to="chapters.chapter"
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="event_creator",
            field=models.ForeignKey(
                default=app.user_auth.models.User,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="event_creator",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="event_organizer_chapter",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="chapters.chapter",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="event_organizer_hub",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="hubs.hub",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="hubs_invited",
            field=models.ManyToManyField(
                blank=True, related_name="events_invited_to", to="hubs.hub"
            ),
        ),
    ]
