from django.urls import path
from . import views

urlpatterns = [
    # List all favorites for the logged-in user
    path('', views.favorite_list, name='favorite-list'),
    # Add a new favorite
    path('add/', views.add_favorite, name='add-favorite'),
]
