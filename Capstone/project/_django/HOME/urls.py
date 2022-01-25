from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path('', home, name='page'),
    path('profile', profile, name='profile')
]
