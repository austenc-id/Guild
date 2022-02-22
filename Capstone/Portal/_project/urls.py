from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # * App URLs
    path('', include('HOME.urls')),
    path('portal/', include('PATRONS.urls')),
    path('relay/', include('RELAY.urls')),
]
