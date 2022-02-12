"""
project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

# * Project API imports
from rest_framework.routers import *
# from app_Patrons.viewsets import PatronAPIViewset

# * API router and app registartions
router = DefaultRouter()
# router.register(r'patrons', PatronAPIViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    # * API urls
    path('api/', include(router.urls)),
    # * App URLs
    path('', include('HOME.urls')),
    path('portal/', include('PATRONS.urls')),
]
