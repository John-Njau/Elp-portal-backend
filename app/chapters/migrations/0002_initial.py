# Generated by Django 4.1.7 on 2023-04-13 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("chapters", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="chapterregister",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Members",
            ),
        ),
        migrations.AddField(
            model_name="chapter",
            name="chapter_admin",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="chapter",
            name="members",
            field=models.ManyToManyField(
                blank=True,
                related_name="chapters",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Chapter Members",
            ),
        ),
    ]
