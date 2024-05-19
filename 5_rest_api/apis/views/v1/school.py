from rest_framework import viewsets
from apis import serializers, filters
from apis.models import (
    School,
    ClassRoom
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class SchoolViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.SchoolDetailSerializer
    queryset = School.objects.all()
    filterset_class = filters.SchoolFilter

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.SchoolSerializer
        return self.serializer_class


class ClassRoomViewSet(viewsets.ModelViewSet):
    """View for managing classroom APIs."""
    serializer_class = serializers.ClassRoomDetailSerializer
    queryset = ClassRoom.objects.all()
    filterset_class = filters.ClassRoomFilter

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.ClassRoomSerializer
        return self.serializer_class
