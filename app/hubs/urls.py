from django.urls import path, include

from rest_framework import routers

from .views import (
    HubViewSet,
    HubRegisterViewSet,
)

router = routers.DefaultRouter()
router.register(r"register", HubRegisterViewSet, basename="hub_register")
router.register(r"", HubViewSet, basename="hub")

urlpatterns = [
    path("hubs/", include(router.urls)),
]
