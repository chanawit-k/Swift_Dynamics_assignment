from rest_framework import viewsets, status
from rest_framework.response import Response
from apis import serializers, filters
from apis.models import Student


class StudentViewSet(viewsets.ModelViewSet):
    """View for managing Student APIs."""
    serializer_class = serializers.StudentDetailSerializer
    queryset = Student.objects.all()
    filterset_class = filters.StudentFilter

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.StudentSerializer
        return self.serializer_class

