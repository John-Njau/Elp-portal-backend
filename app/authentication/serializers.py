from typing import Any

from django.contrib.auth import (
    authenticate,
    get_user_model,
)
from django.core.validators import RegexValidator
from django.template.loader import render_to_string
from rest_framework import (
    exceptions,
    serializers,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):  # type: ignore
    @classmethod
    def get_token(cls, user: Any) -> Any:
        token = super().get_token(user)
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["phone_number"] = user.phone_number
        token["email"] = user.email
        token["username"] = user.username
        return token
