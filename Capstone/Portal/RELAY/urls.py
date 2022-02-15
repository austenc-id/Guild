from django.urls import path, include
from .views import *


app_name = 'relay'
urlpatterns = [
    path('invoke/', invoke, name='invoke')
]
