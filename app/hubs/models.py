from django.db import models

from app.abstracts import IntegerIDModel,TimeStampedModel
from app.user_auth.models import User
# from app.events.models import Event

import cloudinary.uploader
from cloudinary.models import CloudinaryField
from typing import Any

from django.dispatch import receiver
from django.db.models.signals import (
    pre_delete,
)


class Hub(IntegerIDModel):
    name = models.CharField(max_length=100, unique=True, blank=False)
    hub_profile_image = CloudinaryField(
        "Hub profile image", null=True, blank=True)
    description = models.TextField()
    members = models.ManyToManyField(User, related_name="hubs", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    hub_admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


@receiver(pre_delete, sender=Hub)
def remove_image_from_cloudinary(
   sender: Any, instance: Any, *args: Any, **kwargs: Any
) -> None:
    if hasattr(instance, "hub_profile_image") and instance.hub_profile_image is not None and instance.hub_profile_image.public_id:
        cloudinary.uploader.destroy(
            instance.hub_profile_image.public_id, resource_type="image"
        )

# class HubProfile(IntegerIDModel):
#     hub = models.OneToOneField(Hub, on_delete=models.CASCADE)
#     hub_events = models.ManyToManyField(Event, blank=True)
#     hub_event_images = models.ManyToManyField("events.EventImage", blank=True)
#     def __str__(self) -> str:
#         return self.hub.name



class HubRegister(TimeStampedModel):
    hub = models.ForeignKey(Hub, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Members")

    def __str__(self) -> str:
        return self.hub.name