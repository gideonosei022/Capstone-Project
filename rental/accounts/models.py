from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('owner', 'Owner/Agent'),
        ('tenant', 'Tenant'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
