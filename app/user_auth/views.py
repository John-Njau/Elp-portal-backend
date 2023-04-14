from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from app.user_authentication import CustomAuthenticationBackend
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
)
from django.contrib.auth import get_user_model
User = get_user_model()


class CustomUserCreateView(generics.CreateAPIView):
    """
    View to create a new user.
    """
    queryset = User.objects.prefetch_related("groups").all()
    serializer_class = UserSerializer
    """permission_classes = (
        IsAuthenticated,
        IsAdminUser,
    )"""


class CustomUserListView(generics.ListAPIView):
    """
    View to list all users.
    """

    serializer_class = UserSerializer
    queryset = User.objects.prefetch_related("groups").all()


class CustomUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a single user.
    """

    serializer_class = UserSerializer
    queryset = User.objects.prefetch_related("groups").all()

    """permission_classes = (
        IsAuthenticated,
        IsAdminUser,
    )"""


class CustomAuthToken(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (AllowAny,)
    authentication_classes = (CustomAuthenticationBackend,)


class ProfileViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        IsAuthenticated,
        IsAdminUser,
    )
