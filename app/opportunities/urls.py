from django.urls import path, include
from rest_framework import routers

from . import views
from .views import (
    OpportunityDetail,
    # DepartmentDetail,
    DepartmentList,
)

router = routers.DefaultRouter()
router.register(
    r"registration", views.OpportunityRegisterViewSet, basename="opportunity_register"
)
router.register(r"", views.OpportunityViewSet, basename="opportunity")

urlpatterns = [
    path("opportunities/", include(router.urls)),
    path(
        "opportunities/opportunity/<str:pk>/", OpportunityDetail.as_view(), name="opportunity-detail"
    ),
    # path("department/<str:pk>/", DepartmentDetail.as_view(), name="department-detail"),
    path("opportunities/department/", DepartmentList.as_view(), name="department-list"),
]
