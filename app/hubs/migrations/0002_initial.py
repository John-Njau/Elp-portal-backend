# Generated by Django 4.1.7 on 2023-04-13 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("hubs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="hubregister",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Members",
            ),
        ),
        migrations.AddField(
            model_name="hub",
            name="hub_admin",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="hub",
            name="members",
            field=models.ManyToManyField(
                blank=True, related_name="hubs", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
