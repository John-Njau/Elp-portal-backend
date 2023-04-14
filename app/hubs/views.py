from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Hub, HubRegister
from .serializers import HubSerializer, HubRegisterSerializer


class HubRegisterViewSet(viewsets.ModelViewSet):
    serializer_class = HubRegisterSerializer
    queryset = HubRegister.objects.all()

    # permission_classes = (
    #     IsAuthenticated,
    #     IsAdminUser,
    # )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HubViewSet(viewsets.ModelViewSet):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer
    # permission_classes = (
    #     IsAuthenticated,
    #     IsAdminUser,
    # )

