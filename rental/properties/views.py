from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Property
from .serializers import PropertySerializer
from .permissions import IsOwnerOrReadOnly

class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.filter(availability=True)
    serializer_class = PropertySerializer
    permission_classes = [IsOwnerOrReadOnly]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'location', 'description']
    ordering_fields = ['price']
    filterset_fields = ['type', 'location']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
