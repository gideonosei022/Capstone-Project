from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User

class Property(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10)
    description = models.TextField()
    amenities = models.TextField(blank=True)
    availability = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
