from enum import IntEnum
from typing import Any

import cloudinary.uploader
from cloudinary.models import CloudinaryField
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    Group,
)
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import (
    pre_delete,
)
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _

from app.abstracts import TimeStampedModel, IntegerIDModel

from app.user_auth.constant import UserGroup, create_or_update_user_groups


"""class UserEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        abstract = True"""


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email: str, password: str, **kwargs: Any) -> Any:
        """
        Creates and saves a User with the given phone_number and password.
        """

        user = self.model(email=email, **kwargs)
        # user.password = make_password(password)
        user.set_password(password)

        # self.password = make_password(self.password)
        user.save()
        return user

    def create_user(self, email: str, password: str, **kwargs: Any) -> Any:
        kwargs.setdefault("is_superuser", False)
        # kwargs.setdefault("is_staff", False)
        # kwargs.setdefault("is_active", True)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email: str, password: str, **kwargs: Any) -> Any:
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_staff", True)
        superuser = self._create_user(email, password, **kwargs)
        group, _ = Group.objects.get_or_create(name=UserGroup.SUPER_ADMIN.value)
        superuser.groups.add(group)

        return superuser

    """def create_user(self, email, first_name, last_name, password=None, **extra_fields):
    
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        # extra_fields.setdefault("is_active", True)
        # user.is_active = True
        user.save()
        return user

    def create_superuser(
        self, email, first_name, last_name, password=None, **extra_fields
    ):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, first_name, last_name, password, **extra_fields)
"""


class GenderOption(IntEnum):
    Not_Selected = 0
    Male = 1
    Female = 2
    Other = 3

    @classmethod
    def choose_gender(cls):
        return [(key.value, key.name) for key in cls]


# proxy model, multi-modelling inheritance, django import export


class ScholarTypeOption(IntEnum):
    ELP = 1
    WTF = 2
    Both = 3

    @classmethod
    def choose_scholar_type(cls):
        return [(key.value, key.name) for key in cls]




class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel, IntegerIDModel):
    """
    Custom user model to replace the default Django User model.
    """

    # password = models.CharField(verbose_name=_("Password"), max_length=128, blank=False)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)

    username = models.CharField(
        verbose_name=_("Username"), max_length=40, unique=True, blank=True
    )
    first_name = models.CharField(
        verbose_name=_("First Name"), max_length=30, blank=True
    )
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=30, blank=True)
    gender = models.IntegerField(
        verbose_name=_("Gender"),
        choices=GenderOption.choose_gender(),
        default=GenderOption.Not_Selected.value,
    )
    scholar_type = models.IntegerField(
        verbose_name=_("Scholar Type"),
        choices=ScholarTypeOption.choose_scholar_type(),
        default=ScholarTypeOption.WTF.value,
    )
    user_group = models.IntegerField(
        verbose_name=_("User Group"),
        choices=UserGroup.choose_user_group(),
        default=UserGroup.USER.value,
    )
    PF = models.CharField(verbose_name=_("PF number"), max_length=30, blank=True)
    phone_regex = RegexValidator(
        regex=r"^\+?[\d\s-]+$",
        message="Phone number must be in the format: '+xxxxxxxxxx'.",
    )
    phone_number = models.CharField(
        verbose_name=_("phone number"),
        validators=[phone_regex],
        max_length=15,
        unique=False,
        blank=True,
    )
    scholar_code = models.CharField(
        verbose_name=_("Scholar Code"), max_length=30, blank=True
    )
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return "{}".format(self.email.split("@")[0])

    def get_full_name(self) -> str:
        return f"{self.first_name or ''} {self.last_name or ''}"

    def get_scholar_code(self):
        return self.scholar_code

    def get_pf(self):
        return self.PF

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email.split("@")[0]
        super().save(*args, **kwargs)
        create_or_update_user_groups(self, self.user_group)

    


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_("Username"),
        on_delete=models.CASCADE,
        related_name="profile",
    )
    dob = models.DateField(blank=True, null=True, verbose_name=_("Date of Birth"))
    bio = models.CharField(verbose_name=_("Bio"), max_length=140, blank=True, null=True)
    # avatar = models.ImageField(
    #     upload_to="avatars/", blank=True, null=True, verbose_name=_("Avatar")
    # )
    profile_pic = CloudinaryField("Profile picture", null=True, blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return str(self.user.email)

    def get_absolute_url(self):
        return reverse("profiles:profile", kwargs={"username": self.user.username})


@receiver(pre_delete, sender=Profile)
def remove_image_from_cloudinary(
    sender: Any, instance: Any, *args: Any, **kwargs: Any
) -> None:
    if (
        hasattr(instance, "profile_pic")
        and instance.profile_pic is not None
        and instance.profile_pic.public_id
    ):
        cloudinary.uploader.destroy(
            instance.profile_pic.public_id, resource_type="image"
        )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
