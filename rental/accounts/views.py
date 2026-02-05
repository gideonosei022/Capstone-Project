from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from .models import User

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
