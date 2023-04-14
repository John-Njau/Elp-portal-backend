from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView

from app.authentication.serializers import (
    MyTokenObtainPairSerializer,
)

User = get_user_model()


class MyTokenObtainPairView(TokenObtainPairView):  # type: ignore
    serializer_class = MyTokenObtainPairSerializer


