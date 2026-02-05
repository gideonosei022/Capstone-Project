from rest_framework import viewsets
from .models import Favorite
from .serializers import FavoriteSerializer
from rest_framework.permissions import IsAuthenticated

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Temporary in-memory storage for testing
FAVORITES = []

@csrf_exempt
def favorite_list(request):
    # GET request returns all favorites
    if request.method == 'GET':
        return JsonResponse(FAVORITES, safe=False)

@csrf_exempt
def add_favorite(request):
    # POST request to add a favorite
    if request.method == 'POST':
        data = json.loads(request.body)
        FAVORITES.append(data)
        return JsonResponse({"message": "Favorite added successfully!"}, status=201)
