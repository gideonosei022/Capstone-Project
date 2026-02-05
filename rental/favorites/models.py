from django.db import models
from accounts.models import User
from properties.models import Property

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.property.title}"
