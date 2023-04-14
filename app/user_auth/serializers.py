from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model
from app.user_auth.constant import UserGroup

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model.
    """

    # roles = serializers.SerializerMethodField()
    # role = serializers.CharField(max_length=255, write_only=True, default="100")
    user_group = serializers.ChoiceField(choices=UserGroup, default="100")

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "username",
            "password",
            "gender",
            "scholar_type",
            "scholar_code",
            "PF",
            # "role",
            # "roles",
            "user_group",
            "phone_number",
            "is_staff",
            "is_superuser",
        )
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = (
            "id",
            "roles",
        )

    def validate_password(self, value: str):
        """
        User password validation.

        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must be at least 8 characters long."
            )
        if value.isalpha():
            raise serializers.ValidationError(
                "Password must contain at least one number."
            )
        if value.isnumeric():
            raise serializers.ValidationError(
                "Password must contain at least one letter."
            )
        if value.islower():
            raise serializers.ValidationError(
                "Password must contain at least one uppercase letter."
            )
        if value.isupper():
            raise serializers.ValidationError(
                "Password must contain at least one lowercase letter."
            )
        if value.isalnum():
            raise serializers.ValidationError(
                "Password must contain at least one special character."
            )
        return make_password(value)

    def get_roles(self, obj):
        return list(obj.groups.values_list("name", flat=True))

    # def create(self, validated_data):
        # role = validated_data.pop("role")
        # user_group = validated_data.pop("user_group")
        # password = validated_data.pop("password")
        # user = User(**validated_data)
        # user.set_password(password)
        # user.save()

        # if user_group == 100:
        #     group = Group.objects.get_or_create(name="user")
        #     user.groups.add(group)
        # elif user_group == 200:
        #     group = Group.objects.get_or_create(name="hub_admin")
        #     user.groups.add(group)
        # elif user_group == 300:
        #     group = Group.objects.get_or_create(name="chapter_admin")
        #     user.groups.add(group)
        # elif user_group == 400:
        #     group = Group.objects.get_or_create(name="staff_admin")
        #     user.groups.add(group)
        # user = User.objects.create(**validated_data)
        # group = Group.objects.get_or_create(name=role)
        # user.groups.add(group[0])

        # return user
