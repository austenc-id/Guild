"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# * Project API imports
from rest_framework.routers import *
from app_Patrons.viewsets import PatronAPIViewset

# * API router and app registartions
router = DefaultRouter()
router.register(r'patrons', PatronAPIViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    # * API urls
    path('api/', include(router.urls)),
    # * App URLs
    path('', include('app_Home.urls')),
    path('patrons/', include('app_Patrons.urls')),
    path('user/', include('app_Users.urls')),

]
