from django.urls import path, include
from rest_framework import routers

from app.events.views import event_list, event_detail, EventCreate, EventRetrieveUpdateDestroy, EventAttendeesCreateViewSet

router = routers.DefaultRouter()
router.register(r'attendees', EventAttendeesCreateViewSet, basename='event-attendees')


urlpatterns = [
    path('events/', event_list, name='event-list'),
    path('events/create/', EventCreate.as_view(), name='event-create'),
    path('events/<int:pk>/', event_detail, name='event-detail'),
    path('events/<int:pk>/update/',
         EventRetrieveUpdateDestroy.as_view(), name='event-update'),
    path('events/', include(router.urls)),

]
