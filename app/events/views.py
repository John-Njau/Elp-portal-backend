# from rest_framework.permissions import IsAuthenticated

from app.events.serializers import EventSerializer, EventAdminSerializer, EventAttendeesSerializer

from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.events.models import Event, EventAttendees
from rest_framework import viewsets, status

@api_view(['GET'])
def event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def event_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EventSerializer(event)
    return Response(serializer.data)


class EventCreate(generics.CreateAPIView):
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


class EventRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return EventAdminSerializer
        return EventSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        event = serializer.save()
        return Response(EventSerializer(event).data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)
    serializer_class = EventSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]


# event attendees views
class EventAttendeesCreateViewSet(viewsets.ModelViewSet):
    serializer_class = EventAttendeesSerializer
    queryset = EventAttendees.objects.all()
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
