# clients/views.py
from rest_framework import viewsets
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)  # Assign the logged-in user as creator

    @action(detail=True, methods=['get'])
    def projects(self, request, pk=None):
        """Custom action to retrieve projects of a client."""
        client = self.get_object()
        projects = client.projects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)  # Assign the logged-in user as creator
