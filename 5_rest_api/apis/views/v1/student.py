from rest_framework import viewsets
from apis import serializers, filters
from apis.models import Student


class StudentViewSet(viewsets.ModelViewSet):
    """View for managing classroom APIs."""
    serializer_class = serializers.StudentSerializer
    queryset = Student.objects.all()
    filterset_class = filters.StudentFilter

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.StudentSerializer
        return self.serializer_class
