from rest_framework import viewsets  # type: ignore
from apis import serializers
from apis.models import School
from apis.filters import SchoolFilter


class SchoolViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.SchoolDetailSerializer
    queryset = School.objects.all()
    filterset_class = SchoolFilter
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     """Retrieve recipes for authenticated user."""
    #     return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.SchoolSerializer
        return self.serializer_class

    # def perform_create(self, serializer):
    #     """Create a new recipe."""
    #     serializer.save(user=self.request.user)