from enum import IntEnum
from django.contrib.auth.models import Group



class UserGroup(IntEnum):
    USER = 100
    HUB_ADMIN = 200
    CHAPTER_ADMIN = 300
    STAFF_ADMIN = 400
    SUPER_ADMIN = 500

    @classmethod
    def choose_user_group(cls):
        return [(key.value, key.name) for key in cls]


"""
 This code ties the created user groups with the django admin user groups
"""


def create_or_update_user_groups(user, user_group):
    if user_group == UserGroup.USER.value:
        group, created = Group.objects.get_or_create(name="user")
        user.groups.add(group)
    elif user_group == UserGroup.HUB_ADMIN.value:
        group, created = Group.objects.get_or_create(name="hub_admin")
        user.groups.add(group)
    elif user_group == UserGroup.CHAPTER_ADMIN.value:
        group, created = Group.objects.get_or_create(name="chapter_admin")
        user.groups.add(group)
    elif user_group == UserGroup.STAFF_ADMIN.value:
        group, created = Group.objects.get_or_create(name="staff_admin")
        user.groups.add(group)
    elif user_group == UserGroup.SUPER_ADMIN.value:
        group, created = Group.objects.get_or_create(name="super_admin")
        user.groups.add(group)


# USER_GROUPS = [
#     (UserGroup.USER.value, "user"),
#     (UserGroup.HUB_ADMIN.value, "hub_admin"),
#     (UserGroup.CHAPTER_ADMIN.value, "chapter_admin"),
#     (UserGroup.STAFF_ADMIN.value, "staff_admin"),
# ]

# USER_GROUPS = {"hub_admin":"200", "chapter_admin":"300", "staff_admin":"400", "user":"100"}

# hub_admin = 200
# chapter_admin = 300
# staff_admin = 400
# user = 100
