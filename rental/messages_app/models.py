from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User
from properties.models import Property

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
