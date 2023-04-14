from django.contrib import admin
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

User = get_user_model()


class UserAdmin(DjangoUserAdmin):
    model = User

    list_display = (
        # "id",
        "email",
        "first_name",
        "last_name",
        "username",
        "is_active",
        "is_staff",
        "is_superuser",
        "user_group",
    )

    list_filter = ("is_staff", "is_superuser")
    search_fields = ("email", "first_name", "username", "last_name")
    ordering = ("first_name", "last_name")
    filter_horizontal = ("groups", "user_permissions")

    fieldsets = (
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "password",
                )
            },
        ),
        (
            "Contact info",
            {"fields": ("phone_number", "email")},
        ),
        ("Important dates", {"fields": ("last_login",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_group",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            "Personal info",
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            "Contact info",
            {"fields": ("phone_number", "email")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_group",
                )
            },
        ),
    )


admin.site.register(User, UserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "dob", "bio")


admin.site.register(Profile, ProfileAdmin)
