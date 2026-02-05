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

from django.http import JsonResponse

def property_list(request):
    # temporary example data
    data = [
        {"id": 1, "title": "Room A", "location": "Lagos", "price": 50000},
        {"id": 2, "title": "Room B", "location": "Abuja", "price": 60000},
    ]
    return JsonResponse(data, safe=False)