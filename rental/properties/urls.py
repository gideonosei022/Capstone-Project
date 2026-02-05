from django.urls import path
from . import views

urlpatterns = [
    # Example API endpoint
    path('', views.property_list, name='property-list'),
]
