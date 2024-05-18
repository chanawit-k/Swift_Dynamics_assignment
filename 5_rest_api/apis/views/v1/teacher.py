from rest_framework import viewsets  # type: ignore
from apis import serializers, filters
from apis.models import Teacher


class TeacherViewSet(viewsets.ModelViewSet):
    """View for managing classroom APIs."""
    serializer_class = serializers.TeacherDetailSerializer
    queryset = Teacher.objects.all()
    filterset_class = filters.TeacherFilter

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.TeacherSerializer
        return self.serializer_class
