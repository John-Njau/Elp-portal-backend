from django.contrib import admin
from django.urls import path

from .views import (
    CustomUserCreateView,
    CustomUserListView,
    CustomUserRetrieveUpdateDestroyView,
    # UserCreateView,
)

urlpatterns = [
    path(
        "user/userList/",
        CustomUserListView.as_view(),
        name="user-list",
    ),
    path(
        "user/get-user/<str:pk>/",
        CustomUserRetrieveUpdateDestroyView.as_view(),
        name="user-detail",
    ),
    path(
        "user/register/",
        CustomUserCreateView.as_view(),
        name="user-create",
    ),
    #     path(
    #         "register/",
    #         UserCreateView.as_view(),
    #         name="register",
    #     ),
]
