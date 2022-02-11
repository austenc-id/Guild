from django.urls import path, include
from .views import *


app_name = 'patrons'
urlpatterns = [
    path('', index, name='index'),
    path('new', new_patron, name='new'),
    path('view', view_patrons, name='view'),
]
