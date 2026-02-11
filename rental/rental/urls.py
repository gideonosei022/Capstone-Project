"""
URL configuration for rental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rental.properties.views import PropertyViewSet
from rental.favorites.views import FavoriteViewSet
from rental.messages_app.views import MessageViewSet
from django.views.generic import TemplateView

router = DefaultRouter()
router.register('rental.properties', PropertyViewSet)
router.register('rental.favorites', FavoriteViewSet, basename='favorites')
router.register('rental.messages', MessageViewSet, basename='messages')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('rental.accounts.urls')),
    path('api/properties/', include('rental.properties.urls')),
    path('api/favorites/', include('rental.favorites.urls')),
    path('api/messages/', include('rental.messages_app.urls')),
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/', include('rental.rental.urls')),
]
#from django.views.generic import TemplateView


# keep your API routes




