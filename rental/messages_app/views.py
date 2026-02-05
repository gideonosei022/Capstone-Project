from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer

class MessageViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(sender=user) | Message.objects.filter(receiver=user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

MESSAGES = []

@csrf_exempt
def message_list(request):
    if request.method == 'GET':
        return JsonResponse(MESSAGES, safe=False)

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        MESSAGES.append(data)
        return JsonResponse({"message": "Message sent successfully!"}, status=201)
