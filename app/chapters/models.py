from typing import Any

import cloudinary.uploader
from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models.signals import (
    pre_delete,
)
from django.dispatch import receiver

from app.abstracts import TimeStampedModel
from app.user_auth.models import User


class Chapter(models.Model):
    name = models.CharField(max_length=100)
    chapter_profile_image = CloudinaryField("chapter", null=True, blank=True)
    institution = models.CharField(max_length=100, blank=False)
    registration_fee = models.PositiveIntegerField(null=True, blank=True)
    description = models.CharField(max_length=250)
    members = models.ManyToManyField(
        User, related_name="chapters", blank=True, verbose_name="Chapter Members")
    created_on = models.DateTimeField(auto_now_add=True)
    chapter_admin = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = ('Chapters')

    def __str__(self) -> str:
        return self.name


@receiver(pre_delete, sender=Chapter)
def remove_image_from_cloudinary(sender: Any, instance: Any, *args: Any, **kwargs: Any) -> None:
    if hasattr(instance, 'chapter_profile_image') and instance.chapter_profile_image is not None and instance.chapter_profile_image.public_id:
        cloudinary.uploader.destroy(instance.chapter_profile_image.public_id, invalidate=True ,resource_type="image")


class ChapterRegister(TimeStampedModel):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Members")

    def __str__(self) -> str:
        return self.chapter.name
